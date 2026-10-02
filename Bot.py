import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

# Render کے لیے چھوٹا web server
web = Flask(__name__)

@web.route("/")
def home():
    return "SureShot Quotex Signal Bot is running!"

@web.route("/health")
def health():
    return "OK"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SureShot Quotex Signals\n\n"
        "Bot connected successfully ✅\n\n"
        "/signal - Get demo signal\n"
        "/stats - View statistics\n"
        "/help - Help"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SURESHOT SIGNAL\n\n"
        "💱 EUR/USD\n"
        "📈 CALL\n"
        "⏱ 1 MIN\n"
        "⭐ Demo Signal\n\n"
        "⚠️ Research/testing only.\n"
        "No guaranteed profit."
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SIGNAL STATISTICS\n\n"
        "Total Signals: 0\n"
        "Wins: 0\n"
        "Losses: 0\n"
        "Accuracy: 0%"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/signal - Get signal\n"
        "/stats - Statistics\n"
        "/help - Help"
    )

async def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("help", help_command))

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()

    import asyncio
    asyncio.run(run_bot())

    # process کو چلتا رکھیں
    threading.Event().wait()
