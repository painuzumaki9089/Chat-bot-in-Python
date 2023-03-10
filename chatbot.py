#pip install pyTelegramBotApi
import telebot 
import time

bot = telebot.TeleBot('your bot token')
@bot.message_handler(commands = ['start'])
def start_message(message):
   bot.reply_to(message, 'hello')
@bot.message_handler(content_types = ['text'])
def send_message(message)
   if message.text.lower()== 'hello':
    bot.send_message(message.chat.id, 'hello im bot')
   elif message.text.lower()== 'how are you?')
    bot.send_message(message.chat.id, 'im okay')
    time.sleep(1)
    bot.send_message(message.chat.id, 'and how are you?')
    
    
    
    
bot.polling(none_stop = True)
