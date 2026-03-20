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
TOKEN = "COLOQUE_SEU_TOKEN_AQUI" # Certifique-se que é o token do bot da Shopee!
ID_CANAL = "-1002581284569"
MEU_ID = 6599857002

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar(message):
    # Log para você ver no console da Render se ele recebeu algo
    print(f"Mensagem recebida: {message.text}")
    
    if message.chat.id == MEU_ID:
        link = message.text
        if "shopee" in link.lower():
            legenda = (
                "🟠 **OFERTA SHOPEE!** 🟠\n"
                "➖➖➖➖➖➖➖➖➖➖\n\n"
                f"🛒 **Compre aqui:** {link}\n\n"
                "🚚 *Confira se há frete grátis disponível!*"
            )
            try:
                bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
                bot.reply_to(message, "✅ Postado no canal com sucesso!")
            except Exception as e:
                bot.reply_to(message, f"❌ Erro ao postar: {e}")
        else:
            bot.reply_to(message, "⚠️ Mande um link válido da Shopee!")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    bot.polling(none_stop=True)
