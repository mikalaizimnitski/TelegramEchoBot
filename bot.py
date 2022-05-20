import config
import telebot
import datetime

bot = telebot.TeleBot(config.TOKEN)
#Присваивание токена

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    #bot.send_message(message.chat.id, message.text)
    time_shift = 10800
    bot.send_message(message.chat.id, f'\nID чата: {message.chat.id}'
                                      f'\nID пользователя: {message.from_user.id}'
                                      f'\nИмя: {message.from_user.first_name}'
                                      f'\nФамилия: {message.from_user.last_name}'
                                      f'\nПсевдоним: {message.from_user.username}'
                                      f'\nТип чата: {message.chat.type}'
                                      f'\nИдентификатор сообщения: {message.id}'
                                      f'\nТип контента сообщения: {message.content_type}'
                                      f'\n\nТекст сообщения: {message.text}'
                                      f'\nДата отправленного сообщения: {datetime.datetime.utcfromtimestamp(message.date + time_shift)}')
    #print("hello there")
#Функция повтора сообщений

bot.polling(none_stop=True)
#Цикл