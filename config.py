import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY")
    ADMIN_ID: int = int(os.getenv("ADMIN_ID"), 0)

config = Config()