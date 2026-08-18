from bot.handlers import start, weather, location
import asyncio
import logging
from config import config
from aiogram import Bot, Dispatcher



logging.basicConfig(level=logging.INFO)


async def main():
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(location.router)
    dp.include_router(weather.router)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())