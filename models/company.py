from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tax_info = relationship('tax_info')
    addres = relationship('building.addres')

