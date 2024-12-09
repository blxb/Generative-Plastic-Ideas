import telebot
import random

bot = telebot.TeleBot("your token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am a Бот с идеями для поделок из бытового пластика.")
    
@bot.message_handler(commands=['craft'])
def send_welcome(message):
    craft_ideas = [
        "Горшки для растений",
        "Органайзеры",
        "Люстра или абажур",
        "Декоративные цветы",
        "Птичья кормушка"
    ]
    bot.send_message(message.chat.id, f"here is an idea for you: {random.choice(craft_ideas)}")
    
bot.polling()
