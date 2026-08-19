import aiohttp



async def get_coordinates( city_name: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=ru&format=json"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=5) as response:
                data = await response.json()
        except Exception:
                return None , None , None
        
    if "results" not in data or not data["results"]:
         return None , None , None
    
    first_result = data["results"][0]
    return(
        first_result["latitude"],
        first_result["longitude"],
        first_result["name"],
    )
                
async def get_weather_data(lat: float, lon: float):
     url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m&forecast_days=1"
     async with aiohttp.ClientSession() as session:
        try:
               async with session.get(url, timeout=10) as response:
                    data = await response.json()
        except Exception:
                    print(f"❌ Ошибка сети в get_weather_data: {type(e).__name__} - {e}")
                    return None

     if "current_weather" not in data or not data["current_weather"]:
           print(f"❌ Open-Meteo вернул странный ответ: {data}")
           return None
     return data
      
WEATHER_CODES = {
    0: "☀️ Ясно",
    1: "🌤️ Малооблачно",
    2: "⛅ Переменная облачность",
    3: "☁️ Пасмурно",
    45: "🌫️ Туман",
    51: "🌧️ Морось",
    61: "🌧️ Небольшой дождь",
    63: "🌧️ Умеренный дождь",
    65: "🌧️ Сильный дождь",
    71: "❄️ Небольшой снег",
    73: "❄️ Снегопад",
    80: "🌦️ Ливень",
    95: "🌩️ Гроза",
}

async def get_city_name(lat: float, lon: float):
     url = "https://nominatim.openstreetmap.org/reverse"
     headers = {
        "User-Agent": "sky-pulse-bot/1.0"
     }
     async with aiohttp.ClientSession(headers=headers) as session:
          try:
            async with session.get(
                     url, 
                     params = { 
                        "lat":lat,
                        "lon":lon,
                        "format": "json",
                        "accept-language": "ru",
                    },  
                        timeout=5
                ) as response:
                    print(response.status)
                    print("Nominatim status:", response.status)
                    data = await response.json()
                    address = data.get("address")
                    if address is None:
                         return None
                    city_name = (
                         address.get("city")
                         or address.get("town")
                         or address.get("village")
                    )
                    return city_name
          except Exception as e:
            print(type(e).__name__, repr(e))
            return None

                    

def format_weather_message(data: dict, city_name: str) -> str:
    current = data["current_weather"]
    temp = current["temperature"]
    code = current["weathercode"]
    wind = current["windspeed"]

    status = WEATHER_CODES.get(code, "🌈 Погода")

    advice = "Одевайся по погоде!"
    if temp <= 0:
        advice = "На улице мороз! Надевай пуховик, шапку и шарф."
    elif temp <= 15:
        advice = "Прохладно. Надевай куртку или тёплую худи."
    elif temp <= 22:
        advice = "Приятная погода. Подойдёт кофта или ветровка."
    elif temp < 35:
        advice = "Жара! Надевай футболку и шорты."
    else:
        advice = "Экстремальная жара! Не выходи на солнце без кепки и пей больше воды!"

    return (
        f"Погода в **{city_name}**: {temp}°C\n"
        f"{status}\n"
        f"💨 Ветер: {wind} км/ч\n\n"
        f"{advice}"
    )