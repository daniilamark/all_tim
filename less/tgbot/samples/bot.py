# pip install pytelegrambotapi
import telebot

TOKEN = '2051890311:AAHowOj3tQJVxD8Go6yTP1c1oQHpZ-JmufI'

def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            # text = "hek"
            tb.send_message(chatid, text)


tb = telebot.TeleBot(TOKEN)
tb.set_update_listener(listener) #register listener
tb.polling()
#Use none_stop flag let polling will not stop when get new message occur error.
tb.polling(none_stop=True)
# Interval setup. Sleep 3 secs between request new message.
tb.polling(interval=3)