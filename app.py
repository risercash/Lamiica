from loader import bot
from aiogram.types import BotCommand
from config import ADM

command = [
    BotCommand("start", "Перезапуск бота"),
    BotCommand("help", "Помощь по боту"),
    BotCommand('send', 'адм. Рассылка'),
    BotCommand('ankets', 'адм. Анкеты')
]

admin_id = '1434266116'


async def on_shutdown(dp):
    await bot.send_message(ADM, "Я закрылся!")


async def on_startup(dp):
    await bot.send_message(ADM, "Я запущен!")
    await bot.set_my_commands(command)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
