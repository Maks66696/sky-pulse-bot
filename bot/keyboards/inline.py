from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
