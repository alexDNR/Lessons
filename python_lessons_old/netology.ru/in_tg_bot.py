import telebot
token = "2142858528:AAECL073hB_663BZGbQ6zWCCFv6tc9dGmq0"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, 'здаров')


bot.polling(none_stop=True) # постоянно обращается к серверу ТГ
