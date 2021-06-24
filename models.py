import datetime

from sqlalchemy            import Column, Integer, String, ForeignKey, DateTime, Numeric, Boolean
from sqlalchemy.orm        import relationship
from sqlalchemy.sql.schema import ForeignKey

from database              import Base


class BaseMixin():
    id         = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class Position(Base, BaseMixin):
    __tablename__    = 'positions'
    component_number = Column(Integer)
    section_number   = Column(Integer)
    description      = Column(String(length=200), nullable=True)
    name             = Column(String(length=50), nullable=True)
    korean_texts     = relationship('KoreanText', backref='positions')
    english_texts    = relationship('EnglishText', backref='positions')
    images           = relationship('Image', back_populates='positions')

class KoreanText(Base, BaseMixin):
    __tablename__ = 'korean_texts'
    position_id   = Column(Integer, ForeignKey('positions.id'))
    text          = Column(String(1000))

class EnglishText(Base, BaseMixin):
    __tablename__ = 'english_texts'
    position_id   = Column(Integer, ForeignKey('positions.id'))
    text          = Column(String(1000))

class Image(Base, BaseMixin):
    __tablename__ = 'images'
    directory     = Column(String(1000))
    position_id   = Column(Integer, ForeignKey('positions.id'))
    positions     = relationship('Position', back_populates='images')

class User(Base, BaseMixin):
    __tablename__ = 'users'
    email         = Column(String(length=300))
    password      = Column(String(2000))
    is_active     = Column(Boolean)

class Membership(Base, BaseMixin):
    __tablename__ = 'memberships'
    name          = Column(String(50))
    price         = Column(Numeric(12, 3))

class Status(Base, BaseMixin):
    __tablename__ = 'status'
    name          = Column(String(50))

class Member(Base, BaseMixin):
    __tablename__ = 'members'
    user_id       = Column(Integer, ForeignKey('users.id'))
    membership_id = Column(Integer, ForeignKey('memberships.id'))
    status_id     = Column(Integer, ForeignKey('status.id'))
    company       = Column(String(50))
    phone         = Column(String(50))

class History(Base, BaseMixin):
    __tablename__ = 'histories'
    member_id     = Column(Integer, ForeignKey('members.id'))
    status_id     = Column(Integer, ForeignKey('status.id'))
