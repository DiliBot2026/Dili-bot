import os
import sqlite3
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "9262757777:AAGbWdjJLh3boXuMFQi011K-SYXtN22q4Dg"
GROUP_ID = -1003854810251
CHANNEL_NAME = "@pereprodajaoling_soting"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Kino botimiz faol ishlayapti 🎬")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
