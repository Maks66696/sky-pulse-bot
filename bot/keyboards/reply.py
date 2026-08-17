from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import Router, F

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Отправить геолокацию", request_location=True)],
            [KeyboardButton(text="⭐ Избранное"), KeyboardButton(text="ℹ️ О боте")]
        ],
        resize_keyboard=True
)
    return keyboard