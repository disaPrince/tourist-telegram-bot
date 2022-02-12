from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from handlers import client

b1 = KeyboardButton('Главное меню')



#Описаие и кнопки(Самые первые кнопки)
urlkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Информация', callback_data='button1'),\
                                             InlineKeyboardButton(text='Туры✈', callback_data='button2'), \
                                             InlineKeyboardButton(text='Контактные данные', callback_data='button3'), \
                                             InlineKeyboardButton(text='Выйти', callback_data='button4'))


urlb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Алматы', callback_data='button6'),\
                                             InlineKeyboardButton(text='Астана', callback_data='button6'),\
                                             InlineKeyboardButton(text='Шымкент', callback_data='button6'),\
                                             InlineKeyboardButton(text='Караганда', callback_data='button6'),\
                                             InlineKeyboardButton(text='Назад', callback_data='button5'))


urlmon = InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Январь', callback_data='button'),\
                                               InlineKeyboardButton(text='Февраль', callback_data='button'),\
                                               InlineKeyboardButton(text='Март', callback_data='button')).row(
                                               InlineKeyboardButton(text='Апрель', callback_data='button'),\
                                               InlineKeyboardButton(text='Май', callback_data='button'),\
                                               InlineKeyboardButton(text='Июнь', callback_data='button')).row(
                                               InlineKeyboardButton(text='Июль', callback_data='button'),\
                                               InlineKeyboardButton(text='Август', callback_data='button'),\
                                               InlineKeyboardButton(text='Сентябрь', callback_data='button')).row(
                                               InlineKeyboardButton(text='Октябрь', callback_data='button'),\
                                               InlineKeyboardButton(text='Ноябрь', callback_data='button'),\
                                               InlineKeyboardButton(text='Декабрь', callback_data='button')).add(
                                               InlineKeyboardButton(text='Назад', callback_data='button5'))


urlto = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Дубай', callback_data='button7'), \
                                              InlineKeyboardButton(text='Анкара', callback_data='button7'),\
                                              InlineKeyboardButton(text='Каир', callback_data='button7'),\
                                              InlineKeyboardButton(text='Майами', callback_data='button7'),\
                                              InlineKeyboardButton(text='Мадрид', callback_data='button7'),\
                                              InlineKeyboardButton(text='Венеция', callback_data='button7'), \
                                              InlineKeyboardButton(text='Назад', callback_data='button5'))

urlDate = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='1', callback_data='button3'), \
                                                InlineKeyboardButton(text='2', callback_data='button3'), \
                                                InlineKeyboardButton(text='3', callback_data='button3')).add(
                                                InlineKeyboardButton(text='Назад', callback_data='button5'))

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(b1)