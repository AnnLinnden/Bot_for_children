from sqlalchemy import Column, Integer, String, Identity
from ..base import Base


class MediaFiles(Base):
    """Класс для таблицы с медиафайлами в БД. Файлы подтягиваются только в составе цепочки сообщений и только
    после текстового сообщения из таблицы qa_items."""
    __tablename__ = "mediafiles"

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    group_id = Column(String, nullable=False)  # не может быть пустым, поскольку файлы всегда включены в цепочку
    group_number = Column(Integer, nullable=False)  # порядковый номер сообщения в цепочке
    media_type = Column(String)
    file_id = Column(String, nullable=False)  # ссылка, по которой ТГ подтягивает файл из своей базы
    caption = Column(String)  # текстовое описание, которое публикуется вместе с файлом
