from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.reply import get_main_reply_keyboard
from bot.database.db import get_user_favorites
from bot.keyboards.inline import get_favorites_keyboard
from aiogram.types import FSInputFile, Message
from config import config

router = Router()


@router.message(F.text == "/start")
async def cmd_about(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! \n" 
        "Напиши название города или нажми кнопку внизу:" ,
        reply_markup=get_main_reply_keyboard())

@router.message(F.text == "ℹ️ О боте")
async def about_bot(message: Message):
    about_text = (
        "🌤️ *SkyPulse Bot v2.0*\n\n"
        "Умный погодный ассистент:\n"
        "• Точный прогноз в любой точке мира и по GPS 📍\n"
        "• Автоматическая инфографика и графики на 24 часа 📊\n"
        "• Подробные данные о ветре и советы по одежде 👕\n\n"
        "👨‍💻 Разработчик: @MaKsIm196E"
    )
    await message.answer(about_text, parse_mode = "Markdown")

@router.message(F.text == "⭐ Избранное")
async def cmd_favorites(message: Message):
    favorites = await get_user_favorites(message.from_user.id)
    if not favorites:
        await message.answer(
                "⭐ У вас пока нет избранных городов.\n\nНайдите город через поиск и нажмите кнопку «⭐ В избранное» под графиком!"
            )
    else:
        keyboard = get_favorites_keyboard(favorites)
        await message.answer(
            "⭐ Ваши избранные города:\nНажмите на город, чтобы посмотреть погоду:", reply_markup=keyboard
        )

@router.message(Command("get_db"))
async def send_db_backup(message: Message):
    if message.from_user.id != config.ADMIN_ID:
        await message.answer("⛔ У вас нет прав администратора!")
        return

    db_file = FSInputFile("database.db")
    await message.answer_document(
        document = db_file, caption = "🗄️ Актуальная база данных прямо с сервера!"
    )
