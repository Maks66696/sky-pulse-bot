import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from config import config
from bot.database.db import init_db
from bot.handlers import start, weather, location


logging.basicConfig(level=logging.INFO)

async def handle_ping(request):
    return web.Response(text="🌤️ SkyPulse Bot is alive and running 24/7!")

async def main():
    
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(location.router)
    dp.include_router(weather.router)

    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())