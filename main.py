import telebot
# zakladani objektu "bot"
bot = telebot.TeleBot('5122118095:AAFz88KtYG1uOQ80tmnZC9IdAWK5tPXCn0w')

@bot.message_handler(content_types=['text'])

def text(message):
    bot.send_message(message.chat.id, 'Hello, World!')



bot.polling()