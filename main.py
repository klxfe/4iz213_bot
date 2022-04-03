import telebot, wikipedia, re
from telebot import types
import config
# Zakládání objektu bot
TOKEN = '5122118095:AAFz88KtYG1uOQ80tmnZC9IdAWK5tPXCn0w'
bot = telebot.TeleBot(TOKEN)
# Nastavení jazyku angličtina pro Wikipedii
wikipedia.set_lang("en")


#funkce getwiki - vrati nam část článku z wikipedii podle slova
#jde vyhledávání článku, jeho omezení a formatování
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):

                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'Na Wikipedii není informace o teto hře'


# Zpracování příkazu /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Chci top her")
    btn2 = types.KeyboardButton("👋 Zdravim")
    btn3 = types.KeyboardButton("❓ Otazky ohledně mně")
    markup.add(btn1, btn2, btn3)


    bot.send_message(m.chat.id,
                     "Ahoj, {0.first_name}! Tohle je bot,který ti pomůže najít správnou hru pro sebe 🎉".format(m.from_user),
                     reply_markup=markup)


# Ziskání zprávy od uživatele
@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text == "❓ Otazky ohledně mně":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Co bych měl umět", url='https://drive.google.com/file/d/1bVuW4Wd5CHUk0lOfzo3hEVg14ndz1cxE/view?usp=sharing')
        markup.add(button1)

        button2 = types.InlineKeyboardButton("Link na GitHub", url='https://github.com/klxfe/4iz231_bot')
        markup.add(button2)
        bot.send_message(message.chat.id, text="Více o mně se dozvíš zde", reply_markup=markup)

    elif message.text == "Chci top her":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Aktuální seznam top pc her 2022 najdeš zde -> ",
                                             url='https://www.pcgamesn.com/new-pc-games')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Aktuální seznam top pc her 2022 najdeš zde ->", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, getwiki(message.text))


# Start bota
bot.polling(none_stop=True, interval=0)