from telegram.ext import Updater, CommandHandler

# Define a function to get the chat ID
def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=f"Your Chat ID is: {chat_id}")

# Initialize the updater and dispatcher
updater = Updater('AAHImfidXzyhGsGdYZn87-z3ZY_KWf3Dzec')  # Replace with your bot token
dispatcher = updater.dispatcher

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))

# Start the bot
updater.start_polling()
updater.idle()
