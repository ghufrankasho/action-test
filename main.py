import asyncio
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6762569300:AAGnU6WOqeoxfrcVxXOHbQooC3Gg2YkuN58'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_hello():
    # Replace chat_id with the actual chat_id of the channel
    chat_id = '-1002044150371'
    await bot.send_message(chat_id=chat_id, text='Hello, World!')

async def main():
    await send_hello()
    # other asynchronous operations here

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
