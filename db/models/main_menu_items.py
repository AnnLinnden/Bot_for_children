from sqlalchemy import Column, Integer, String, Identity
from ..base import Base


class MenuItem(Base):
    __tablename__ = "main_menu_items"

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    command = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    response = Column(String, nullable=False)
