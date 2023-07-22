from sqlalchemy.orm import Session
from models import User, Party, Ticket, Organizer, Attraction, Payment, Review

class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def save(db: Session, user: User) -> User:
        if user.user_id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def find_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.user_id == user_id).first()

    @staticmethod
    def exists_by_id(db: Session, user_id: int) -> bool:
        return db.query(User).filter(User.user_id == user_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, user_id: int) -> None:
        user = db.query(User).filter(User.user_id == user_id).first()
        if user is not None:
            db.delete(user)
            db.commit()

class PartyRepository:
    @staticmethod
    def find_all(db: Session) -> list[Party]:
        return db.query(Party).all()

    @staticmethod
    def save(db: Session, party: Party) -> Party:
        if party.party_id:
            db.merge(party)
        else:
            db.add(party)
        db.commit()
        db.refresh(party)
        return party

    @staticmethod
    def find_by_id(db: Session, party_id: int) -> Party:
        return db.query(Party).filter(Party.party_id == party_id).first()

    @staticmethod
    def exists_by_id(db: Session, party_id: int) -> bool:
        return db.query(Party).filter(Party.party_id == party_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, party_id: int) -> None:
        party = db.query(Party).filter(Party.party_id == party_id).first()
        if party is not None:
            db.delete(party)
            db.commit()

class TicketRepository:
    @staticmethod
    def find_all(db: Session) -> list[Ticket]:
        return db.query(Ticket).all()

    @staticmethod
    def save(db: Session, ticket: Ticket) -> Ticket:
        if ticket.ticket_id:
            db.merge(ticket)
        else:
            db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    @staticmethod
    def find_by_id(db: Session, ticket_id: int) -> Ticket:
        return db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

    @staticmethod
    def exists_by_id(db: Session, ticket_id: int) -> bool:
        return db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, ticket_id: int) -> None:
        ticket = db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        if ticket:
            db.delete(ticket)
            db.commit()

class OrganizerRepository:
    @staticmethod
    def find_all(db: Session) -> list[Organizer]:
        return db.query(Organizer).all()

    @staticmethod
    def save(db: Session, organizer: Organizer) -> Organizer:
        if organizer.organizer_id:
            db.merge(organizer)
        else:
            db.add(organizer)
        db.commit()
        db.refresh(organizer)
        return organizer

    @staticmethod
    def find_by_id(db: Session, organizer_id: int) -> Organizer:
        return db.query(Organizer).filter(Organizer.organizer_id == organizer_id).first()

    @staticmethod
    def exists_by_id(db: Session, organizer_id: int) -> bool:
        return db.query(Organizer).filter(Organizer.organizer_id == organizer_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, organizer_id: int) -> None:
        organizer = db.query(Organizer).filter(Organizer.organizer_id == organizer_id).first()
        if organizer:
            db.delete(organizer)
            db.commit()

class AttractionRepository:
    @staticmethod
    def find_all(db: Session) -> list[Attraction]:
        return db.query(Attraction).all()

    @staticmethod
    def save(db: Session, attraction: Attraction) -> Attraction:
        if attraction.attraction_id:
            db.merge(attraction)
        else:
            db.add(attraction)
        db.commit()
        db.refresh(attraction)
        return attraction

    @staticmethod
    def find_by_id(db: Session, attraction_id: int) -> Attraction:
        return db.query(Attraction).filter(Attraction.attraction_id == attraction_id).first()

    @staticmethod
    def exists_by_id(db: Session, attraction_id: int) -> bool:
        return db.query(Attraction).filter(Attraction.attraction_id == attraction_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, attraction_id: int) -> None:
        attraction = db.query(Attraction).filter(Attraction.attraction_id == attraction_id).first()
        if attraction:
            db.delete(attraction)
            db.commit()

class ReviewRepository:
    @staticmethod
    def find_all(db: Session) -> list[Review]:
        return db.query(Review).all()

    @staticmethod
    def save(db: Session, review: Review) -> Review:
        if review.review_id:
            db.merge(review)
        else:
            db.add(review)
        db.commit()
        db.refresh(review)
        return review

    @staticmethod
    def find_by_id(db: Session, review_id: int) -> Review:
        return db.query(Review).filter(Review.review_id == review_id).first()

    @staticmethod
    def exists_by_id(db: Session, review_id: int) -> bool:
        return db.query(Review).filter(Review.review_id == review_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, review_id: int) -> None:
        review = db.query(Review).filter(Review.review_id == review_id).first()
        if review:
            db.delete(review)
            db.commit()


class PaymentRepository:
    @staticmethod
    def find_all(db: Session) -> list[Payment]:
        return db.query(Payment).all()

    @staticmethod
    def save(db: Session, payment: Payment) -> Payment:
        if payment.payment_id:
            db.merge(payment)
        else:
            db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    @staticmethod
    def find_by_id(db: Session, payment_id: int) -> Payment:
        return db.query(Payment).filter(Payment.payment_id == payment_id).first()

    @staticmethod
    def exists_by_id(db: Session, payment_id: int) -> bool:
        return db.query(Payment).filter(Payment.payment_id == payment_id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, payment_id: int) -> None:
        payment = db.query(Payment).filter(Payment.payment_id == payment_id).first()
        if payment:
            db.delete(payment)
            db.commit()
