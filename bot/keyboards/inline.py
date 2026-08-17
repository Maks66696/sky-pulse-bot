from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Router, F

router = Router()

def get_weather_inline_keyboard(lat: float, lon: float, city_name: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = 
            [[
                InlineKeyboardButton(
                text = "🔄 Обновить", 
                callback_data = f"refresh_{lat}_{lon}_{city_name}")
            ]]
                        )
    
    return keyboard
