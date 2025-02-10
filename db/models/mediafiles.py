from sqlalchemy import Column, Integer, String, Identity
from ..base import Base


class MediaFiles(Base):
    """Класс для таблицы с медиафайлами. Файлы подтягиваются не сами по себе, а только в составе цепочки сообщений
    и только после текстового сообщения, которое лежит в таблице qa_items. То есть сначала идет минимум одно
    текстовое сообщение и только потом файлы."""
    __tablename__ = "mediafiles"

    id = Column(Integer, Identity(start=1), primary_key=True, autoincrement=True)
    group_id = Column(String, nullable=False)  # не может быть пустым, поскольку файлы всегда включены в цепочку
    group_number = Column(Integer, nullable=False)  # порядковый номер сообщения в цепочке
    media_type = Column(String)
    file_id = Column(String, nullable=False)  # ссылка, по которой ТГ подтягивает файл из своей базы
