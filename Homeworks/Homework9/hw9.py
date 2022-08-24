import GigaBot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Lets rock!')

def echo_all(message):
	updater.reply_to(message, message.text)

def UserMessage(update: Update, context: CallbackContext):
    if (update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    else:
        try:
            update.message.reply_text(eval(update.message.text))
        except:
            update.message.reply_text("Не понятно")


updater = Updater(GigaBot.token())

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))

print('server start')
updater.start_polling()
updater.idle()