from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

admin_menu = InlineKeyboardMarkup(row_width=2)\
    .add(InlineKeyboardButton(text='Добавить Тур', callback_data='addTour'),
         InlineKeyboardButton(text='Настройка Туров ⚙', callback_data='tourSettings'))