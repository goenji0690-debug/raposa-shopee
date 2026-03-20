import telebot
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot de Ofertas Shopee Ativo!"

def run():
    # A Render exige a porta 10000 por padrão em muitos casos
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÃO ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"
# Teu ID que garante a comissão (visto no teu link de exemplo)
MEU_ID_AFILIADO = "AUpPs68ZBd"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def msg_recebida(message):
    link_original = message.text.strip()
    
    if "shopee" in link_original.lower() or "shope.ee" in link_original.lower():
        # Se mandares um link curto da shopee, ele apenas posta. 
        # O ideal é mandares o link já convertido pelo app para não haver erro de comissão.
        legenda = (
            "🔥 **OFERTA RELÂMPAGO SHOPEE!** 🔥\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
            "💰 **CONFIRA O PREÇO NO LINK!**\n\n"
            f"🛒 **COMPRE AQUI:** {link_original}\n\n"
            "🚚 *Dica: Use o cupom de Frete Grátis!*"
        )
        
        try:
            bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado com Sucesso!")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao enviar: {e}")

if __name__ == "__main__":
    keep_alive()
    print("Bot Ligado!")
    bot.infinity_polling()
