# 🌤️ SkyPulse Bot — Асинхронный Telegram-бот прогноза погоды и инфографики

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-2CA5E0.svg?logo=telegram&logoColor=white)](https://github.com/aiogram/aiogram)
[![aiohttp](https://img.shields.io/badge/aiohttp-Async_Client-orange.svg)](https://docs.aiohttp.org/)
[![SQLite](https://img.shields.io/badge/SQLite-aiosqlite-003B57.svg?logo=sqlite&logoColor=white)](https://aiosqlite.omnilib.dev/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-RAM_Rendering-11557c.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**SkyPulse** — высокопроизводительный асинхронный Telegram-бот для получения детального прогноза погоды, автоматической генерации 24-часовой инфографики прямо в оперативной памяти и управления избранными городами с персистентным хранением в базе данных SQLite.

---

## ✨ Ключевой функционал

- ⚡ **100% Асинхронный стек:** Архитектура на `aiogram 3` и `aiohttp` гарантирует неблокирующую обработку запросов от множества пользователей параллельно.
- 📊 **Инфографика в оперативной памяти (RAM):** Отрисовка 24-часовых графиков температуры на `matplotlib` с буферизацией в `io.BytesIO` и отправкой через `BufferedInputFile` (нулевая нагрузка на файловую систему сервера).
- 🌍 **Универсальный геокодинг:** Поиск по текстовому названию любого населённого пункта планеты (с поддержкой сленга и опечаток) + приём нативных GPS-локаций с обратным геокодингом через OpenStreetMap Nominatim.
- 🗄️ **Персистентная база данных:** Асинхронное хранилище на `aiosqlite` для избранных городов с защитой от SQL-инъекций (`?`-параметризация) и предотвращением дубликатов (`UNIQUE`).
- 🔄 **Интерактивный UI:** Двухуровневая система интерфейса (главное Reply-меню + инлайн-кнопки обновления и сохранения под графиками).
- 🛡️ **Отказоустойчивость:** Обработка сетевых сбоев, таймауты (`timeout=5`) и автоматическое восстановление сессий Telegram.

---

## 🏛️ Слоистая архитектура проекта (Layered Architecture)

Проект спроектирован по стандартам модульной коммерческой разработки:

```text
sky-pulse-bot/
├── bot/
│   ├── database/          # Слой работы с базой данных
│   │   ├── __init__.py
│   │   └── db.py          # Асинхронные CRUD-операции на aiosqlite
│   │
│   ├── handlers/          # Слой роутеров и обработчиков событий
│   │   ├── __init__.py
│   │   ├── start.py       # Команды /start, меню «О боте» и «Избранное»
│   │   ├── weather.py     # Поиск погоды, инлайн-обновление и добавление в БД
│   │   └── location.py    # Обработка входящих GPS-координат
│   │
│   ├── keyboards/         # Фабрики клавиатур и разметки
│   │   ├── __init__.py
│   │   ├── reply.py       # Главное меню (ReplyKeyboardMarkup)
│   │   └── inline.py      # Инлайн-кнопки обновления и списков избранного
│   │
│   ├── services/          # Бизнес-логика и внешние интеграции
│   │   ├── __init__.py
│   │   ├── weather_api.py # Асинхронный клиент Open-Meteo & Nominatim (aiohttp)
│   │   └── chart.py       # Генератор инфографики (matplotlib в RAM)
│   │
│   └── __init__.py
│
├── .env.example           # Шаблон конфигурации окружения
├── .gitignore             # Исключение секретов, баз данных и кэша
├── config.py              # Типизированная загрузка настроек (Dataclass)
├── requirements.txt       # Зависимости проекта
└── main.py                # Асинхронная точка входа (Dispatcher & Polling)

🛠️ Стек технологий

    Язык программирования: Python 3.11+

    Telegram Framework: aiogram 3.x

    Асинхронные HTTP-запросы: aiohttp

    База данных: SQLite через aiosqlite

    Визуализация данных: matplotlib (бэкенд Agg + io.BytesIO)

    Геокодинг: Open-Meteo Geocoding API & OpenStreetMap Nominatim

    Управление окружением: python-dotenv & dataclasses

🚀 Локальный запуск и установка
1. Клонирование репозитория
code Bash

git clone https://github.com/Maks66696/sky-pulse-bot.git
cd sky-pulse-bot

2. Настройка виртуального окружения
code Bash

# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

3. Установка зависимостей
code Bash

pip install -r requirements.txt

4. Настройка переменных окружения

Создайте файл .env в корне проекта (по примеру .env.example):
code Env

BOT_TOKEN=your_telegram_bot_token_here

5. Запуск бота
code Bash

python main.py

👨‍💻 Автор

    Разработчик: Maks66696

    Проект: Портфолио асинхронных микросервисов на Python