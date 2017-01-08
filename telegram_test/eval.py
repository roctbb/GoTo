import telebot,time
from threading import Thread

token = "305642538:AAH7MwaSKJaWJ73FA0TqQx5Np_-GKvXOucs"

bot = telebot.TeleBot(token)

users = set()

@bot.message_handler(commands=['spam'])
def handle_start_spam(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Спамим корочь")

@bot.message_handler(commands=['stop'])
def handle_stop_spam(message):
    users.remove(message.chat.id)
    bot.send_message(message.chat.id, " Ок, без вопросов")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        result = eval(message.text)
        bot.send_message(message.chat.id, str(result))
    except:
        bot.send_message(message.chat.id, "Наркоман штолле?")

def spam():
    global users
    while True:
        for user in users:
            bot.send_message(user, "Берем сироп вишневый!")
        time.sleep(5)
def polling():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    thread = Thread(target=spam)
    thread.start()
    thread1 = Thread(target=polling)
    thread1.start()
