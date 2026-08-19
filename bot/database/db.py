import aiosqlite

DB_NAME = "database.db" 

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS favorite_cities(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                city_name TEXT,
                lat REAL,
                lon REAL,
                UNIQUE(user_id, city_name)    
            )
        """)

        await db.commit()

async def add_favorite_city(user_id: int, city_name: str, lat : float, lon : float):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT OR IGNORE INTO favorite_cities (user_id, city_name, lat, lon) 
        VALUES (?, ?, ?, ?)""", 
        (user_id, city_name, lat, lon)
        ) 
        await db.commit()

async def delete_favorite_city(user_id: int, city_name: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
        "DELETE FROM favorite_cities WHERE user_id = ? AND city_name = ?",
        (user_id, city_name)
        )
        await db.commit()


async def get_user_favorites(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT city_name, lat, lon FROM favorite_cities WHERE user_id = ?",
        (user_id,),) as cursor:
            rows = await cursor.fetchall()
            return rows
