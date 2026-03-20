import telebot
import os
from flask import Flask
import threading

# --- WEB SERVER PARA MANTER VIVO ---
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Shopee Online", 200

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÃO DO BOT ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar(message):
    link = message.text
    print(f"Recebi isso aqui: {link}") # Isso vai aparecer nos logs da Render
    
    if "shopee" in link.lower() or "shope.ee" in link.lower():
        legenda = (
            "🟠 **OFERTA SHOPEE!** 🟠\n"
            "➖➖➖➖➖➖➖➖➖➖\n\n"
            f"🛒 **Compre aqui:** {link}\n\n"
            "🚚 *Confira se há cupons de frete grátis!*"
        )
        try:
            bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
            bot.reply_to(message, "✅ Enviado para o canal!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao postar. Verifique se sou ADM do canal!\nErro: {e}")
    else:
        bot.reply_to(message, "⚠️ Por favor, mande um link da Shopee.")

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    bot.polling(none_stop=True)
