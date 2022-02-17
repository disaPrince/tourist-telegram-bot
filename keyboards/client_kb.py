from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Главное меню'))





menu_b = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='Информация 🖥', callback_data='button1'),\
                                             InlineKeyboardButton(text='Туры✈', callback_data='button2'), \
                                             InlineKeyboardButton(text='Контактные данные 📱', callback_data='button3'), \
                                             InlineKeyboardButton(text='Выйти 🔴', callback_data='button4'))


from_b = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Алматы', callback_data='button6'),\
                                             InlineKeyboardButton(text='Астана', callback_data='button6'),\
                                             InlineKeyboardButton(text='Шымкент', callback_data='button6'),\
                                             InlineKeyboardButton(text='Караганда', callback_data='button6'),\
                                             InlineKeyboardButton(text='Назад', callback_data='button5'))


mon_b = InlineKeyboardMarkup(row_width=1).row(InlineKeyboardButton(text='Январь', callback_data='button'),\
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


to_b = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Дубай', callback_data='button7'), \
                                              InlineKeyboardButton(text='Анкара', callback_data='button7'),\
                                              InlineKeyboardButton(text='Каир', callback_data='button7'),\
                                              InlineKeyboardButton(text='Майами', callback_data='button7'),\
                                              InlineKeyboardButton(text='Мадрид', callback_data='button7'),\
                                              InlineKeyboardButton(text='Венеция', callback_data='button7'), \
                                              InlineKeyboardButton(text='Назад', callback_data='button5'))



day_b = InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(text='1', callback_data='button8'), InlineKeyboardButton(text='2', callback_data='button8'), InlineKeyboardButton(text='3', callback_data='button8'),\
                                             InlineKeyboardButton(text='4', callback_data='button8'), InlineKeyboardButton(text='5', callback_data='button8'), InlineKeyboardButton(text='6', callback_data='button8'),\
                                             InlineKeyboardButton(text='7', callback_data='button8'), InlineKeyboardButton(text='8', callback_data='button8'), InlineKeyboardButton(text='9', callback_data='button8'),\
                                             InlineKeyboardButton(text='10', callback_data='button8'), InlineKeyboardButton(text='11', callback_data='button8'), InlineKeyboardButton(text='12', callback_data='button8'),\
                                             InlineKeyboardButton(text='13', callback_data='button8'), InlineKeyboardButton(text='14', callback_data='button8'), InlineKeyboardButton(text='15', callback_data='button8'),\
                                             InlineKeyboardButton(text='16', callback_data='button8'), InlineKeyboardButton(text='17', callback_data='button8'), InlineKeyboardButton(text='18', callback_data='button8'),\
                                             InlineKeyboardButton(text='19', callback_data='button8'), InlineKeyboardButton(text='20', callback_data='button8'), InlineKeyboardButton(text='21', callback_data='button8'),\
                                             InlineKeyboardButton(text='22', callback_data='button8'), InlineKeyboardButton(text='23', callback_data='button8'), InlineKeyboardButton(text='24', callback_data='button8'),\
                                             InlineKeyboardButton(text='25', callback_data='button8'), InlineKeyboardButton(text='26', callback_data='button8'), InlineKeyboardButton(text='27', callback_data='button8'),\
                                             InlineKeyboardButton(text='28', callback_data='button8'), InlineKeyboardButton(text='29', callback_data='button8'), InlineKeyboardButton(text='30', callback_data='button8'))\
                                             .insert(InlineKeyboardButton(text='31', callback_data='button8'))




budg_b = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='100 000 - 200 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='200 000 - 400 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='400 000 - 600 000 тг', callback_data='button9'),\
                                             InlineKeyboardButton(text='600 000 - 1 000 000 тг', callback_data='button9'))

adults_b = InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(text='1', callback_data='button10'),\
                                              InlineKeyboardButton(text='2', callback_data='button10'),\
                                              InlineKeyboardButton(text='3', callback_data='button10'),\
                                              InlineKeyboardButton(text='4', callback_data='button10'),\
                                              InlineKeyboardButton(text='5', callback_data='button10'))

child_b = InlineKeyboardMarkup(row_width=5).add(InlineKeyboardButton(text='1', callback_data='button11'),\
                                              InlineKeyboardButton(text='2', callback_data='button11'),\
                                              InlineKeyboardButton(text='3', callback_data='button11'),\
                                              InlineKeyboardButton(text='4', callback_data='button11'),\
                                              InlineKeyboardButton(text='5', callback_data='button11'))
