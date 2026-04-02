import telebot
import requests
import os
from flask import Flask
from threading import Thread

# --- SISTEMA PARA O RENDER NÃO DAR TIMEOUT (FLASK) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Raposa Online! 🦊🚀"

def run():
    # O Render fornece a porta automaticamente, o padrão é 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def start_flask():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÃO AUTOMÁTICA ---
# IMPORTANTE: No Render, vá em 'Environment' e adicione a Key: TOKEN_BOT
TOKEN = os.environ.get("TOKEN_BOT")
ID_CANAL = "@raposaqueimaestoque" 

if not TOKEN:
    print("❌ ERRO: A variável TOKEN_BOT não foi encontrada no Render!")

bot = telebot.TeleBot(TOKEN)

# --- LÓGICA DE FILTRO (SHOPEE E MERCADO LIVRE) ---
@bot.message_handler(func=lambda message: True)
def processar_links(message):
    texto = message.text.lower()
    
    try:
        # Se for link da Shopee
        if "shope.ee" in texto or "shopee.com.br" in texto:
            link_final = message.text.split('?')[0]
            msg = f"🦊 *ACHADO NA SHOPEE!* 🛍️\n\n👉 {link_final}\n\n#Shopee #Ofertas"
            bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado na Shopee!")

        # Se for link do Mercado Livre
        elif "mercadolivre.com.br" in texto or "mlb.io" in texto:
            link_final = message.text.split('?')[0]
            msg = f"🦊 *OFERTA NO MERCADO LIVRE!* 📦\n\n👉 {link_final}\n\n#ML #Promo"
            bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado no Mercado Livre!")

    except Exception as e:
        print(f"Erro ao postar: {e}")

# --- EXECUÇÃO ---
if __name__ == "__main__":
    start_flask()
    print(f"🚀 Bot Iniciado com Sucesso!")
    bot.infinity_polling()
