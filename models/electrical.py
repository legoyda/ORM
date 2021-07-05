from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Electrical(Base):
    __tablename__ = 'electrical'

    id = Column(Integer, primary_key=True)
    power_config = Column(String)

    def __repr__(self):
        return f'(ID:{self.id}),(Power config:{self.power_config})'
