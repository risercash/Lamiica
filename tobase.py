import asyncio
import re
import pymongo

from datetime import datetime
import ssl
from config import URL


col = pymongo.MongoClient(URL)
client = pymongo.MongoClient(URL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
Users = client['LAM']['Users']


def new_user(usr):
    ''' ==== База пользователей ==== '''
    new_user = Users.find_one({'user_id': usr.id})

    if not new_user:
        new_user = ({
            "user_id": usr.id,
            "username": usr.username,
            "full_name": usr.full_name,
            "date": datetime.today().strftime("%d.%m.%y %H:%M"),
        })
        Users.insert_one(new_user)
        return new_user


async def show_users(): return list(Users.find({}, {'_id': 0}))