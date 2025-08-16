from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException, status
from .. import models


class ModerationService:

    @staticmethod
    async def promote_user(user_id: int, db: Session) -> bool:
        user_to_promote = (
            await db.execute(select(models.User).filter(models.User.user_id == user_id))
        ).scalar_one_or_none()

        if user_to_promote:
            user_to_promote.is_admin = True
            await db.commit()
            await db.refresh(user_to_promote)
            return True
        return False

    @staticmethod
    async def demote_user(user_id: int, db: Session) -> bool:
        user_to_demote = (
            await db.execute(select(models.User).filter(models.User.user_id == user_id))
        ).scalar_one_or_none()

        if user_to_demote:
            user_to_demote.is_admin = False
            await db.commit()
            await db.refresh(user_to_demote)
            return True
        return False

    @staticmethod
    async def delete_user(user_id: int, db: Session) -> bool:
        user_to_delete = (
            await db.execute(select(models.User).filter(models.User.user_id == user_id))
        ).scalar_one_or_none()

        if user_to_delete:
            await db.delete(user_to_delete)
            await db.commit()
            return True
        return False

    @staticmethod
    async def approve_event(event_id: int, db: Session) -> bool:
        event_to_approve = (
            await db.execute(
                select(models.Event).filter(models.Event.event_id == event_id)
            )
        ).scalar_one_or_none()

        if event_to_approve:
            event_to_approve.is_approved = True

            organizer = (
                await db.execute(
                    select(models.User).filter(
                        models.User.user_id == event_to_approve.organizer_id
                    )
                )
            ).scalar_one_or_none()

            if organizer and not organizer.is_organizer:
                organizer.is_organizer = True
                await db.commit()
                await db.refresh(organizer)

            await db.commit()
            await db.refresh(event_to_approve)
            return True
        return False

    @staticmethod
    async def reject_event(event_id: int, db: Session) -> bool:
        event_to_reject = (
            await db.execute(
                select(models.Event).filter(models.Event.event_id == event_id)
            )
        ).scalar_one_or_none()

        if event_to_reject:
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
                models.EventDate.__table__.delete().where(
                    models.EventDate.event_id == event_id
                )
            )
            await db.execute(
                models.EventCategoryMapping.__table__.delete().where(
                    models.EventCategoryMapping.event_id == event_id
                )
            )
            await db.delete(event_to_reject)
            await db.commit()
            return True
        return False
