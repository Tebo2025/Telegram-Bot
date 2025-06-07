import telebot
from flask import Flask, request
import os
from telebot import types

API_TOKEN = '7294673307:AAHEKkdBwnHfp4QImiELzjxyyLrzqBsF_uw'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

WEBSITE_URL = "https://bakulifetours.com/"
WHATSAPP_URL = "https://wa.me/994774186543?text=Hi%2C+I+want+to+book+a+tour"

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
    def add_buttons():
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("🌐 Learn More", url=WEBSITE_URL),
            types.InlineKeyboardButton("📲 Book Now", url=WHATSAPP_URL)
        )
        return markup

    if call.data == 'tours':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🏙️ Baku City Tour", callback_data='baku_tour'),
            types.InlineKeyboardButton("🪨 Gobustan & Absheron", callback_data='gobustan'),
            types.InlineKeyboardButton("🏔 Shahdag Adventure", callback_data='shahdag'),
            types.InlineKeyboardButton("🌲 Gabala Day Trip", callback_data='gabala'),
            types.InlineKeyboardButton("🏛 Sheki Cultural Tour", callback_data='sheki'),
            types.InlineKeyboardButton("🍷 Shamakhi Wine", callback_data='shamakhi'),
            types.InlineKeyboardButton("📩 WhatsApp", url=WHATSAPP_URL),
            types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main')
        )
        bot.edit_message_text("Select a tour to learn more:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == 'transfers':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🛫 Airport ↔ Hotel", callback_data='airport'),
            types.InlineKeyboardButton("🚘 Round Trip Transfers", callback_data='roundtrip'),
            types.InlineKeyboardButton("🚖 VIP Vehicle Rental", callback_data='vip'),
            types.InlineKeyboardButton("📩 WhatsApp", url=WHATSAPP_URL),
            types.InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main')
        )
        bot.edit_message_text("Select a transfer option:", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data in ['packages', 'visa', 'hotels', 'support', 'about']:
        if call.data == 'packages':
            text = "🎉 **Group & Custom Packages**\n\nWhether it's family, friends, or corporate travel — we build packages tailored to your group size & preferences. Includes transportation, accommodation, guided tours, meals, and full support throughout your journey."
        elif call.data == 'visa':
            text = "🛂 **Visa Support**\n\nWe assist travelers in obtaining fast and reliable e-visas for Azerbaijan. Our team helps you through the process, document submission, and keeps you updated at every stage."
        elif call.data == 'hotels':
            text = "🏨 **Hotel Bookings**\n\nChoose from 3★ to 5★ hotels across Baku and regions. Central locations, scenic views, breakfast options, and great deals are part of every booking. We find what fits your budget and comfort."
        elif call.data == 'support':
            text = "💬 **Customer Support**\n\nWe’re here to help 24/7! Whether you have questions about tours, transfers, or booking – just reach out. Human support, no bots."
        elif call.data == 'about':
            text = "📖 **About Baku Life Tours**\n\nWe are a Baku-based travel agency providing trusted service since 2017. With 100,000+ happy travelers, our specialties include daily tours, airport transfers, hotel booking, visa help, and tailored group packages."
        markup = add_buttons()
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif call.data == 'main':
        send_start(call.message)

    # Turların geniş təsviri
    elif call.data == 'baku_tour':
        bot.send_message(call.message.chat.id, "🏙️ **Baku City Tour**\n\nDiscover the charm of Baku with our city tour that covers iconic landmarks such as Flame Towers, Highland Park, the historical Old City (Icherisheher), Maiden Tower, Nizami Street, and the stunning Baku Boulevard. Includes transport & guide.", reply_markup=add_buttons())
    elif call.data == 'gobustan':
        bot.send_message(call.message.chat.id, "🪨 **Gobustan & Absheron Tour**\n\nExplore ancient carvings, mud volcanoes at Gobustan, and visit Fire Temple and Burning Mountain in Absheron. Full-day cultural and natural exploration.", reply_markup=add_buttons())
    elif call.data == 'shahdag':
        bot.send_message(call.message.chat.id, "🏔 **Shahdag Mountain Adventure**\n\nEscape to the mountains! Skiing, cable cars, snow activities in winter or hiking & ATV rides in summer. Perfect for nature and thrill seekers.", reply_markup=add_buttons())
    elif call.data == 'gabala':
        bot.send_message(call.message.chat.id, "🌲 **Gabala Day Trip**\n\nNature-filled day visiting Nohur Lake, waterfalls, Tufandag resort, and local attractions. Relaxing atmosphere and fresh mountain air guaranteed.", reply_markup=add_buttons())
    elif call.data == 'sheki':
        bot.send_message(call.message.chat.id, "🏛 **Sheki Cultural Tour**\n\nExplore Sheki’s history: Khan Palace, Karvansaray, local cuisine and artisans. A beautiful town rich in tradition and culture.", reply_markup=add_buttons())
    elif call.data == 'shamakhi':
        bot.send_message(call.message.chat.id, "🍷 **Shamakhi Wine Experience**\n\nVisit local vineyards, enjoy tastings, cellar tours and traditional lunch. Scenic and serene journey through wine country.", reply_markup=add_buttons())
    elif call.data == 'airport':
        bot.send_message(call.message.chat.id, "🛫 **Airport ↔ Hotel Transfers**\n\n24/7 transfer from Heydar Aliyev Airport to any hotel in Baku. Meet & greet service, clean cars, multilingual drivers.", reply_markup=add_buttons())
    elif call.data == 'roundtrip':
        bot.send_message(call.message.chat.id, "🚘 **Round Trip Regional Transfers**\n\nRound-trip rides to Gabala, Sheki, Shahdag, and more. Safe, reliable, and comfortable with flexible pick-up times.", reply_markup=add_buttons())
    elif call.data == 'vip':
        bot.send_message(call.message.chat.id, "🚖 **VIP Vehicle Rental**\n\nPremium cars including V-Class, Sprinter, SUV with driver. Ideal for business travelers, events, delegations, and luxury clients.", reply_markup=add_buttons())

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
