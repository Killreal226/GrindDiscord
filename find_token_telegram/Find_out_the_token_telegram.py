import telebot
token_telegram_bot = '5203497261:AAEC68-h7YtybJtdP0hCZIzxM6zS3hxXtMs'
bot = telebot.TeleBot (token_telegram_bot)
@bot.message_handler()
def get_id (message):
    if message.text == 'id':
        bot.send_message (message.chat.id, f'Твой id: {message.from_user.id}')
bot. polling (none_stop = True)
