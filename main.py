import telebot
import os
from flask import Flask
from threading import Thread

# Configuração do Flask para a Render não desligar
app = Flask('')

@app.route('/')
def home():
    return "Bot está vivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÃO DO BOT ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def msg_recebida(message):
    texto = message.text
    if "shopee" in texto.lower() or "shope.ee" in texto.lower():
        msg = f"🟠 **OFERTA SHOPEE!** 🟠\n\n🛒 **Compre aqui:** {texto}"
    else:
        msg = texto
    
    try:
        bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
        bot.reply_to(message, "✅ Postado!")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro: {e}")

if __name__ == "__main__":
    keep_alive() # Inicia o servidor web
    print("Bot rodando...")
    bot.infinity_polling() # Mantém o bot verificando mensagens
