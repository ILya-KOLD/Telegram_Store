
from aiogram.utils.keyboard import (ReplyKeyboardMarkup, KeyboardButton,
                                    InlineKeyboardMarkup, InlineKeyboardButton,
                                    ReplyKeyboardBuilder, InlineKeyboardBuilder
                                    )


from app.database.requests import get_categories, get_category_items

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
        builder.add(InlineKeyboardButton(text=f"{category.name}", callback_data=f"category_{category.id}"))
    builder.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
    return builder.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_items(category_id)
    builder = InlineKeyboardBuilder()

    for item in all_items:
        builder.add(InlineKeyboardButton(text=f"{item.name}", callback_data=f"item_{item.id}"))
    builder.add(InlineKeyboardButton(text="На главную", callback_data="to_main"))
    return builder.adjust(2).as_markup()


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер",
                                                           request_contact=True)]],
                                 resize_keyboard=True,
                                 one_time_keyboard=True) #Запросить номер



