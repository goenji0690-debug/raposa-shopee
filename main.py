import telebot
import os
import threading
from flask import Flask

# --- CONFIGURAÇÃO DO WEB SERVER ---
app = Flask(__name__)
@app.route('/')
def home(): return "Raposa Shopee Online", 200

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÃO DO BOT (COLOQUE SEUS DADOS) ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569" 
MEU_ID = 6599857002

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar(message):
    if message.chat.id == MEU_ID:
        link = message.text
        if "shopee.com.br" in link or "shope.ee" in link:
            msg = f"🟠 **OFERTA SHOPEE** 🟠\n\n🛒 **Compre aqui:** {link}"
            bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado na Shopee!")
        else:
            bot.reply_to(message, "🦊 Mande um link da Shopee!")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.polling(none_stop=True)
