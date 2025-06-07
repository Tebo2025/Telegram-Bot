import telebot
from flask import Flask, request
import os

API_TOKEN = '7294673307:AAHEKkdBwnHfp4QImiELzjxyyLrzqBsF_uw'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, """
👋 Welcome to Baku Life Tours!

Explore Azerbaijan with our all-in-one travel services:
🚌 Daily & Private Tours
🚘 Transfers (Standard to VIP)
🏨 Hotel Bookings
🛂 Visa Assistance
👨‍👩‍👧‍👦 Group & Corporate Packages

👇 Please choose a service to begin.
    """)

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

📲 DM us to book or type the tour name for details.
    """)

@bot.message_handler(commands=['transfers'])
def send_transfers(message):
    bot.reply_to(message, """
🚘 Reliable Transfers in Azerbaijan:

• Airport Pickup/Drop  
• City-to-City Rides (Gabala, Shahdag, Sheki, etc.)  
• VIP Vehicles: V-Class, Sprinter, SUVs

✅ Private & group options available  
📅 Book via DM or tell us your route & date!
    """)

@bot.message_handler(commands=['packages'])
def send_packages(message):
    bot.reply_to(message, """
🎉 Group & Custom Packages:

Whether it's family, friends, or corporate travel —
We build packages tailored to your group size & preferences.

🧾 Tell us:
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

Send us your nationality & preferred travel dates to begin.
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
📩 @bakulifetravel
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
