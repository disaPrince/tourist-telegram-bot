from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery
from create_bot import dp
from domain import Tours
from database import db_connect
from keyboards import admin_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram_calendar import DialogCalendar, dialog_cal_callback


username = ['Adqwertyil', 'KingDias', 'JDam20']
tour = Tours.Tours


class Tour(StatesGroup):
    photo = State()
    name = State()
    description = State()
    rating = State()
    from_city = State()
    to_city = State()
    when_date = State()
    days = State()
    price = State()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin_menu, commands=['moderate'])
    dp.register_callback_query_handler(add_tour, text='addTour')
    dp.register_message_handler(load_photo, content_types=['photo'], state=Tour.photo)
    dp.register_message_handler(set_name, state=Tour.name)
    dp.register_message_handler(set_description, state=Tour.description)
    dp.register_message_handler(set_rating, state=Tour.rating)
    dp.register_message_handler(set_from_city, state=Tour.from_city)
    dp.register_message_handler(set_to_city, state=Tour.to_city)
    dp.register_message_handler(set_days, state=Tour.days)
    dp.register_message_handler(set_price, state=Tour.price)
    dp.register_callback_query_handler(get_tours, text='tourSettings')


async def admin_menu(message: types.Message):
    if message.from_user.username in username:
        await message.answer(message.from_user.first_name, reply_markup=admin_kb.admin_menu)
    else:
        await message.answer('Доступно только Админам')


async def add_tour(callback: types.CallbackQuery):
    if callback.from_user.username in username:
        await Tour.photo.set()
        await callback.message.answer("Загрузи фото:")


async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        global savingState
        savingState = state
        tour.photo = message.photo[0].file_id
        await Tour.next()
        await message.reply("Введите название:")


async def set_name(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        # async with savingState.proxy() as data:
        tour.name = message.text
        await Tour.next()
        await message.reply("Введите описание:")


async def set_description(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        # async with savingState.proxy() as data:
        tour.description = message.text
        await Tour.next()
        await message.reply("Введите рейтинг тура:")


async def set_rating(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        tour.rating = message.text
        await Tour.next()
        await message.reply("Город вылета:")


async def set_from_city(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        tour.from_city = message.text
        await Tour.next()
        await message.reply("Город тура:")


async def set_to_city(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        tour.to_city = message.text
        await state.finish()
        await message.reply("Дата начало тура: ", reply_markup=await DialogCalendar().start_calendar())


@dp.callback_query_handler(dialog_cal_callback.filter())
async def process_dialog_calendar(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.answer(f'You selected {date.strftime("%d/%m/%Y")}')
        tour.when_date = date
        await Tour.days.set()
        await callback_query.message.reply("Длителность в днях: ")


async def set_days(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        tour.days = message.text
        await Tour.next()
        await message.reply("Цена: ")


async def set_price(message: types.Message, state: FSMContext):
    if message.from_user.username in username:
        tour.price = message.text
        await state.finish()
        await db_connect.db_add_tour(tour)
        await message.reply("Тур успешно добавлен", reply_markup=admin_kb.admin_menu)


async def get_tours(callback: types.CallbackQuery):
    await callback.message.answer("Текущие туры:")
    await db_connect.db_get_tour(callback.message)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback: types.CallbackQuery):
    await db_connect.db_delete_tour(callback.data.replace('del ', ''))
    await callback.answer(text=f'{callback.data.replace("del ", "")} удалена', show_alert=True)

