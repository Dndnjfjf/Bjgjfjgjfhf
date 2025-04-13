import telebot
from telebot import types
import requests
from googletrans import Translator

bot_token = input("أدخل توكن البوت الخاص بك: ")
bot = telebot.TeleBot(bot_token)

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'origin': 'https://www.writecream.com',
    'priority': 'u=1, i',
    'referer': 'https://www.writecream.com/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

translator = Translator()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    channel_button = types.InlineKeyboardButton("رابط القناة", url="https://t.me/+KzydxjYyLZNiMzNi")
    group_button = types.InlineKeyboardButton("رابط الكروب", url="https://t.me/cu_cccu")
    markup.add(channel_button)
    markup.add(group_button)
    bot.reply_to(message, f"مرحبا! أنا بوت يرسل صور بناء على وصفك.\n\nالمطور: @vipQvip", reply_markup=markup)
    bot.send_message(message.chat.id, "الآن، أرسل لي وصفًا للصورة باللغة الإنجليزية وسأقوم بإرسال الصورة.") 


@bot.message_handler(func=lambda message: True)
def get_description(message):
    if message.text.startswith('/'):  
        return

    try:
        translated_text = message.text

        params = {
            'prompt': translated_text,
            'aspect_ratio': 'Select Aspect Ratio',
            'link': 'writecream.com',
        }

        response = requests.get(
            'https://1yjs1yldj7.execute-api.us-east-1.amazonaws.com/default/ai_image',
            params=params,
            headers=headers,
        )

        bot.send_message(message.chat.id, f"تم إرسال الوصف: {translated_text}") 
        bot.send_message(message.chat.id, response.text)  

    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ: {str(e)}")


bot.infinity_polling()