from aiogram import types

keyboard = types.InlineKeyboardMarkup()
key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
keyboard.add(key_yes, key_no)

callBack = types.InlineKeyboardMarkup()
callBack.add(types.InlineKeyboardButton(text='📑 «АНКЕТА» 📑', url="https://forms.gle/goFYS5sEoQzWcso46"))

next = types.InlineKeyboardMarkup()
next.add(types.InlineKeyboardButton(text='Понятно!', callback_data="next"))

# Основоное меню админки
menu = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
menu.add(
    types.KeyboardButton('Создать сообщения'),
    types.KeyboardButton('Скачать Анкету пользователей!')
)


admin_menu = types.InlineKeyboardMarkup(row_width=2)
admin_menu.add(
    types.InlineKeyboardButton('Да, отправить',callback_data='send_message'),
    types.InlineKeyboardButton('Редактировать сообщение', callback_data='edit_message'),
)

step = types.InlineKeyboardMarkup(row_width=2)
step.add(
    types.InlineKeyboardButton('Изменить текст',callback_data='edit_step_text'),
    types.InlineKeyboardButton('Изменить картинку',callback_data='edit_step_photo'),
    types.InlineKeyboardButton('Следующий этап', callback_data='next_step'),
)

step_skip = types.InlineKeyboardMarkup(row_width=1)
step_skip.add(
    types.InlineKeyboardButton('Пропустить', callback_data='step_skip'),
)

startBoard = types.InlineKeyboardMarkup(row_width=1)
startBoard.add(
    types.InlineKeyboardButton('🔁 Заного 🔁', callback_data='sb'),
)