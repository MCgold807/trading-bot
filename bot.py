from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8600637053:AAGcSsK1TJtLQi0dCDGfAHspl2JY3CoNDsQ"
CHAT_ID = "-1003820822526"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None or update.message.text is None:
        return

    text = update.message.text

    try:
        parts = text.split()
        tipo = parts[0]
        entry = parts[1]
        sl = parts[2]
        tp1 = parts[3]
        tp2 = parts[4]
        tp3 = parts[5]

        message = f"""🔥 XAUUSD {tipo}

📍 Entry: {entry}
🛑 SL: {sl}

🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}

⚡ Setup automatico"""

        await context.bot.send_message(chat_id=CHAT_ID, text=message)

    except:
        await update.message.reply_text("Formato sbagliato ❌")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
