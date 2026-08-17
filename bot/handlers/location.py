from bot.keyboards import reply
from bot.keyboards.reply import get_main_reply_keyboard
from aiogram import Router, F
from bot.services.weather_api import  get_weather_data, format_weather_message
from aiogram.types import Message
router = Router()

@router.message(F.location)
async def handle_location(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude
    return lat , lon
print(handle_location)