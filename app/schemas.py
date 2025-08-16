from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class EventBase(BaseModel):
    title: str
    location: str
    description: str | None = None
    capacity: int | None = None
    ticket_price: float
    is_approved: bool = False


class EventCreate(EventBase):
    pass


class Event(EventBase):
    event_id: int
    organizer_id: int | None = None
    organizer_name: str | None = None
    current_participants: int = 0

    class Config:
        from_attributes = True


class EventImage(BaseModel):
    image_id: int
    event_id: int
    image_url: str
    image_type: str

    class Config:
        from_attributes = True
