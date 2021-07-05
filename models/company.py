from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    tax_info_id = Column(String, ForeignKey('tax_info.id'))
    name = Column(String)
    tax_info = relationship('tax_info')

    def __repr__(self):
        return f'(ID:{self.id}),(Company name:{self.name})'
