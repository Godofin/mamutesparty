# routers.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, Party, Ticket, Organizer, Attraction, Review, Payment
from repositories import UserRepository, PartyRepository, TicketRepository, OrganizerRepository, AttractionRepository, ReviewRepository, PaymentRepository
from schemas import UserBase, UserPatch, UserRequest, UserResponse, PartyBase, PartyCreate, PartyUpdate, PartyInDB, TicketBase, TicketPatch, TicketRequest, TicketResponse, OrganizerBase, OrganizerPatch, OrganizerRequest, OrganizerResponse, AttractionBase, AttractionPatch, AttractionRequest, AttractionResponse, ReviewBase, ReviewPatch, ReviewRequest, ReviewResponse, PaymentBase, PaymentPatch, PaymentRequest, PaymentResponse

router = APIRouter()

# Users Route Start
@router.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user_req: UserRequest, db: Session = Depends(get_db)):
    user = User(**user_req.dict())
    user_repo = UserRepository()
    return user_repo.save(db, user)

@router.get("/users/", response_model=List[UserResponse], tags=["Users"])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    users = user_repo.find_all(db)
    return users[skip : skip + limit]

@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    user = user_repo.find_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(user_id: int, user_req: UserRequest, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    user = user_repo.find_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key, value in user_req.dict().items():
        setattr(user, key, value)
    return user_repo.save(db, user)

@router.patch("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def patch_user(user_id: int, user_req: UserPatch, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    user = user_repo.find_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key, value in user_req.dict(exclude_unset=True).items():
        setattr(user, key, value)
    return user_repo.save(db, user)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository()
    if not user_repo.exists_by_id(db, user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user_repo.delete_by_id(db, user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Users Route End

# Party Route Start
@router.post("/parties/", response_model=PartyInDB, status_code=status.HTTP_201_CREATED, tags=["Parties"])
def create_party(party: PartyCreate, db: Session = Depends(get_db)):
    new_party = Party(**party.dict())
    db.add(new_party)
    db.commit()
    db.refresh(new_party)
    return new_party

@router.get("/parties/", response_model=List[PartyInDB], tags=["Parties"])
def read_parties(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    party_repo = PartyRepository()
    parties = party_repo.find_all(db)
    return parties[skip : skip + limit]


@router.get("/parties/{party_id}", response_model=PartyInDB, tags=["Parties"])
def read_party(party_id: int, db: Session = Depends(get_db)):
    party = db.query(Party).filter(Party.party_id == party_id).first()
    if party is None:
        raise HTTPException(status_code=404, detail="Party not found")
    return party

@router.put("/parties/{party_id}", response_model=PartyInDB, tags=["Parties"])
def update_party(party_id: int, party: PartyUpdate, db: Session = Depends(get_db)):
    updated_party = db.query(Party).filter(Party.party_id == party_id).first()
    if updated_party is None:
        raise HTTPException(status_code=404, detail="Party not found")
    
    for key, value in party.dict(exclude_unset=True).items():
        setattr(updated_party, key, value)
    
    db.commit()
    db.refresh(updated_party)
    return updated_party

@router.patch("/parties/{party_id}", response_model=PartyInDB, tags=["Parties"])
def patch_party(party_id: int, party: PartyUpdate, db: Session = Depends(get_db)):
    existing_party = db.query(Party).filter(Party.party_id == party_id).first()
    if existing_party is None:
        raise HTTPException(status_code=404, detail="Party not found")
    
    for key, value in party.dict(exclude_unset=True).items():
        setattr(existing_party, key, value)
    
    db.commit()
    db.refresh(existing_party)
    return existing_party

@router.delete("/parties/{party_id}", response_model=PartyInDB, tags=["Parties"])
def delete_party(party_id: int, db: Session = Depends(get_db)):
    party = db.query(Party).filter(Party.party_id == party_id).first()
    if party is None:
        raise HTTPException(status_code=404, detail="Party not found")
    
    db.delete(party)
    db.commit()
    return party
# Party Route End

# Ticket Route Start
@router.post("/tickets/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED, tags=["Tickets"])
def create_ticket(ticket_req: TicketRequest, db: Session = Depends(get_db)):
    ticket = Ticket(**ticket_req.dict())
    ticket_repo = TicketRepository()
    return ticket_repo.save(db, ticket)

@router.get("/tickets/", response_model=List[TicketResponse], tags=["Tickets"])
def read_tickets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ticket_repo = TicketRepository()
    tickets = ticket_repo.find_all(db)
    return tickets[skip : skip + limit]

@router.get("/tickets/{ticket_id}", response_model=TicketResponse, tags=["Tickets"])
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket_repo = TicketRepository()
    ticket = ticket_repo.find_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket

@router.put("/tickets/{ticket_id}", response_model=TicketResponse, tags=["Tickets"])
def update_ticket(ticket_id: int, ticket_req: TicketRequest, db: Session = Depends(get_db)):
    ticket_repo = TicketRepository()
    ticket = ticket_repo.find_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    for key, value in ticket_req.dict().items():
        setattr(ticket, key, value)
    return ticket_repo.save(db, ticket)

@router.patch("/tickets/{ticket_id}", response_model=TicketResponse, tags=["Tickets"])
def patch_ticket(ticket_id: int, ticket_req: TicketPatch, db: Session = Depends(get_db)):
    ticket_repo = TicketRepository()
    ticket = ticket_repo.find_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    for key, value in ticket_req.dict(exclude_unset=True).items():
        setattr(ticket, key, value)
    return ticket_repo.save(db, ticket)

@router.delete("/tickets/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tickets"])
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket_repo = TicketRepository()
    if not ticket_repo.exists_by_id(db, ticket_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    ticket_repo.delete_by_id(db, ticket_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Ticket Route End

# Organizer Route Start
@router.post("/organizers/", response_model=OrganizerResponse, status_code=status.HTTP_201_CREATED, tags=["Organizers"])
def create_organizer(organizer_req: OrganizerRequest, db: Session = Depends(get_db)):
    organizer = Organizer(**organizer_req.dict())
    organizer_repo = OrganizerRepository()
    return organizer_repo.save(db, organizer)

@router.get("/organizers/", response_model=List[OrganizerResponse], tags=["Organizers"])
def read_organizers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    organizer_repo = OrganizerRepository()
    organizers = organizer_repo.find_all(db)
    return organizers[skip : skip + limit]

@router.get("/organizers/{organizer_id}", response_model=OrganizerResponse, tags=["Organizers"])
def read_organizer(organizer_id: int, db: Session = Depends(get_db)):
    organizer_repo = OrganizerRepository()
    organizer = organizer_repo.find_by_id(db, organizer_id)
    if not organizer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizer not found")
    return organizer

@router.put("/organizers/{organizer_id}", response_model=OrganizerResponse, tags=["Organizers"])
def update_organizer(organizer_id: int, organizer_req: OrganizerRequest, db: Session = Depends(get_db)):
    organizer_repo = OrganizerRepository()
    organizer = organizer_repo.find_by_id(db, organizer_id)
    if not organizer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizer not found")
    for key, value in organizer_req.dict().items():
        setattr(organizer, key, value)
    return organizer_repo.save(db, organizer)

@router.patch("/organizers/{organizer_id}", response_model=OrganizerResponse, tags=["Organizers"])
def patch_organizer(organizer_id: int, organizer_req: OrganizerPatch, db: Session = Depends(get_db)):
    organizer_repo = OrganizerRepository()
    organizer = organizer_repo.find_by_id(db, organizer_id)
    if not organizer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizer not found")
    for key, value in organizer_req.dict(exclude_unset=True).items():
        setattr(organizer, key, value)
    return organizer_repo.save(db, organizer)

@router.delete("/organizers/{organizer_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Organizers"])
def delete_organizer(organizer_id: int, db: Session = Depends(get_db)):
    organizer_repo = OrganizerRepository()
    if not organizer_repo.exists_by_id(db, organizer_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Organizer not found")
    organizer_repo.delete_by_id(db, organizer_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Organizer Route End
# Attraction Route Start
@router.post("/attractions/", response_model=AttractionResponse, status_code=status.HTTP_201_CREATED, tags=["Attractions"])
def create_attraction(attraction_req: AttractionRequest, db: Session = Depends(get_db)):
    attraction = Attraction(**attraction_req.dict())
    attraction_repo = AttractionRepository()
    return attraction_repo.save(db, attraction)

@router.get("/attractions/", response_model=List[AttractionResponse], tags=["Attractions"])
def read_attractions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    attraction_repo = AttractionRepository()
    attractions = attraction_repo.find_all(db)
    return attractions[skip : skip + limit]

@router.get("/attractions/{attraction_id}", response_model=AttractionResponse, tags=["Attractions"])
def read_attraction(attraction_id: int, db: Session = Depends(get_db)):
    attraction_repo = AttractionRepository()
    attraction = attraction_repo.find_by_id(db, attraction_id)
    if not attraction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attraction not found")
    return attraction

@router.put("/attractions/{attraction_id}", response_model=AttractionResponse, tags=["Attractions"])
def update_attraction(attraction_id: int, attraction_req: AttractionRequest, db: Session = Depends(get_db)):
    attraction_repo = AttractionRepository()
    attraction = attraction_repo.find_by_id(db, attraction_id)
    if not attraction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attraction not found")
    for key, value in attraction_req.dict().items():
        setattr(attraction, key, value)
    return attraction_repo.save(db, attraction)

@router.patch("/attractions/{attraction_id}", response_model=AttractionResponse, tags=["Attractions"])
def patch_attraction(attraction_id: int, attraction_req: AttractionPatch, db: Session = Depends(get_db)):
    attraction_repo = AttractionRepository()
    attraction = attraction_repo.find_by_id(db, attraction_id)
    if not attraction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attraction not found")
    for key, value in attraction_req.dict(exclude_unset=True).items():
        setattr(attraction, key, value)
    return attraction_repo.save(db, attraction)

@router.delete("/attractions/{attraction_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Attractions"])
def delete_attraction(attraction_id: int, db: Session = Depends(get_db)):
    attraction_repo = AttractionRepository()
    if not attraction_repo.exists_by_id(db, attraction_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attraction not found")
    attraction_repo.delete_by_id(db, attraction_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Attraction Route End
# Review Route Start
@router.post("/reviews/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED, tags=["Reviews"])
def create_review(review_req: ReviewRequest, db: Session = Depends(get_db)):
    review = Review(**review_req.dict())
    review_repo = ReviewRepository()
    return review_repo.save(db, review)

@router.get("/reviews/", response_model=List[ReviewResponse], tags=["Reviews"])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    review_repo = ReviewRepository()
    reviews = review_repo.find_all(db)
    return reviews[skip : skip + limit]

@router.get("/reviews/{review_id}", response_model=ReviewResponse, tags=["Reviews"])
def read_review(review_id: int, db: Session = Depends(get_db)):
    review_repo = ReviewRepository()
    review = review_repo.find_by_id(db, review_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    return review

@router.put("/reviews/{review_id}", response_model=ReviewResponse, tags=["Reviews"])
def update_review(review_id: int, review_req: ReviewRequest, db: Session = Depends(get_db)):
    review_repo = ReviewRepository()
    review = review_repo.find_by_id(db, review_id)
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    for key, value in review_req.dict().items():
        setattr(review, key, value)
    return review_repo.save(db, review)

@router.delete("/reviews/{review_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Reviews"])
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review_repo = ReviewRepository()
    if not review_repo.exists_by_id(db, review_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
    review_repo.delete_by_id(db, review_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Review Route End

# Payment Route Start
@router.post("/payments/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED, tags=["Payments"])
def create_payment(payment_req: PaymentRequest, db: Session = Depends(get_db)):
    payment = Payment(**payment_req.dict())
    payment_repo = PaymentRepository()
    return payment_repo.save(db, payment)

@router.get("/payments/", response_model=List[PaymentResponse], tags=["Payments"])
def read_payments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    payment_repo = PaymentRepository()
    payments = payment_repo.find_all(db)
    return payments[skip : skip + limit]

@router.get("/payments/{payment_id}", response_model=PaymentResponse, tags=["Payments"])
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment_repo = PaymentRepository()
    payment = payment_repo.find_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return payment

@router.put("/payments/{payment_id}", response_model=PaymentResponse, tags=["Payments"])
def update_payment(payment_id: int, payment_req: PaymentRequest, db: Session = Depends(get_db)):
    payment_repo = PaymentRepository()
    payment = payment_repo.find_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    for key, value in payment_req.dict().items():
        setattr(payment, key, value)
    return payment_repo.save(db, payment)

@router.delete("/payments/{payment_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Payments"])
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment_repo = PaymentRepository()
    if not payment_repo.exists_by_id(db, payment_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    payment_repo.delete_by_id(db, payment_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# Payment Route End

