import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from config import TOKEN_API

from app.handlers import router #Импорт внешнего роутера
from app.database.models import async_main

bot = Bot(token=TOKEN_API)
dp = Dispatcher()



#Старт поллинга. Включение внешнего роутера. Запуск БД
async def main():
    await async_main()
    print("Бот запущен")
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот отключен")