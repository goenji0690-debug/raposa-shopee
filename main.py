import telebot
import os
from flask import Flask
import threading

# --- SERVIDOR PARA A RENDER NÃO DORMIR ---
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Online", 200

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÃO DIRETA ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar_tudo(message):
    texto = message.text
    print(f"Recebi: {texto}") # Aparecerá nos logs da Render
    
    # Se tiver shopee no link, ele formata. Se não, posta o texto puro.
    if "shopee" in texto.lower() or "shope.ee" in texto.lower():
        legenda = f"🟠 **OFERTA SHOPEE!** 🟠\n\n🛒 **Compre aqui:** {texto}"
    else:
        legenda = texto

    try:
        bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
        bot.reply_to(message, "✅ POSTADO NO CANAL!")
    except Exception as e:
        bot.reply_to(message, f"❌ ERRO: {e}\n\nVerifique se o bot é ADM do canal {ID_CANAL}")

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print("Bot iniciando...")
    bot.polling(none_stop=True)
