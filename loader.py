import logging

from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

class OnOff:
    status = False

advert = OnOff()
    
# ON_OFF Advertysings blocks ON_OFF = True or False
ADMINS = [673347535, 703880354, 789663182, 649280792, 741846012, 623214940, 796119756, 675554725, 460911743, 1434266116, 1271268427]

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
