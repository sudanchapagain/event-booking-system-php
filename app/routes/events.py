from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Request,
    Form,
    UploadFile,
    File,
)
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os
import shutil

from .. import models
from ..core import database
from ..core.dependencies import get_current_user, get_current_user_optional

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["Events"])


@router.post("/new", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def create_event(
    request: Request,
    title: str = Form(...),
    location: str = Form(...),
    start_date: str = Form(...),
    end_date: str = Form(...),
    capacity: int = Form(...),
    description: str = Form(...),
    category: int = Form(None),
    ticket_price: float = Form(0.0),
    event_image: UploadFile = File(None),
    db: Session = Depends(database.get_db),
    user: models.User = Depends(get_current_user),
):
    errors = []

    if (
        not title
        or not location
        or not start_date
        or not end_date
        or capacity <= 0
        or not description
    ):
        errors.append("Please fill in all required fields correctly.")

    if datetime.fromisoformat(start_date) >= datetime.fromisoformat(end_date):
        errors.append("Start date must be earlier than the end date.")

    event_image_url = None
    if event_image and event_image.filename:
        upload_dir = "app/static/uploads/events"
        os.makedirs(upload_dir, exist_ok=True)
        file_extension = os.path.splitext(event_image.filename)[1]
        file_name = f"{int(datetime.now().timestamp())}_{event_image.filename}"
        file_path = os.path.join(upload_dir, file_name)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(event_image.file, buffer)
        event_image_url = f"/static/uploads/events/{file_name}"

    if errors:
        categories_query = select(
            models.EventCategory.category_id, models.EventCategory.name
        )
        categories = (await db.execute(categories_query)).all()
        return templates.TemplateResponse(
            "new.jinja",
            {
                "request": request,
                "errors": errors,
                "categories": categories,
                "title": title,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "capacity": capacity,
                "description": description,
                "category": category,
                "ticket_price": ticket_price,
            },
        )

    try:
        new_event = models.Event(
            title=title,
            location=location,
            organizer_id=user.user_id,
            description=description,
            capacity=capacity,
            ticket_price=ticket_price,
            is_approved=False,
        )
        db.add(new_event)
        await db.commit()
        await db.refresh(new_event)

        if event_image_url:
            new_event_image = models.EventImage(
                event_id=new_event.event_id,
                image_url=event_image_url,
                image_type="main",
            )
            db.add(new_event_image)
            await db.commit()

        new_event_date = models.EventDate(
            event_id=new_event.event_id,
            start_date=datetime.fromisoformat(start_date),
            end_date=datetime.fromisoformat(end_date),
        )
        db.add(new_event_date)
        await db.commit()

        if category:
            new_category_mapping = models.EventCategoryMapping(
                event_id=new_event.event_id, category_id=category
            )
            db.add(new_category_mapping)
            await db.commit()

        return RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)

    except Exception as e:
        await db.rollback()
        errors.append(f"Error creating event: {e}")
        categories_query = select(
            models.EventCategory.category_id, models.EventCategory.name
        )
        categories = (await db.execute(categories_query)).all()
        return templates.TemplateResponse(
            "new.jinja",
            {
                "request": request,
                "errors": errors,
                "categories": categories,
                "title": title,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "capacity": capacity,
                "description": description,
                "category": category,
                "ticket_price": ticket_price,
            },
        )


@router.get("/event/{event_id}/register")
async def register_for_event(
    event_id: int,
    request: Request,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    event = (
        await db.execute(
            select(models.Event).where(
                and_(
                    models.Event.event_id == event_id, models.Event.is_approved == True
                )
            )
        )
    ).scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing_booking = (
        await db.execute(
            select(models.UserEventAttendance).where(
                and_(
                    models.UserEventAttendance.user_id == current_user.user_id,
                    models.UserEventAttendance.event_id == event_id,
                )
            )
        )
    ).scalar_one_or_none()

    if existing_booking:
        return RedirectResponse(
            url=f"/event?event_id={event_id}&message=Already registered",
            status_code=status.HTTP_302_FOUND,
        )

    if event.ticket_price == 0:
        new_attendance = models.UserEventAttendance(
            user_id=current_user.user_id, event_id=event_id, status="confirmed"
        )
        db.add(new_attendance)
        await db.commit()

        return RedirectResponse(
            url=f"/event?event_id={event_id}&message=Successfully registered",
            status_code=status.HTTP_302_FOUND,
        )
    else:
        return RedirectResponse(
            url=f"/event?event_id={event_id}&message=Payment required - feature coming soon",
            status_code=status.HTTP_302_FOUND,
        )


@router.get("/event/{event_id}/cancel")
async def cancel_event_registration(
    event_id: int,
    request: Request,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    booking = (
        await db.execute(
            select(models.UserEventAttendance).where(
                and_(
                    models.UserEventAttendance.user_id == current_user.user_id,
                    models.UserEventAttendance.event_id == event_id,
                )
            )
        )
    ).scalar_one_or_none()

    if booking:
        await db.delete(booking)
        await db.commit()
        message = "Booking cancelled successfully"
    else:
        message = "No booking found to cancel"

    return RedirectResponse(
        url=f"/event?event_id={event_id}&message={message}",
        status_code=status.HTTP_302_FOUND,
    )


@router.post("/event/{event_id}/edit")
async def edit_event(
    event_id: int,
    request: Request,
    title: str = Form(...),
    location: str = Form(...),
    description: str = Form(...),
    capacity: int = Form(...),
    ticket_price: float = Form(...),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    event = (
        await db.execute(
            select(models.Event).where(
                and_(
                    models.Event.event_id == event_id,
                    models.Event.organizer_id == current_user.user_id,
                )
            )
        )
    ).scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found or unauthorized")

    if not title or not location or not description or capacity <= 0:
        return RedirectResponse(
            url=f"/event?event_id={event_id}&message=Please fill all fields correctly",
            status_code=status.HTTP_302_FOUND,
        )

    event.title = title
    event.location = location
    event.description = description
    event.capacity = capacity
    event.ticket_price = ticket_price

    await db.commit()

    return RedirectResponse(
        url=f"/event?event_id={event_id}&message=Event updated successfully",
        status_code=status.HTTP_302_FOUND,
    )


@router.get("/event/{event_id}/delete")
async def delete_event(
    event_id: int,
    request: Request,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    event = (
        await db.execute(select(models.Event).where(models.Event.event_id == event_id))
    ).scalar_one_or_none()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if not (current_user.user_id == event.organizer_id or current_user.is_admin):
        raise HTTPException(status_code=403, detail="Unauthorized")

    await db.execute(
        models.UserEventAttendance.__table__.delete().where(
            models.UserEventAttendance.event_id == event_id
        )
    )
    await db.execute(
        models.EventImage.__table__.delete().where(
            models.EventImage.event_id == event_id
        )
    )
    await db.execute(
        models.EventDate.__table__.delete().where(models.EventDate.event_id == event_id)
    )
    await db.execute(
        models.EventCategoryMapping.__table__.delete().where(
            models.EventCategoryMapping.event_id == event_id
        )
    )

    await db.delete(event)
    await db.commit()

    return RedirectResponse(
        url="/explore?message=Event deleted successfully",
        status_code=status.HTTP_302_FOUND,
    )
