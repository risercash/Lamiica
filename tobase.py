import asyncio
import re
from aiohttp.client import request
import pymongo

from datetime import datetime
import ssl
from config import URL


col = pymongo.MongoClient(URL)
client = pymongo.MongoClient(URL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
Users = client['LAM1']['Users']


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


async def append_insta_link(user_id, link):
    Users.update_one({"user_id": user_id},
                     {'$set': {"insta_link": link}})


async def append_request(user_id, req):
    Users.update_one({"user_id": user_id},
                     {'$set': {"request": req}})
