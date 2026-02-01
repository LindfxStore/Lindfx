import telebot
import os

TOKEN = os.getenv("8560972473:AAFzrLDRlkXhTokR_5i6zFnnzCrvKslhm5E")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Railway üzerinde çalışıyor 🚀")

bot.infinity_polling()
