import telebot
import os
from flask import Flask
from threading import Thread

# --- SERVIDOR WEB PARA A RENDER MANTER O BOT VIVO ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Shopee Raposa Online!"

def run():
    # A Render exige o uso de uma porta dinâmica
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- CONFIGURAÇÃO DO BOT (TOKEN ATUALIZADO) ---
TOKEN = "8722324715:AAFBGt_Q5laJqxjuv9fnQaImL-7z88zYPjo"
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

# --- PROCESSAMENTO DAS MENSAGENS ---
@bot.message_handler(func=lambda m: True)
def processar_shopee(message):
    link = message.text.strip()
    
    # Verifica se o link enviado é da Shopee
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
            bot.reply_to(message, f"❌ Erro ao postar no canal: {e}")
    else:
        bot.reply_to(message, "⚠️ Por favor, envie um link válido da Shopee.")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    keep_alive() # Inicia o servidor Flask em segundo plano
    print("Bot Raposa Shopee Iniciado com sucesso!")
    # O bot infinity_polling mantém o robô escutando o Telegram
    bot.infinity_polling()
