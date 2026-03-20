import telebot
import os
from flask import Flask
from threading import Thread

# --- SERVIDOR PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): 
    return "Bot Shopee Raposa Ativo!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÃO ---
TOKEN = "8722324715:AAFBGt_Q5laJqxjuv9fnQaImL-7z88zYPjo"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar_shopee(message):
    link = message.text.strip()
    
    # Verifica se o link é da Shopee
    if "shopee" in link.lower() or "shope.ee" in link.lower():
        legenda = (
            "🔥 **OFERTA RELÂMPAGO SHOPEE!** 🔥\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
            "💰 **O PREÇO BAIXOU MUITO!**\n"
            "👉 *Confira o valor atualizado no link abaixo:*\n\n"
            f"🛒 **COMPRE AQUI:** {link}\n\n"
            "🚚 *Dica: Use o cupom de Frete Grátis no App!*"
        )
        
        try:
            bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado na Toca da Raposa!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao postar: {e}")

if __name__ == "__main__":
    keep_alive()
    print("Bot Shopee Online!")
    bot.infinity_polling()
