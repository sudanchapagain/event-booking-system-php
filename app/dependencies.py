from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy import select
from jose import JWTError, jwt

from . import models
from .core import database, auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)


async def get_current_user(
    request: Request,
    db: Session = Depends(database.get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_value = request.cookies.get("access_token")
    if not token_value:
        raise credentials_exception

    try:
        payload = jwt.decode(token_value, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = (
        await db.execute(select(models.User).filter(models.User.email == email))
    ).scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user


async def get_current_user_optional(
    request: Request,
    db: Session = Depends(database.get_db),
):
    try:
        token_value = request.cookies.get("access_token")
        if not token_value:
            return None

        payload = jwt.decode(token_value, auth.SECRET_KEY, algorithms=[auth.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None

        user = (
            await db.execute(select(models.User).filter(models.User.email == email))
        ).scalar_one_or_none()
        return user
    except:
        return None
