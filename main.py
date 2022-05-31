from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests, json


updater = Updater("5541235735:AAEQdvzPXC-IjCZYiOnNKbCzO5pZ2LBDiRQ",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""Hello Welcome This Is Bot Made By Akash. Currently Under Development\
		/help to see the commands available.
		/quote for a random quote.""")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands.
		/youtube
		/help
		/quote

		Maybe More In Future.""")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("My Channel Link , Subscribe It\
	https://www.youtube.com/channel/UCgNLt08ze6NaZ3uMDLLN3RA?sub_confirmation=1")

def quote(update: Update, context: CallbackContext):
	url = "https://api.quotable.io/random?tags=wisdom,friendship"
	response = requests.get(url)
	json_data = response.json()
	update.message.reply_text(json_data["content"])
	update.message.reply_text("Author : "+json_data["author"])
	update.message.reply_text("click /quote for more")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)
	update.message.reply_text("""Type /help For Help
		or /quote For a Random Quote.
		""")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('quote', quote))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
