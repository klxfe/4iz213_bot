import telebot, wikipedia, re
from telebot import types
import config
# Создаем экземпляр бота
TOKEN = '5122118095:AAFz88KtYG1uOQ80tmnZC9IdAWK5tPXCn0w'
bot = telebot.TeleBot(TOKEN)
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("en")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Více o mně", url='https://drive.google.com/file/d/1bVuW4Wd5CHUk0lOfzo3hEVg14ndz1cxE/view?usp=sharing')
    markup.add(button1)

    button2 = types.InlineKeyboardButton("Více o mně", url='https://drive.google.com/file/d/1bVuW4Wd5CHUk0lOfzo3hEVg14ndz1cxE/view?usp=sharing')
    markup.add(button2)

    bot.send_message(m.chat.id,
                     "Ahoj, {0.first_name}! Tohle je bot,který ti pomůže najít správnou hru pro sebe)".format(m.from_user),
                     reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
# Запускаем бота
bot.polling(none_stop=True, interval=0)