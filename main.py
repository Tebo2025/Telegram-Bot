import telebot
from flask import Flask, request
import os
from telebot import types

API_TOKEN = '7294673307:AAHEKkdBwnHfp4QImiELzjxyyLrzqBsF_uw'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# Ana menyu
@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🚌 Tours", callback_data='tours'),
        types.InlineKeyboardButton("🚘 Transfers", callback_data='transfers'),
        types.InlineKeyboardButton("🎉 Packages", callback_data='packages'),
        types.InlineKeyboardButton("🛂 Visa", callback_data='visa'),
        types.InlineKeyboardButton("🏨 Hotels", callback_data='hotels'),
        types.InlineKeyboardButton("💬 Support", callback_data='support'),
        types.InlineKeyboardButton("📖 About", callback_data='about')
    )
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
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🏙️ Baku City Tour", callback_data='baku_tour'),
            types.InlineKeyboardButton("🪨 Gobustan & Absheron", callback_data='gobustan'),
            types.InlineKeyboardButton("🏔 Shahdag Adventure", callback_data='shahdag'),
            types.InlineKeyboardButton("🌲 Gabala Day Trip", callback_data='gabala'),
            types.InlineKeyboardButton("🏛 Sheki Cultural Tour", callback_data='sheki'),
            types.InlineKeyboardButton("🍷 Shamakhi Wine", callback_data='shamakhi'),
            types.InlineKeyboardButton("📩 WhatsApp", url='https://wa.me/994774186543?text=Hi%2C+I+want+to+book+a+tour'),
            types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main')
        )
        bot.edit_message_text("Select a tour to learn more:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == 'transfers':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🛫 Airport ↔ Hotel", callback_data='airport'),
            types.InlineKeyboardButton("🚘 Round Trip Transfers", callback_data='roundtrip'),
            types.InlineKeyboardButton("🚖 VIP Vehicle Rental", callback_data='vip'),
            types.InlineKeyboardButton("📩 WhatsApp", url='https://wa.me/994774186543?text=Hi%2C+I+need+a+transfer'),
            types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main')
        )
        bot.edit_message_text("Select a transfer option:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == 'packages' or call.data == 'visa' or call.data == 'hotels' or call.data == 'support' or call.data == 'about':
        markup = types.InlineKeyboardMarkup(row_width=1)
        if call.data == 'packages':
            text = "🎉 Tell us your group size, dates and interests – and we’ll build your perfect package!"
        elif call.data == 'visa':
            text = "🛂 We assist with tourist e-visas. Just tell us your nationality and travel dates."
        elif call.data == 'hotels':
            text = "🏨 From 3★ to 5★ hotels, we offer the best stays in top locations."
        elif call.data == 'support':
            text = "💬 Contact our support team 24/7 via WhatsApp."
        elif call.data == 'about':
            text = "📖 Baku Life Tours: Trusted by 100,000+ travelers since 2017."
        markup.add(
            types.InlineKeyboardButton("📩 WhatsApp", url='https://wa.me/994774186543'),
            types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main')
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == 'main':
        send_start(call.message)

    # Turların geniş təsviri
    elif call.data == 'baku_tour':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🏙️ **Baku City Tour**\n\nDiscover the charm of Baku with our city tour that covers iconic landmarks such as Flame Towers, Highland Park, the historical Old City (Icherisheher), Maiden Tower, Nizami Street, and the stunning Baku Boulevard. Our guide will share fascinating stories about Azerbaijan’s past and present. Includes transportation and local guide.")
    elif call.data == 'gobustan':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🪨 **Gobustan & Absheron Tour**\n\nA journey to ancient rock carvings and mud volcanoes at Gobustan National Park followed by a trip to Absheron Peninsula to visit Ateshgah Fire Temple and Yanar Dag (Burning Mountain). Perfect for history and nature lovers!")
    elif call.data == 'shahdag':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🏔 **Shahdag Mountain Adventure**\n\nA full-day adventure to Azerbaijan’s famous mountain resort. Enjoy snow sports in winter or hiking, quad biking, and cable cars in summer. Ideal for thrill-seekers and nature enthusiasts.")
    elif call.data == 'gabala':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🌲 **Gabala Day Trip**\n\nExplore the green landscapes of Gabala. Visit Nohur Lake, Tufandag Mountain Resort, shooting club, waterfalls, and enjoy local cuisine. Great for families and relaxation.")
    elif call.data == 'sheki':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🏛 **Sheki Cultural Tour**\n\nVisit the historical city of Sheki. Highlights include the Sheki Khan’s Palace, Karvansaray, local sweet shops (halva), and artisans making silk and stained glass. A cultural gem of the Caucasus.")
    elif call.data == 'shamakhi':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🍷 **Shamakhi Wine Experience**\n\nTaste Azerbaijan’s best wines at Shamakhi’s vineyards. Includes wine tasting, cellar tour, and traditional lunch in a scenic location. A relaxing and tasteful experience for wine lovers.")

    # Transfer alt-menular
    elif call.data == 'airport':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🛬 **Airport ↔ Hotel Transfers**\n\n24/7 reliable transfers from Heydar Aliyev Airport to any hotel in Baku. Clean vehicles, English-speaking driver available, and optional name sign at the arrival gate.")
    elif call.data == 'roundtrip':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🚘 **Round Trip Transfers**\n\nComfortable and safe transfers from Baku to regions like Gabala, Shahdag, Sheki, Guba, and back. Vehicles with AC, multiple seat options, and professional drivers.")
    elif call.data == 'vip':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "🚖 **VIP Vehicle Rental**\n\nBook premium vehicles such as Mercedes V-Class, Sprinter, and SUVs with a private driver. Perfect for business trips, delegations, and luxury travel.")

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
