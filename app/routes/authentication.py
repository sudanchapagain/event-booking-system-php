from fastapi import APIRouter, Depends, status, HTTPException, Form, Response, Request
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from sqlalchemy.exc import IntegrityError
from fastapi.templating import Jinja2Templates

from .. import schemas, models
from ..core import database, security, auth
from ..core.dependencies import get_current_user

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(tags=["Authentication"])


@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db),
):
    user = (
        await db.execute(select(models.User).filter(models.User.email == username))
    ).scalar_one_or_none()
    if not user:
        return templates.TemplateResponse(
            "login.jinja",
            {"request": request, "message": "Invalid credentials"},
            status_code=400,
        )
    if not security.Hash.verify(user.password_hash, password):
        return templates.TemplateResponse(
            "login.jinja",
            {"request": request, "message": "Invalid credentials"},
            status_code=400,
        )

    access_token = auth.create_access_token(data={"sub": user.email})
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=access_token, httponly=True)
    return response


@router.post("/signup")
async def signup(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(database.get_db),
):
    errors = []

    existing_user = (
        await db.execute(select(models.User).filter(models.User.email == email))
    ).scalar_one_or_none()

    if existing_user:
        errors.append("Email is already registered")

    if len(username) < 3:
        errors.append("Username must be at least 3 characters long")

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if errors:
        return templates.TemplateResponse(
            "signup.jinja", {"request": request, "errors": errors}, status_code=400
        )

    try:
        hashed_password = security.Hash.bcrypt(password)
        new_user = models.User(
            username=username, email=email, password_hash=hashed_password
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        response = RedirectResponse(
            url="/login?success=signup", status_code=status.HTTP_302_FOUND
        )
        return response

    except IntegrityError:
        await db.rollback()
        errors.append("Email is already registered")
        return templates.TemplateResponse(
            "signup.jinja", {"request": request, "errors": errors}, status_code=400
        )


@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="access_token")
    return response


@router.post("/settings")
async def update_settings(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    user_phone: str = Form(None),
    password: str = Form(None),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    errors = []

    if len(username) < 3:
        errors.append("Username must be at least 3 characters long")

    existing_user = (
        await db.execute(
            select(models.User).where(
                and_(
                    models.User.username == username,
                    models.User.user_id != current_user.user_id,
                )
            )
        )
    ).scalar_one_or_none()

    if existing_user:
        errors.append("Username is already taken")

    existing_email = (
        await db.execute(
            select(models.User).where(
                and_(
                    models.User.email == email,
                    models.User.user_id != current_user.user_id,
                )
            )
        )
    ).scalar_one_or_none()

    if existing_email:
        errors.append("Email is already taken")

    if errors:
        return templates.TemplateResponse(
            "settings.jinja",
            {"request": request, "user": current_user, "errors": errors},
        )

    current_user.username = username
    current_user.email = email
    if user_phone:
        current_user.user_phone = user_phone

    if password and len(password) >= 8:
        current_user.password_hash = hashing.Hash.bcrypt(password)

    await db.commit()

    return templates.TemplateResponse(
        "settings.jinja",
        {"request": request, "user": current_user, "update_success": True},
    )
