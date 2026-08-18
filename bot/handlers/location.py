from aiogram import Router, F
from bot.services.weather_api import get_weather_data, format_weather_message, get_city_name
from bot.services.chart import create_chart
from aiogram.types import Message, BufferedInputFile
from bot.keyboards.inline import get_weather_inline_keyboard

import datetime
router = Router()


@router.message(F.location)
async def handle_location(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude
    weather_data = await get_weather_data(lat , lon)
    if weather_data is None:
        await message.answer(
            f"⚠️ Не удалось получить данные о погоде."
        )
        return
    city_name = await get_city_name(lat, lon)
    if city_name is None:
        city_name = "вашем местоположении"
        
    text = format_weather_message(weather_data, city_name)
    raw_times = weather_data["hourly"]["time"][:24]
    temps = weather_data["hourly"]["temperature_2m"][:24]
    formatted_times = [datetime.datetime.fromisoformat(t).strftime("%H:%M") for t in raw_times]
    chart_buf = create_chart(formatted_times, temps, city_name)
    keyboard = get_weather_inline_keyboard(lat, lon, city_name)
    photo = BufferedInputFile(file=chart_buf.getvalue(),
    filename="chart.png")
    await message.answer_photo(photo=photo, caption=text, parse_mode="Markdown", reply_markup=keyboard)
    
    