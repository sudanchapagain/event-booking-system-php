from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy import select

from .routes import authentication, dashboard, events
from . import models
from .core import database
from .core.database import engine
from .core.dependencies import get_current_user_optional

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


app.include_router(authentication.router)
app.include_router(dashboard.router)
app.include_router(events.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(
    request: Request,
    current_user: models.User | None = Depends(get_current_user_optional),
):
    return templates.TemplateResponse(
        "index.jinja", {"request": request, "user": current_user}
    )


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, success: str = None):
    context = {"request": request}
    if success == "signup":
        context["message"] = "Account created successfully! Please sign in."
    return templates.TemplateResponse("login.jinja", context)


@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.jinja", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.jinja", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.jinja", {"request": request})


@app.get("/explore", response_class=HTMLResponse)
async def explore_page(
    request: Request,
    search: str = "",
    location: str = "",
    min_price: float = 0,
    max_price: float = 10000,
    category: int = None,
    start_date: str = None,
    end_date: str = None,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user_optional),
):
    from sqlalchemy import and_, or_, func
    from datetime import datetime

    query = (
        select(
            models.Event.event_id,
            models.Event.title,
            models.Event.location,
            models.Event.capacity,
            models.Event.ticket_price,
            models.EventDate.start_date,
            models.EventDate.end_date,
            models.EventCategory.name.label("category"),
        )
        .select_from(models.Event)
        .outerjoin(
            models.EventCategoryMapping,
            models.Event.event_id == models.EventCategoryMapping.event_id,
        )
        .outerjoin(
            models.EventCategory,
            models.EventCategoryMapping.category_id == models.EventCategory.category_id,
        )
        .outerjoin(models.EventDate, models.Event.event_id == models.EventDate.event_id)
        .where(models.Event.is_approved == True)
    )

    if search:
        query = query.where(models.Event.title.ilike(f"%{search}%"))

    if location:
        query = query.where(models.Event.location.ilike(f"%{location}%"))

    if category:
        query = query.where(models.EventCategoryMapping.category_id == category)

    if start_date:
        try:
            start_dt = datetime.fromisoformat(start_date + " 00:00:00")
            query = query.where(models.EventDate.start_date >= start_dt)
        except:
            pass

    if end_date:
        try:
            end_dt = datetime.fromisoformat(end_date + " 23:59:59")
            query = query.where(models.EventDate.end_date <= end_dt)
        except:
            pass

    if min_price != 0 or max_price != 10000:
        query = query.where(
            and_(
                models.Event.ticket_price >= min_price,
                models.Event.ticket_price <= max_price,
            )
        )

    query = query.order_by(models.EventDate.start_date.asc())

    events = (await db.execute(query)).all()

    categories_query = select(
        models.EventCategory.category_id, models.EventCategory.name
    )
    categories = (await db.execute(categories_query)).all()

    return templates.TemplateResponse(
        "explore.jinja",
        {
            "request": request,
            "events": events,
            "categories": categories,
            "user": current_user,
            "search": search,
            "location": location,
            "min_price": min_price,
            "max_price": max_price,
            "category": category,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


@app.get("/event", response_class=HTMLResponse)
async def event_page(
    request: Request,
    event_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user_optional),
):
    from sqlalchemy import func

    event_query = (
        select(
            models.Event,
            models.User.username.label("organizer_name"),
            models.User.user_id.label("organizer_id"),
            func.count(models.UserEventAttendance.user_id).label(
                "current_participants"
            ),
        )
        .outerjoin(models.User, models.Event.organizer_id == models.User.user_id)
        .outerjoin(
            models.UserEventAttendance,
            models.Event.event_id == models.UserEventAttendance.event_id,
        )
        .where(
            and_(models.Event.event_id == event_id, models.Event.is_approved == True)
        )
        .group_by(models.Event.event_id, models.User.username, models.User.user_id)
    )

    event_result = (await db.execute(event_query)).first()

    if not event_result:
        return templates.TemplateResponse(
            "404.jinja", {"request": request}, status_code=404
        )

    event = event_result[0]
    organizer_name = event_result.organizer_name
    organizer_id = event_result.organizer_id
    current_participants = event_result.current_participants

    image_query = (
        select(models.EventImage.image_url)
        .where(models.EventImage.event_id == event_id)
        .limit(1)
    )
    image_result = (await db.execute(image_query)).first()
    image_url = image_result[0] if image_result else None

    dates_query = select(models.EventDate).where(models.EventDate.event_id == event_id)
    dates_result = (await db.execute(dates_query)).first()

    is_booked = False
    if current_user:
        booking_query = select(models.UserEventAttendance).where(
            and_(
                models.UserEventAttendance.user_id == current_user.user_id,
                models.UserEventAttendance.event_id == event_id,
            )
        )
        booking_result = (await db.execute(booking_query)).first()
        is_booked = booking_result is not None

    is_event_organizer = current_user and current_user.user_id == organizer_id
    is_admin = current_user and current_user.is_admin
    is_organizer = current_user and current_user.is_organizer

    return templates.TemplateResponse(
        "event.jinja",
        {
            "request": request,
            "event": event,
            "organizer_name": organizer_name,
            "organizer_id": organizer_id,
            "current_participants": current_participants,
            "image_url": image_url,
            "event_dates": dates_result,
            "user": current_user,
            "is_booked": is_booked,
            "is_event_organizer": is_event_organizer,
            "is_admin": is_admin,
            "is_organizer": is_organizer,
        },
    )


@app.get("/dpa", response_class=HTMLResponse)
async def dpa_page(request: Request):
    return templates.TemplateResponse("dpa.jinja", {"request": request})


@app.get("/privacy", response_class=HTMLResponse)
async def privacy_page(request: Request):
    return templates.TemplateResponse("privacy.jinja", {"request": request})


@app.get("/terms", response_class=HTMLResponse)
async def terms_page(request: Request):
    return templates.TemplateResponse("terms.jinja", {"request": request})


@app.get("/new", response_class=HTMLResponse)
async def new_event_page(
    request: Request,
    current_user: models.User = Depends(get_current_user_optional),
    db: Session = Depends(database.get_db),
):
    if not current_user:
        return templates.TemplateResponse(
            "login.jinja",
            {"request": request, "message": "Please login to create events"},
        )

    categories_query = select(
        models.EventCategory.category_id, models.EventCategory.name
    )
    categories = (await db.execute(categories_query)).all()
    return templates.TemplateResponse(
        "new.jinja",
        {"request": request, "categories": categories, "user": current_user},
    )


@app.get("/profile", response_class=HTMLResponse)
async def profile_page(
    request: Request, current_user: models.User = Depends(get_current_user_optional)
):
    if not current_user:
        return templates.TemplateResponse(
            "login.jinja",
            {"request": request, "message": "Please login to view profile"},
        )
    return templates.TemplateResponse(
        "profile.jinja", {"request": request, "user": current_user}
    )


@app.get("/settings", response_class=HTMLResponse)
async def settings_page(
    request: Request, current_user: models.User = Depends(get_current_user_optional)
):
    if not current_user:
        return templates.TemplateResponse(
            "login.jinja",
            {"request": request, "message": "Please login to view settings"},
        )
    return templates.TemplateResponse(
        "settings.jinja", {"request": request, "user": current_user}
    )
