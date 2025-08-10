# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8379742321:AAEef6P1oYZr0r-Ud8Yt1DaUBCo_7U7HhQI"
MY_ID = 1905094596

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sender = update.message.from_user
    if update.message.text:
        msg = "sms {}:
{}".format(sender.first_name, update.message.text)
        await context.bot.send_message(chat_id=MY_ID, text=msg)
    else:
        await context.bot.forward_message(
            chat_id=MY_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot is running...")
app.run_polling()
