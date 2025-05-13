import logging
import openai
import os

from aiogram import Bot, Dispatcher, executor, types

# Telegram и OpenAI токены
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def handle_message(message: types.Message):
    user_message = message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты умный, прямой и честный ассистент проекта «Тихий Стыд». Помогаешь разбирать внутренние блоки, стыд и самосаботаж, говоришь по делу, дружелюбно, но твёрдо."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        bot_reply = response["choices"][0]["message"]["content"]
        await message.reply(bot_reply)

    except Exception as e:
        await message.reply(f"Ошибка: {e}")

if __name__ == " в __main__":
    executor.start_polling(dp, skip_updates=True)
