from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Equipment(Base):
    __tablename__ = 'equipments'

    id = Column(Integer, primary_key=True)
    room_id = Column(String, ForeignKey('room.id'))
    room = relationship('room')

    def __repr__(self):
        return f'(Room ID:{self.id}), (Number: {self.equipment_title})'
