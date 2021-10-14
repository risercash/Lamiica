import asyncio
import json

import pandas as pd
import tobase
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery, Message
from buttons import buttons as btn
from config import user_admin_id, ME, ADM
from loader import bot, dp

userData = {}
admin_message = {}


@dp.message_handler(Command('admin'))
async def admin(message: Message):
    if message.chat.id in user_admin_id:
        await message.answer('Режим Admin-Panel', reply_markup=btn.menu)


@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer(f"""Приветствую тебя, {message.from_user.first_name} 👋

Я помогу тебе записаться на бесплатную консультацию «Анализ твоего Инстаграм»❓⁉️❓

Для того, что бы нам лучше узнать тебя 🔎 и чем тебе помочь 
нажми на кнопку, что бы заполнить анкету 
⬇️⬇️⬇️⬇️

💡Данная анкета необходима, что бы лучше подготовиться к консультации💡""", reply_markup=btn.next)
    
    new_user = tobase.new_user(message.from_user)
    if new_user:
        if message.from_user.username == None:
            usr = f"{message.from_user.full_name} ({message.from_user.id})"
        else:
            usr = f"@{message.from_user.username} ({message.from_user.id})"

        await bot.send_message(ADM, usr)


@dp.callback_query_handler(text_contains="next")
async def nextme(call: CallbackQuery):
    await call.answer(cache_time=20)
    await call.message.answer("""Если ты хочешь получить реальный результат, то отвечай на все вопросы честно и развёрнуто! 

☝️Время и дату консультации я напишу тебе в Директ! 

☝️Если вдруг ты не получишь от меня сообщение, то напиши мне в Директ в моем 👉[Инстаграм!](https://instagram.com/alena.chugavina)""", reply_markup=btn.callBack, parse_mode='Markdown')


@dp.message_handler(Command("send"))
async def start(message: Message, state: FSMContext):
    if message.from_user.id != ADM and message.from_user.id != ME:
        return
    await message.answer("Введите сообщение для рассылки")
    await state.set_state("wait_sms")


@dp.message_handler(state="wait_sms")
async def wait_sms(message: Message, state: FSMContext):
    await state.reset_state()
    users = await tobase.show_users()
    await message.answer(f"Нашел {len(users)} пользователей. Начинаю рассылку.")
    send = 0
    for user in users:
        try:
            await bot.send_message(user["user_id"], message.text)
            send += 1
        except:
            pass
        await asyncio.sleep(0.5)
    await message.answer(f"Рассылку закончил! Отправлено {send} сообщений")
    

@dp.message_handler(Command("ankets"))
async def start(message: Message):
    ankets = await tobase.show_users()
    df = pd.DataFrame(ankets)
    df.to_excel('users.xlsx')
    with open('users.xlsx', 'rb') as file:
        await message.answer_document(file)