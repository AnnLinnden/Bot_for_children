from pathlib import Path
from importlib import import_module
from aiogram import Router

handlers_path = Path(__file__).parent
handlers_files = handlers_path.glob('*_handler.py')

# собираем все роутеры в один список, чтобы потом импортировать их в main.py
all_routers = []
for handler_file in handlers_files:
    module_name = f'handlers.{handler_file.stem}'
    module = import_module(module_name)

    for attribute_name in dir(module):
        if attribute_name.endswith("_router"):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, Router):  # Проверяем, что это роутер
                all_routers.append(attribute)
                break

