from sqlalchemy.orm import Session
from sqlalchemy import select, func, case
from typing import List, Dict, Any, Optional
from .. import models


class DashboardService:

    @staticmethod
    async def user_has_permission(user_id: int, permission: str, db: Session) -> bool:
        if permission == "admin":
            user = (
                await db.execute(
                    select(models.User.is_admin).filter(models.User.user_id == user_id)
                )
            ).scalar_one_or_none()
            return user is True
        elif permission == "organizer":
            user = (
                await db.execute(
                    select(models.User.is_organizer).filter(
                        models.User.user_id == user_id
                    )
                )
            ).scalar_one_or_none()
            return user is True
        return False

    @staticmethod
    async def get_user_bookings(user_id: int, db: Session) -> List[Dict[str, Any]]:
        bookings_query = (
            select(
                models.Event.event_id,
                models.Event.title.label("event_title"),
                models.Event.ticket_price,
                models.User.user_id,
                models.User.username,
                models.User.email,
                models.User.user_phone,
                models.UserEventAttendance.status,
            )
            .join(
                models.UserEventAttendance,
                models.Event.event_id == models.UserEventAttendance.event_id,
            )
            .join(
                models.User, models.UserEventAttendance.user_id == models.User.user_id
            )
            .filter(models.Event.organizer_id == user_id)
            .order_by(models.Event.event_id, models.User.username)
        )

        bookings_result = (await db.execute(bookings_query)).all()
        events_with_bookings = {}

        for row in bookings_result:
            event_id = row.event_id
            if event_id not in events_with_bookings:
                events_with_bookings[event_id] = {
                    "title": row.event_title,
                    "ticket_price": row.ticket_price,
                    "attendees": [],
                }
            events_with_bookings[event_id]["attendees"].append(
                {
                    "username": row.username,
                    "email": row.email,
                    "user_phone": row.user_phone,
                    "status": row.status,
                }
            )

        return list(events_with_bookings.values())

    @staticmethod
    async def get_sales_data(user_id: int, db: Session) -> List[Dict[str, Any]]:
        sales_query = (
            select(
                models.Event.event_id,
                models.Event.title.label("event_title"),
                models.Event.ticket_price,
                models.func.count(models.UserEventAttendance.user_id).label(
                    "attendee_count"
                ),
                models.func.sum(
                    models.case(
                        (
                            models.UserEventAttendance.status == "confirmed",
                            models.Event.ticket_price,
                        ),
                        else_=0,
                    )
                ).label("total_revenue"),
            )
            .outerjoin(
                models.UserEventAttendance,
                models.Event.event_id == models.UserEventAttendance.event_id,
            )
            .filter(models.Event.organizer_id == user_id)
            .group_by(models.Event.event_id)
            .order_by(models.Event.event_id)
        )

        return (await db.execute(sales_query)).all()

    @staticmethod
    async def get_all_users(db: Session) -> List[Dict[str, Any]]:
        users_query = select(
            models.User.user_id,
            models.User.username,
            models.User.email,
            models.User.is_admin,
        ).filter(models.User.username != "deleted_user")

        return (await db.execute(users_query)).all()

    @staticmethod
    async def get_unapproved_events(db: Session) -> List[Dict[str, Any]]:
        events_query = select(
            models.Event.event_id,
            models.Event.title,
            models.Event.description,
            models.Event.location,
        ).filter(models.Event.is_approved == False)

        return (await db.execute(events_query)).all()
