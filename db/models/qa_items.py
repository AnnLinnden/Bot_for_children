from sqlalchemy import Column, Integer, String, Identity
from ..base import Base


class QAItem(Base):
    __tablename__ = "qa_items"

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    category = Column(String)  # юридические вопросы, здоровье, образование и пр.
    callback_data = Column(String)  # по этому полю обработчик находит сообщение с нужной callback_data
    message = Column(String, nullable=False)  # само сообщение
    keyboard = Column(String)  # если нужно подтянуть к сообщению инлайн-клаву, она создается здесь в формате json
