from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    DECIMAL,
    TEXT,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from .core.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(16), unique=True, nullable=False)
    user_phone = Column(String(10), unique=True)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_organizer = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    description = Column(TEXT)
    organizer_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    capacity = Column(Integer)
    ticket_price = Column(DECIMAL(10, 2), nullable=False)
    is_approved = Column(Boolean, default=False)

    organizer = relationship("User")


class EventCategory(Base):
    __tablename__ = "event_categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)


class EventCategoryMapping(Base):
    __tablename__ = "event_category_mapping"

    event_id = Column(
        Integer, ForeignKey("events.event_id", ondelete="CASCADE"), primary_key=True
    )
    category_id = Column(
        Integer,
        ForeignKey("event_categories.category_id", ondelete="CASCADE"),
        primary_key=True,
    )


class UserEventAttendance(Base):
    __tablename__ = "user_event_attendance"

    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="SET DEFAULT"), primary_key=True
    )
    event_id = Column(
        Integer, ForeignKey("events.event_id", ondelete="CASCADE"), primary_key=True
    )
    status = Column(String(20), default="confirmed")


class EventImage(Base):
    __tablename__ = "event_images"

    image_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id", ondelete="CASCADE"))
    image_url = Column(String(255), nullable=False)
    image_type = Column(String(20), nullable=False)


class EventDate(Base):
    __tablename__ = "event_dates"

    event_date_id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.event_id", ondelete="CASCADE"))
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)


class TicketSale(Base):
    __tablename__ = "ticket_sales"

    sale_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    event_id = Column(Integer, ForeignKey("events.event_id", ondelete="CASCADE"))
    quantity = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    sale_date = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
