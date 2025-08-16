from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from ..core import database
from ..core.dependencies import get_current_user
from ..services.dashboard_service import DashboardService
from ..services.moderation_service import ModerationService
from .. import models

router = APIRouter(tags=["dashboard"], prefix="/dashboard")
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard_home(
    request: Request,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db),
):
    is_admin = await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    )
    is_organizer = await DashboardService.user_has_permission(
        current_user.user_id, "organizer", db
    )

    context = {
        "request": request,
        "user": current_user,
        "tab": "dashboard",
        "is_admin": is_admin,
        "is_organizer": is_organizer,
    }

    return templates.TemplateResponse("dashboard/home.jinja", context)


@router.get("/bookings", response_class=HTMLResponse)
async def dashboard_bookings(
    request: Request,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db),
):
    is_organizer = await DashboardService.user_has_permission(
        current_user.user_id, "organizer", db
    )
    is_admin = await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    )

    if not is_organizer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view bookings",
        )

    bookings = await DashboardService.get_user_bookings(current_user.user_id, db)

    context = {
        "request": request,
        "user": current_user,
        "tab": "bookings",
        "is_admin": is_admin,
        "is_organizer": is_organizer,
        "bookings": bookings,
    }

    return templates.TemplateResponse("dashboard/bookings.jinja", context)


@router.get("/sales", response_class=HTMLResponse)
async def dashboard_sales(
    request: Request,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db),
):
    is_organizer = await DashboardService.user_has_permission(
        current_user.user_id, "organizer", db
    )
    is_admin = await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    )

    if not is_organizer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view sales",
        )

    sales_data = await DashboardService.get_sales_data(current_user.user_id, db)

    context = {
        "request": request,
        "user": current_user,
        "tab": "sales",
        "is_admin": is_admin,
        "is_organizer": is_organizer,
        "sales_data": sales_data,
    }

    return templates.TemplateResponse("dashboard/sales.jinja", context)


@router.get("/moderation", response_class=HTMLResponse)
async def dashboard_moderation(
    request: Request,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db),
):
    is_admin = await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    )
    is_organizer = await DashboardService.user_has_permission(
        current_user.user_id, "organizer", db
    )

    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view moderation",
        )

    users = await DashboardService.get_all_users(db)

    context = {
        "request": request,
        "user": current_user,
        "tab": "moderation",
        "is_admin": is_admin,
        "is_organizer": is_organizer,
        "users": users,
    }

    return templates.TemplateResponse("dashboard/moderation.jinja", context)


@router.get("/posts", response_class=HTMLResponse)
async def dashboard_posts(
    request: Request,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db),
):
    is_admin = await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    )
    is_organizer = await DashboardService.user_has_permission(
        current_user.user_id, "organizer", db
    )

    if not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to view posts",
        )

    events = await DashboardService.get_unapproved_events(db)

    context = {
        "request": request,
        "user": current_user,
        "tab": "posts",
        "is_admin": is_admin,
        "is_organizer": is_organizer,
        "events": events,
    }

    return templates.TemplateResponse("dashboard/posts.jinja", context)


@router.post(
    "/moderation", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND
)
async def moderation_actions(
    request: Request,
    action: str = Form(...),
    user_id: int = Form(None),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform moderation actions",
        )

    success = False
    if action == "promote":
        success = await ModerationService.promote_user(user_id, db)
    elif action == "demote":
        success = await ModerationService.demote_user(user_id, db)
    elif action == "delete_user":
        success = await ModerationService.delete_user(user_id, db)

    return RedirectResponse(
        url="/dashboard/moderation",
        status_code=status.HTTP_302_FOUND,
    )


@router.post(
    "/posts", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND
)
async def post_actions(
    request: Request,
    action: str = Form(...),
    event_id: int = Form(None),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not await DashboardService.user_has_permission(
        current_user.user_id, "admin", db
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform post actions",
        )

    success = False
    if action == "approve_event":
        success = await ModerationService.approve_event(event_id, db)
    elif action == "reject_event":
        success = await ModerationService.reject_event(event_id, db)

    return RedirectResponse(
        url="/dashboard/posts",
        status_code=status.HTTP_302_FOUND,
    )
