from sqlalchemy import Column, Integer, String, Identity, JSON
from ..base import Base


class QAItem(Base):
    __tablename__ = "qa_items"

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)  # юридические вопросы, здоровье, образование и пр.
    callback_data = Column(String)  # нажата кнопка -> бот забирает callback_data, по ней ищет и отправляет сообщение.
    # Может быть пустой, т.к. есть цепочки сообщений, где лишь у первого есть callback_data
    message = Column(String, nullable=False)  # само сообщение
    group_id = Column(String)  # объединяющий ID, если нужна цепочка сообщений
    group_number = Column(Integer)  # номер сообщения в цепочке, объединенной group_id
    keyboard = Column(JSON)  # если нужно добавить к сообщению инлайн-клаву, она создается здесь в формате json.
    # Пример хранения в БД: {
#         [{"text": "Подробнее", "callback_data": "qa_law_2"}],
#         [{"text": "Главное меню", "callback_data": "menu_main"}]
# }
