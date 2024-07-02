
from aiogram.utils.keyboard import (ReplyKeyboardMarkup, KeyboardButton,
                                    InlineKeyboardMarkup, InlineKeyboardButton,
                                    ReplyKeyboardBuilder, InlineKeyboardBuilder
                                    )


from app.database.requests import get_categories

#Клавиатура создается при команде Start
main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Каталог")],
                                              [KeyboardButton(text="Корзина")],
                                              [KeyboardButton(text="Контакты"),
                                               KeyboardButton(text="О нас")]],
                                    resize_keyboard=True,
                                    input_field_placeholder="Выберите пункт меню")


async def categories():
    all_categories = await get_categories()
    builder = InlineKeyboardBuilder()

    for category in all_categories:
        builder.add(InlineKeyboardButton(text=f"{category.name}", callback_data=f"{category.id}"))
    builder.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
    return builder.adjust(2).as_markup()


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер",
                                                           request_contact=True)]],
                                 resize_keyboard=True,
                                 one_time_keyboard=True) #Запросить номер

