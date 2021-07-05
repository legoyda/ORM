from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Mechanical(Base):
    __tablename__ = 'mechanical'

    id = Column(Integer, primary_key=True)
    manufacture = Column(String)

    def __repr__(self):
        return f'(ID:{self.id}),(Manufacture:{self.manufacture})'
