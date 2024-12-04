from sqlalchemy import Column, Integer, String
from ..base import Base


class MenuItem(Base):
    __tablename__ = "main_menu_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    command = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    response = Column(String, nullable=False)
