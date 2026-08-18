from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.reply import get_main_reply_keyboard

router = Router()

about_text = (
    "🌤️ **SkyPulse Bot **\n\n"
    "Умный погодный ассистент:\n"
    "• Точный прогноз в любой точке мира и по GPS 📍\n"
    "• Автоматическая инфографика и графики на 24 часа 📊\n"
    "• Подробные данные о ветре и советы по одежде 👕\n\n"
    "👨‍💻 Разработчик: @твой_юзернейм"
)

@router.message(F.text == "/start")
async def cmd_about(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! \n" 
        "Напиши название города или нажми кнопку внизу:" ,
        reply_markup=get_main_reply_keyboard())

@router.message(F.text == "ℹ️ О боте")
async def about_bot(message: Message):
    await message.answer(about_text, parse_mode = "Markdown")

@router.message(F.text == "⭐ Избранное")
async def cmd_favorites(message: Message):
    await message.answer(
        "⭐ Раздел «Избранное» находится в разработке!\n"
        "Скоро здесь можно будет сохранять свои любимые города."
    )