from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio

bot = Bot(token='6762569300:AAGnU6WOqeoxfrcVxXOHbQooC3Gg2YkuN58')
dp = Dispatcher(bot)
# async def send_hello():
#     # Replace chat_id with the actual chat_id of the channel
#     chat_id = '-1002044150371'
#     await bot.send_message(chat_id=chat_id, text='Hello, World!')

# async def main():
#     await send_hello()
#     # other asynchronous operations here


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
# Dictionary to store user inputs
user_inputs = {}
data = {}
logging.basicConfig(level=logging.INFO)


@dp.message_handler(lambda message: message.text)
async def start(message: types.Message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # insert_image_button = types.KeyboardButton("Insert Image 📷")
    # insert_name_button = types.KeyboardButton("Insert Name 📝")
    # insert_code_button = types.KeyboardButton("Insert Code 🔢")
    # send_post_button = types.KeyboardButton("Send Post 📮")
    # keyboard.add(insert_image_button, insert_name_button, insert_code_button, send_post_button)
    await message.reply(f"Welcome to the product insertion bot! +{message.text}")


# # Handler for inserting image
# @dp.message_handler(lambda message: message.text == "Insert Image 📷")
# async def insert_image(message: types.Message):
#     await message.reply("Please upload an image.")
#     user_inputs[message.from_user.id] = {"type": "image"}


# # Handler for inserting name
# @dp.message_handler(lambda message: message.text == "Insert Name 📝")
# async def insert_name(message: types.Message):
#     await message.reply("Please insert the name of the product.")
#     user_inputs[message.from_user.id]['name'] =None


# # Handler for inserting code
# @dp.message_handler(lambda message: message.text == "Insert Code 🔢")
# async def insert_code(message: types.Message):
#     await message.reply("Please insert the product code.")
#     user_inputs[message.from_user.id]['code'] = None


# # Handler for receiving images
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def handle_uploaded_image(message: types.Message):
#     user_id = message.from_user.id
#     print(user_id)
#     if user_id not in user_inputs:
#         await message.reply("Please start with /start command.")
#         return

#     if user_inputs[user_id].get("type") != "image":
#         await message.reply("Please insert an image at the right step.")
#         return

#     user_inputs[user_id]["image_id"] = message.photo[-1].file_id
#     print(user_inputs)
#     await message.reply("Image received!")


# @dp.message_handler(lambda message: message.text != "Send Post 📮")
# async def handle_text(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in user_inputs:
#         await message.reply("Please start with /start command.")
#         return

#     if "name" in user_inputs[user_id] and user_inputs[user_id]['name'] is None:
#         user_inputs[message.from_user.id]['name'] = message.text
#         await message.reply("Name received!")
#         if "code" in user_inputs[user_id] and user_inputs[user_id]['code'] is not None:
#             await message.reply_photo(photo=user_inputs[user_id]["image_id"],
#                                       caption=f'Product Name 📝 : {user_inputs[user_id]["name"]} \n\nProduct Code 🔢: {user_inputs[user_id]["code"]}')
#             await message.reply("if you want to send this post click the send post button")
#         return
#     if "code" in user_inputs[user_id] and user_inputs[user_id]['code'] is None:
#         user_inputs[message.from_user.id]['code'] = message.text
#         await message.reply("Code received!")
#         if "name" in user_inputs[user_id] and user_inputs[user_id]['name'] is not None:

#             await message.reply_photo(photo=user_inputs[user_id]["image_id"],
#                                       caption=f'Product Name 📝 : {user_inputs[user_id]["name"]} \n\nProduct Code 🔢: {user_inputs[user_id]["code"]}')
#             await message.reply("if you want to send this  click the Send Post button")
#         return


# # Handler for sending post
# @dp.message_handler(lambda message: message.text == "Send Post 📮")
# async def send_post(message: types.Message):
#     print(user_inputs)
#     user_id = message.from_user.id
#     if user_id not in user_inputs or len(user_inputs[user_id]) < 3:
#         await message.reply("Please insert all required data before sending the post.")
#         return

#     post_data = user_inputs[user_id]




#         # send_to_groups(bot,data)
#     await send_to_groups(bot, post_data,message)
#     await message.reply("Post sent to groups!")
#         # time.sleep(10)


# async def send_to_groups(bot, post_data,message):
#     try:

#         await bot.send_photo(chat_id='-1002044150371', photo=post_data["image_id"],
#                              caption=f'Product Name 📝 : {post_data["name"]} \n\nProduct Code 🔢: {post_data["code"]}')
#         logging.info("Post sent to groups successfully.")
#     except Exception as e:
#         logging.error(f"Error occurred while sending post: {e}")



executor.start_polling(dp)

