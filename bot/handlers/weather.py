import datetime
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from bot.services.weather_api import get_coordinates, get_weather_data, format_weather_message
from bot.services.chart import create_chart
from bot.keyboards.inline import get_weather_inline_keyboard

router = Router()

@router.message(F.text)
async def handle_city_search(message: Message):
    lat, lon, city_name = await get_coordinates(message.text)
    if lat is None:
        await message.answer("❌ Город не найден. Попробуй ещё раз!")
        return
    data = await get_weather_data(lat, lon)
    if data is None:
        await message.answer("⚠️ Ошибка получения данных погоды.")
        return
    raw_times = data["hourly"]["time"][:24]
    temps = data["hourly"]["temperature_2m"][:24]
    formatted_times = [datetime.datetime.fromisoformat(t).strftime("%H:%M") for t in raw_times]
    chart_buf = create_chart(formatted_times, temps, city_name)
    text = format_weather_message(data, city_name)
    keyboard = get_weather_inline_keyboard(lat, lon, city_name)
    photo = BufferedInputFile(file=chart_buf.getvalue(),
    filename="chart.png")
    await message.answer_photo(photo=photo, caption=text, parse_mode="Markdown", reply_markup=keyboard)

@router.callback_query(F.data.startswith("refresh_"))
async def handle_refresh_callback(call: CallbackQuery):
    await call.answer("🔄 Обновляю данные...")
    _, lat, lon, city_name = call.data.split("_")
    lat, lon = float(lat), float(lon)
    data = await get_weather_data(lat, lon)
    if data is None:
        await call.message.answer("⚠️ Не удалось обновить погоду.")
        return
 
    raw_times = data["hourly"]["time"][:24]
    temps = data["hourly"]["temperature_2m"][:24]
    formatted_times = [
        datetime.datetime.fromisoformat(t).strftime("%H:%M") for t in raw_times
    ]

    chart_buf = create_chart(formatted_times, temps, city_name)
    text = format_weather_message(data, city_name)
    keyboard = get_weather_inline_keyboard(lat, lon, city_name)

    photo = BufferedInputFile(file=chart_buf.getvalue(), filename="chart.png")
    await call.message.answer_photo(
        photo=photo, caption=text, parse_mode="Markdown", reply_markup=keyboard
    ) 