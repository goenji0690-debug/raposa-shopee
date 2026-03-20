import telebot
import os
from flask import Flask
from threading import Thread

# --- SERVIDOR WEB ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Shopee Raposa Ativo!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- CONFIGURAÇÃO (TOKEN NOVO) ---
TOKEN = "8722324715:AAEb8rcwcXD95jEInrj7WmWDXfhukTteRVk"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

# --- LÓGICA DAS OFERTAS ---
@bot.message_handler(func=lambda m: True)
def processar_shopee(message):
    link = message.text.strip()
    
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
            bot.reply_to(message, "✅ Postado com sucesso na Toca da Raposa!")
        except Exception as e:
            print(f"Erro ao postar: {e}")

if __name__ == "__main__":
    keep_alive()
    print("Bot Raposa Online com Token Novo!")
    bot.infinity_polling()
