from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.database.requests as rq

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    number = State()

@router.message(Command("start"))
async def start_command(message: Message):
    await rq.set_user(message.from_user.id, message.from_user.username, message.from_user.first_name) #Регистрация пользователя при запуске
    await message.answer(text="Добро пожаловать в магазин.",
                         reply_markup=kb.main_keyboard)

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(text="Это кнопка помощи")

@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Выберите категорию товара",
                         reply_markup=await kb.categories())

@router.callback_query(F.data.startswith("category_"))
async def category(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.answer("Выберите товар по категории",
                                  reply_markup=await kb.items(callback.data.split("_")[1]))

@router.callback_query(F.data.startswith("item_"))
async def item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split("_")[1])
    await callback.answer("Вы выбрали товар")
    await callback.message.answer(f"Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите ваш возраст")


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Отправьте ваш номер телефона",
                         reply_markup=kb.get_number)


@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):

    await state.update_data(number=message.contact.phone_number) #Запись контакта в машину состояний
    data = await state.get_data() #Запись всех полученных данных в переменную словаря.

    await message.answer(f"Ваше имя: {data['name']}\n"
                         f"Ваш возраст: {data['age']}\n"
                         f"Номер: {data['number']}")
    await state.clear()





