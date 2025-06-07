import telebot
from flask import Flask, request

API_TOKEN = '7294673307:AAHEKkdBwnHfp4QImiELzjxyyLrzqBsF_uw'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Baku Life Tours!\nChoose: /tours /transfers")

@bot.message_handler(commands=['tours'])
def show_tours(message):
    bot.reply_to(message, "🌍 Gabala, Guba, Shahdag, Gobustan, Absheron")

@bot.message_handler(commands=['transfers'])
def show_transfers(message):
    bot.reply_to(message, "🚐 Airport Transfers & VIP Services\nContact: https://wa.me/994774186543")

@app.route(f"/{API_TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "!", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is alive!", 200

if __name__ == "__main__":
    app.run(debug=True)
