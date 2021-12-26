import os
from telegram import update
from telegram.ext import Updater, MessageHandler, Filters, handler
from telegram.ext.filters import UpdateFilter


def process_message(update, context):

    text = update.message.text

    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='-1001203865577',
            text=str(text).replace('#channel', '')
        )


if __name__ == '__main__':

    updater = Updater(
        token=os.environ['5051406874:AAFDWsR6U1TZQgfHDYeUNzlJn1R1cm3tPb4'], use_context=True)
 
     
    dp = Updater
    dp.add_handler(MessageHandler(
        filters=Filters.text, callback=process_message))
        
    update.Update.start_polling()

    print('Bot is polling')

    update.idle()
