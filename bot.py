import telebot
import config
import time

flood = False
text = config.text
expecting_text = False
if len(config.TOKENS) == 1:
    bot1 = telebot.TeleBot(config.TOKENS[0])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 2:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 3:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 4:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 5:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 6:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])
    bot6 = telebot.TeleBot(config.TOKENS[5])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot6.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 7:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])
    bot6 = telebot.TeleBot(config.TOKENS[5])
    bot7 = telebot.TeleBot(config.TOKENS[6])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot6.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot7.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 8:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])
    bot6 = telebot.TeleBot(config.TOKENS[5])
    bot7 = telebot.TeleBot(config.TOKENS[6])
    bot8 = telebot.TeleBot(config.TOKENS[7])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot6.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot7.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot8.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 9:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])
    bot6 = telebot.TeleBot(config.TOKENS[5])
    bot7 = telebot.TeleBot(config.TOKENS[6])
    bot8 = telebot.TeleBot(config.TOKENS[7])
    bot9 = telebot.TeleBot(config.TOKENS[8])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot6.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot7.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot8.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot9.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
elif len(config.TOKENS) == 10:
    bot1 = telebot.TeleBot(config.TOKENS[0])
    bot2 = telebot.TeleBot(config.TOKENS[1])
    bot3 = telebot.TeleBot(config.TOKENS[2])
    bot4 = telebot.TeleBot(config.TOKENS[3])
    bot5 = telebot.TeleBot(config.TOKENS[4])
    bot6 = telebot.TeleBot(config.TOKENS[5])
    bot7 = telebot.TeleBot(config.TOKENS[6])
    bot8 = telebot.TeleBot(config.TOKENS[7])
    bot9 = telebot.TeleBot(config.TOKENS[8])
    bot10 = telebot.TeleBot(config.TOKENS[9])

    def flooding(message_id):
        bot1.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot2.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot3.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot4.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot5.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot6.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot7.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot8.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot9.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))
        bot10.send_message(message_id, text)
        time.sleep(2.5/len(config.TOKENS))


@bot1.message_handler(commands=['start'])
def answer(message):
    global flood, text
    flood = True
    while flood:
        flooding(message.chat.id)


@bot1.message_handler(commands=['stop'])
def answer(message):
    global flood
    flood = False
    while flood:
        flooding(message.chat.id)


@bot1.message_handler(commands=['text'])
def answer(message):
    global expecting_text
    bot1.send_message(message.chat.id, 'Enter the text:')
    expecting_text = True


@bot1.message_handler(content_types=['text'])
def answer(message):
    global text
    global expecting_text
    if expecting_text:
        text = message.text
        bot1.send_message(message.chat.id, 'Now text is ' + text)


while 1:
    bot1.polling(none_stop=True)
