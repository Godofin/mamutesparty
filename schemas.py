from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    type: str

class UserPatch(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    type: Optional[str]

class UserRequest(UserBase):
    pass

class UserResponse(UserBase):
    user_id: int

    class Config:
        orm_mode = True


class PartyBase(BaseModel):
    title: str
    description: str
    date: datetime
    time: datetime
    location: str
    price: float
    available_tickets: int
    organizer_id: int

class PartyCreate(PartyBase):
    pass

class PartyUpdate(PartyBase):
    title: Optional[str]
    description: Optional[str]
    date: Optional[datetime]
    time: Optional[datetime]
    location: Optional[str]
    price: Optional[float]
    available_tickets: Optional[int]
    organizer_id: Optional[int]

class PartyInDB(PartyBase):
    party_id: int

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    user_id: int
    party_id: int
    quantity: int
    purchase_date: str

class TicketPatch(BaseModel):
    user_id: Optional[int]
    party_id: Optional[int]
    quantity: Optional[int]
    purchase_date: Optional[str]

class TicketRequest(TicketBase):
    pass

class TicketResponse(TicketBase):
    ticket_id: int

    class Config:
        orm_mode = True

class OrganizerBase(BaseModel):
    name: str
    contact: str
    role: str
    user_id: int

class OrganizerPatch(BaseModel):
    name: Optional[str]
    contact: Optional[str]
    role: Optional[str]
    user_id: Optional[int]

class OrganizerRequest(OrganizerBase):
    pass

class OrganizerResponse(OrganizerBase):
    organizer_id: int

    class Config:
        orm_mode = True

class AttractionBase(BaseModel):
    name: str
    description: str
    party_id: int

class AttractionPatch(BaseModel):
    name: Optional[str]
    description: Optional[str]
    party_id: Optional[int]

class AttractionRequest(AttractionBase):
    pass

class AttractionResponse(AttractionBase):
    attraction_id: int

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    user_id: int
    party_id: int
    rating: float
    comment: str
    date: str

class ReviewPatch(BaseModel):
    user_id: Optional[int]
    party_id: Optional[int]
    rating: Optional[float]
    comment: Optional[str]
    date: Optional[str]

class ReviewRequest(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    review_id: int

    class Config:
        orm_mode = True

class PaymentBase(BaseModel):
    user_id: int
    party_id: int
    amount: float
    date: str
    status: str

class PaymentPatch(BaseModel):
    user_id: Optional[int]
    party_id: Optional[int]
    amount: Optional[float]
    date: Optional[str]
    status: Optional[str]

class PaymentRequest(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    payment_id: int

    class Config:
        orm_mode = True
