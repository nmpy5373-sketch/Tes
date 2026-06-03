from openai import OpenAI
import telebot

BOT_TOKEN = "8021926353:AAHA920HQfWTMwkbqlnfLFG9Ptn8Tn4KMWM"
OPENAI_API_KEY = "AQ.Ab8RN6KWclxJXCUbCWe4DbpJU87tiCD-yIvCtZefxswYphQDtw"

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

@bot.message_handler(func=lambda m: True)
def ai_chat(message):
    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=message.text
        )
        bot.reply_to(message, response.output_text)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()