from aiogram import Dispatcher
from aiogram.types import *

from loader import dp


async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")



def register_users_py(dp: Dispatcher):
    pass

