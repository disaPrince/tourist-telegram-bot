from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from create_bot import dp
from keyboards import client_kb
from aiogram.dispatcher.filters import Text
from database import db_connect
from domain import Tours
from aiogram_calendar import DialogCalendar, dialog_cal_callback
from aiogram.types import CallbackQuery

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


async def start(message: types.Message):
    await message.answer(message.from_user.first_name, reply_markup=client_kb.kb)
    await message.answer('Добро пожаловать в Tour Bot!', reply_markup=client_kb.menu_b)


async def menu(message: types.Message):
    await message.answer('Давайте выберем поездку в Tour Bot!', reply_markup=client_kb.menu_b)


async def contacts(callback: types.CallbackQuery):
    await callback.message.answer('Адиль: 8708 111 62 02')
    await callback.answer()


async def information(callback: types.CallbackQuery):
    await callback.message.answer('Туристическая компания для нахождения очень выгодных туров по всему миру 🍹')
    await callback.message.answer(r'Для подробной информацией перейдите на <a href=" ">сайт компании</a>', parse_mode=types.ParseMode.HTML)
    await callback.answer()


async def func_from(callback: types.CallbackQuery):
    await callback.message.answer('Откуда вылетаете?📲', reply_markup=client_kb.from_b)
    await callback.answer()

async def func_to(callback: types.CallbackQuery):
    await callback.message.answer('Выберите страну:🌃', reply_markup=client_kb.to_b)
    from_c = callback.data
    tour.from_city = [from_c.replace('b_', '', 1)]
    await callback.answer()


async def data(callback: types.CallbackQuery):
        await callback.message.reply("Дата начало тура: ", reply_markup=await DialogCalendar().start_calendar())
        to_c = callback.data
        tour.to_city = [to_c.replace('bu_', '', 1)]
        await callback.answer()



@dp.callback_query_handler(dialog_cal_callback.filter())
async def day(callback_query: CallbackQuery, callback_data: dict):
    select, date = await DialogCalendar().process_selection(callback_query, callback_data)
    if select:
        await callback_query.message.answer(f'Вы выбрали дату: {date.strftime("%d/%m/%Y")}')
        tour.when_date = date
        # await Tour.days.set()
        await callback_query.message.answer("Длителность днях: ", reply_markup=client_kb.child_b)

# async def price(message: types.Message):
#     tour.days = message.text
#     await Tour.next()
#     await message.answer("Цена: ")


# async def price(message: types.Message, state: FSMContext):
#     tour.price = message.text
#     await state.finish()
async def budget(callback: types.CallbackQuery):
    tour.days = callback.data
    await callback.message.answer('Какой ваш бюджет: 💳', reply_markup=client_kb.budg_b)
    await callback.answer()
    await callback.message.delete()


# async def adults(callback: types.CallbackQuery):
#     await callback.message.answer('Количество взрослых(старше 16 лет): 👨‍👦‍👦', reply_markup=client_kb.adults_b)
#     await callback.answer()
#     await callback.message.delete()
#
#
# async def children(callback: types.CallbackQuery):
#     await callback.message.answer('Количество детей(младше 16 лет):👨‍👦‍👦', reply_markup=client_kb.child_b)
#     await callback.answer()
#     await callback.message.delete()

async def back(callback: types.CallbackQuery):
    await callback.message.delete()

async def result(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ваш запрос обрабатывается, ожидайте ответа 💻", show_alert=True)
    # await callback.message.answer(tour.to_city)
    await callback.message.answer('Подходящий тур по вашему запросу:')
    await callback.answer()
    await callback.message.delete()
    await db_connect.sql_read(callback.message)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_callback_query_handler(information, text='button1')
    dp.register_callback_query_handler(contacts, text='button3')
    dp.register_callback_query_handler(func_from, text='button2')
    dp.register_callback_query_handler(func_to, Text(startswith=('b_')))
    dp.register_callback_query_handler(data, Text(startswith=('bu_')))
    dp.register_callback_query_handler(budget, text='button11')
    dp.register_callback_query_handler(back, text='button4')
    dp.register_callback_query_handler(back, text='button5')
    dp.register_message_handler(menu, Text(equals='Главное меню', ignore_case=True))
    # dp.register_message_handler(price, state=Tour.days)
    # dp.register_message_handler(price, state=Tour.price)

    # dp.register_callback_query_handler(adults, text='button9')
    # dp.register_callback_query_handler(children, text='button10')
    dp.register_callback_query_handler(result, text='button9')



# async def month(callback: types.CallbackQuery):
#     await callback.message.answer('Выберите месяц:📆', reply_markup=client_kb.mon_b)
#     await callback.answer()
#
#
#
# async def day(callback: types.CallbackQuery):
#     await callback.message.answer('Выберите день:📅', reply_markup=client_kb.day_b)
#     await callback.answer()
