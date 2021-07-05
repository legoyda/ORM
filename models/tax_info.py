from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base


class Tax_info(Base):
    __tablename__ = 'tax_info'

    id = Column(Integer, primary_key=True)
    name = Column(String, ForeignKey('company.id'))
    comercial_info = Column(String)
    company = Column('company')

    def __repr__(self):
        return f'(ID:{self.id}),(Comercial Info:{self.comercial_info})'
