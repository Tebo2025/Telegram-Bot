import telebot
from flask import Flask, request
import os
from telebot import types

API_TOKEN = '7294673307:AAHEKkdBwnHfp4QImiELzjxyyLrzqBsF_uw'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🚌 Tours", callback_data='tours')
    btn2 = types.InlineKeyboardButton("🚘 Transfers", callback_data='transfers')
    btn3 = types.InlineKeyboardButton("🎉 Packages", callback_data='packages')
    btn4 = types.InlineKeyboardButton("🛂 Visa", callback_data='visa')
    btn5 = types.InlineKeyboardButton("🏨 Hotels", callback_data='hotels')
    btn6 = types.InlineKeyboardButton("💬 Support", callback_data='support')
    btn7 = types.InlineKeyboardButton("📖 About", callback_data='about')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.chat.id, """
👋 Welcome to Baku Life Tours!

Explore Azerbaijan with our all-in-one travel services:
🚌 Daily & Private Tours
🚘 Transfers (Standard to VIP)
🏨 Hotel Bookings
🛂 Visa Assistance
👨‍👩‍👧‍👦 Group & Corporate Packages

👇 Please choose a service to begin.
    """, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'tours':
        send_tours(call.message)
    elif call.data == 'transfers':
        send_transfers(call.message)
    elif call.data == 'packages':
        send_packages(call.message)
    elif call.data == 'visa':
        send_visa(call.message)
    elif call.data == 'hotels':
        send_hotels(call.message)
    elif call.data == 'support':
        send_support(call.message)
    elif call.data == 'about':
        send_about(call.message)

@bot.message_handler(commands=['tours'])
def send_tours(message):
    bot.reply_to(message, """
📍 Our Most Popular Tours:

• Baku City Tour  
• Gobustan & Absheron Tour  
• Shahdag Mountain Adventure  
• Gabala Day Trip  
• Sheki Cultural Tour  
• Shamakhi Wine Experience

📲 DM us to book or write us on WhatsApp - +994774186543.
    """)

@bot.message_handler(commands=['transfers'])
def send_transfers(message):
    bot.reply_to(message, """
🚘 Reliable Transfers in Azerbaijan:

• Airport Pickup/Drop  
• City-to-City Rides (Gabala, Shahdag, Sheki, etc.)  
• VIP Vehicles: V-Class, Sprinter, SUVs

✅ Private & group options available  
📅 Book via DM or tell us your route & date on WhatsApp!
    """)

@bot.message_handler(commands=['packages'])
def send_packages(message):
    bot.reply_to(message, """
🎉 Group & Custom Packages:

Whether it's family, friends, or corporate travel —
We build packages tailored to your group size & preferences.

🧾 Tell us these information on WhatsApp:
• How many people?
• Travel dates?
• Interests?

We’ll send you a full plan!
    """)

@bot.message_handler(commands=['visa'])
def send_visa(message):
    bot.reply_to(message, """
🛂 Need a visa for Azerbaijan?

✅ Fast e-visa application  
✅ Tourist visa assistance  
✅ Full guidance step-by-step

Send us your nationality & preferred travel dates on WhatsApp to begin.
    """)

@bot.message_handler(commands=['hotels'])
def send_hotels(message):
    bot.reply_to(message, """
🏨 Let us find the best stay for you!

• 3★ to 5★ Hotels  
• Central or scenic locations  
• Best price guarantee

📍 Just tell us:  
City – Dates – Guests – Preferences
    """)

@bot.message_handler(commands=['support'])
def send_support(message):
    bot.reply_to(message, """
💬 Need help or have questions?

Our support team is available 24/7.  
Click below to chat with a human:  
📩 +994774186543
    """)

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, """
📖 About Baku Life Tours

We are a Baku-based travel agency offering:  
✅ Daily & Private Tours  
✅ Transfers (Standard–VIP)  
✅ Visa Support  
✅ Hotel Booking  
✅ Custom Group Trips

Trusted by 100,000+ travelers since 2017.
    """)

@app.route(f'/{API_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return '!', 200

@app.route('/', methods=['GET'])
def index():
    return 'Bot is alive!', 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
