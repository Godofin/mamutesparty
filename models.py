from sqlalchemy import Column, Integer, String, Date, Time, Float
from database import Base

from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    type = Column(String)


class Party(Base):
    __tablename__ = "parties"

    party_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(Date)
    time = Column(Date)
    location = Column(String)
    price = Column(Float)
    available_tickets = Column(Integer)
    organizer_id = Column(Integer)


class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    party_id = Column(Integer)
    quantity = Column(Integer)
    purchase_date = Column(Date)


class Organizer(Base):
    __tablename__ = "organizers"

    organizer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)
    role = Column(String)
    user_id = Column(Integer)


class Attraction(Base):
    __tablename__ = "attractions"

    attraction_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    party_id = Column(Integer)


class Review(Base):
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    party_id = Column(Integer)
    rating = Column(Float)
    comment = Column(String)
    date = Column(Date)


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    party_id = Column(Integer)
    amount = Column(Float)
    date = Column(Date)
    status = Column(String)

