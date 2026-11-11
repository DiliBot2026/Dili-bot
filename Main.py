import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command

# Bot ma'lumotlari
TOKEN = "9262757777:AAGbWdjJLh3boXuMFQi011K-SYXtN22q4Dg"
GROUP_ID = -1003854810251
CHANNEL_USERNAME = "@pereprodajaoling_soting"

# Kino bazasi (Kino kodi va uning Telegram video ID raqami)
MOVIES = {
    "1": "BAACAgIAAxkBAAIB...",  # 1-kino uchun video file_id
    "2": "BAACAgIAAxkBAAIB...",  # 2-kino uchun video file_id
}

# Botni sozlash
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i uchun javob
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        f"Salom! 🎬 Kino botimiz faol ishlayapti.\n\n"
        f"Kino kodini yuboring va kinoni tomosha qiling!"
    )

# Kino kodini qabul qilish va video yuborish
@dp.message(F.text)
async def send_movie(message: types.Message):
    code = message.text.strip()
    
    if code in MOVIES:
        video_id = MOVIES[code]
        await message.answer_video(
            video=video_id,
            caption=f"🎬 Siz so'ragan kino! Kanalimiz: {CHANNEL_USERNAME}"
        )
    else:
        await message.answer("❌ Bunday kodli kino topilmadi. Iltimos, to'g'ri kod yuboring.")

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
