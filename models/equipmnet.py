from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    room_id = Column(String, ForeignKey('room.id'))
    room = relationship('room')
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'equipment'
    }
