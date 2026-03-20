import telebot
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot de Ofertas Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÃO ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def msg_recebida(message):
    texto_recebido = message.text
    
    # Se você mandar "link, preço", ele separa os dois
    if "," in texto_recebido:
        partes = texto_recebido.split(",")
        link = partes[0].strip()
        preco = partes[1].strip()
    else:
        link = texto_recebido.strip()
        preco = "Confira no site!" # Texto padrão se você esquecer o preço

    if "shopee" in link.lower() or "shope.ee" in link.lower():
        legenda = (
            "🔥 **TOCA DA RAPOSA - OFERTA SHOPEE** 🔥\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
            f"💰 **PREÇO: R$ {preco}**\n\n"
            f"🛒 **COMPRE AQUI:** {link}\n\n"
            "🚚 *Use o cupom de Frete Grátis no App!*"
        )
        
        try:
            bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
            bot.reply_to(message, f"✅ Postado com preço R$ {preco}!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro: {e}")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
