import aiosqlite


class DatabaseManager:
    def __init__(self):
        self.path = 'db/database.db'

    async def initialize_database(self):
        pass
