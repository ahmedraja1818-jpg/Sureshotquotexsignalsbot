from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SureShot Quotex Signals\n\n"
        "Bot successfully connected ✅\n\n"
        "Commands:\n"
        "/signal - Latest demo signal\n"
        "/stats - Signal statistics\n"
        "/help - Help"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SURESHOT SIGNAL\n\n"
        "💱 EUR/USD\n"
        "📈 CALL\n"
        "⏱ 1 MIN\n"
        "⭐ Demo Signal\n\n"
        "⚠️ Research/testing only. No guaranteed profit."
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 SIGNAL STATISTICS\n\n"
        "Total Signals: 0\n"
        "Wins: 0\n"
        "Losses: 0\n"
        "Accuracy: 0%\n\n"
        "Live statistics will be added later."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/signal - Get signal\n"
        "/stats - View statistics\n"
        "/help - Help"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("help", help_command))

print("SureShot Signal Bot is running...")

app.run_polling()
