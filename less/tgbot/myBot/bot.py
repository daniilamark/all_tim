from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Бот запущен. Нажмите Ctrl+C для завершения")

def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")

def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text)
		rate = 80.34
		soms = number * rate
		context.bot.send_message(chat_id=chat.id, text=str(soms) + " сом")
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")

token = "2051890311:AAHowOj3tQJVxD8Go6yTP1c1oQHpZ-JmufI"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()