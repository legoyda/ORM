from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    size = Column(String)
    building = relationship('building')

    def __repr__(self):
        return f'(Room ID:{self.id}),(Room number:{self.number}),(Room size:{self.size}))'
