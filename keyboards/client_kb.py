from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Главное меню'))

menu_b = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Информация 🖥', callback_data='information'),\
                                             InlineKeyboardButton(text='Туры✈', callback_data='tours'), \
                                             InlineKeyboardButton(text='Контактные данные 📱', callback_data='contacts'), \
                                             InlineKeyboardButton(text='Выйти 🔴', callback_data='back'))

from_b = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Алматы', callback_data='b_Almaty'),\
                                             InlineKeyboardButton(text='Астана', callback_data='b_Astana'),\
                                             InlineKeyboardButton(text='Шымкент', callback_data='b_Shymkent'),\
                                             InlineKeyboardButton(text='Караганда', callback_data='b_Karaganda'),\
                                             InlineKeyboardButton(text='Кызылорда', callback_data='b_Qyzylorda'),\
                                             InlineKeyboardButton(text='Костанай', callback_data='b_Kostanay'),\
                                             InlineKeyboardButton(text='Семей', callback_data='b_Semey'),\
                                             InlineKeyboardButton(text='Актау', callback_data='b_Aktau'),\
                                             InlineKeyboardButton(text='Атырау', callback_data='b_Atyrau'),\
                                             InlineKeyboardButton(text='Актобе', callback_data='b_Aktobe'),\
                                             InlineKeyboardButton(text='Тараз', callback_data='b_Taraz'),\
                                             InlineKeyboardButton(text='Павлодар', callback_data='b_Pavlodar'),\
                                             InlineKeyboardButton(text='Усть-Каменогорск', callback_data='b_Oskemen'),\
                                             InlineKeyboardButton(text='Орал', callback_data='b_Oral'),\
                                             InlineKeyboardButton(text='Туркестан', callback_data='b_Turkestan'),\
                                             InlineKeyboardButton(text='Петропавловск', callback_data='b_Petropavlovsk'),\
                                             InlineKeyboardButton(text='Назад', callback_data='back'))

to_b = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Дубай', callback_data='bu_Dubai'), \
                                              InlineKeyboardButton(text='Анкара', callback_data='bu_Ankara'),\
                                              InlineKeyboardButton(text='Каир', callback_data='bu_Kair'),\
                                              InlineKeyboardButton(text='Майами', callback_data='bu_Maiyami'),\
                                              InlineKeyboardButton(text='Мадрид', callback_data='bu_Madrid'),\
                                              InlineKeyboardButton(text='Венеция', callback_data='bu_Venecia'), \
                                              InlineKeyboardButton(text='Нью Йорк', callback_data='bu_New York'), \
                                              InlineKeyboardButton(text='Назад', callback_data='back'))

budg_b = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='100 000 - 200 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='200 000 - 400 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='400 000 - 600 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='600 000 - 1 000 000 тг', callback_data='button9'))

days_b = InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(text='1', callback_data='but_1'),\
                                              InlineKeyboardButton(text='2', callback_data='but_2'),\
                                              InlineKeyboardButton(text='3', callback_data='but_3'),\
                                              InlineKeyboardButton(text='4', callback_data='but_4'),\
                                              InlineKeyboardButton(text='5', callback_data='but_5'))
