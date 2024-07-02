from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select

async def set_user(tg_id, tg_name, tg_first_name): #Функция регистрации пользователя при первом запуске
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, tg_name=tg_name, tg_first_name=tg_first_name))
            await session.commit()


async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))