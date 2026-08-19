from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_weather_inline_keyboard(lat: float, lon: float, city_name: str):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard = 
            [[
                InlineKeyboardButton(
                text = "🔄 Обновить", 
                callback_data = f"refresh_{lat}_{lon}_{city_name}")
            ],
            [
                InlineKeyboardButton(
                text = "⭐ В избранное", 
                callback_data = f"fav_{lat}_{lon}_{city_name}")
            ]]
                        )
    
    return keyboard

def get_favorites_keyboard(favorites: list):
    buttons = []
    for city_name, lat, lon in favorites:
        city_name = str(city_name)
        lat = float(lat)
        lon = float(lon)

        button = InlineKeyboardButton(
            text = f"📍 {city_name}",
            callback_data = f"refresh_{lat}_{lon}_{city_name}",
        )

        buttons.append([button])

    return InlineKeyboardMarkup(inline_keyboard = buttons)