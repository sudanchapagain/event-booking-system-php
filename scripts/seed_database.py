import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models import EventCategory, User
from app.core.security import Hash


async def create_sample_data():
    async with AsyncSessionLocal() as db:
        existing_categories = (await db.execute(select(EventCategory))).all()
        if not existing_categories:
            categories = [
                EventCategory(name="Music"),
                EventCategory(name="Sports"),
                EventCategory(name="Business"),
                EventCategory(name="Entertainment"),
                EventCategory(name="Arts & Culture"),
                EventCategory(name="Community & Social"),
                EventCategory(name="Education & Training"),
                EventCategory(name="Science & Technology"),
            ]

            for category in categories:
                db.add(category)

            await db.commit()
            print("Sample categories created!")

        admin_user = (
            await db.execute(select(User).where(User.email == "admin@chautari.com"))
        ).scalar_one_or_none()
        if not admin_user:
            admin = User(
                username="admin",
                email="admin@chautari.com",
                password_hash=Hash.bcrypt("admin123"),
                is_admin=True,
                is_organizer=True,
            )
            db.add(admin)
            await db.commit()
            print("Admin user created! Email: admin@chautari.com, Password: admin123")

        print("Sample data setup completed!")


if __name__ == "__main__":
    asyncio.run(create_sample_data())
