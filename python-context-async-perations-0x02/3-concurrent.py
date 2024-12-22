import aiosqlite
import asyncio

# Database file
DATABASE_FILE = "example.db"

async def async_fetch_users():
    """
    Fetches all users from the database asynchronously.
    """
    async with aiosqlite.connect(DATABASE_FILE) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            print("All users:")
            for row in rows:
                print(row)
            return rows

async def async_fetch_older_users():
    """
    Fetches users older than 40 from the database asynchronously.
    """
    async with aiosqlite.connect(DATABASE_FILE) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            rows = await cursor.fetchall()
            print("Users older than 40:")
            for row in rows:
                print(row)
            return rows

async def fetch_concurrently():
    """
    Executes both async_fetch_users and async_fetch_older_users concurrently.
    """
    # Use asyncio.gather to run both functions at the same time
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return results

# Run the asyncio program
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
