import telebot
import requests
import os
import re
from flask import Flask
from threading import Thread

# --- SISTEMA PARA O RENDER NÃO DAR TIMEOUT (FLASK) ---
app = Flask('')

@app.route('/')
def home():
    # Esta mensagem confirma que o Render e o UptimeRobot estão alcançando o bot
    return "Bot Raposa Shopee Online! 🦊🚀", 200

def run():
    # O Render usa a porta 10000 por padrão
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def start_flask():
    t = Thread(target=run)
    t.daemon = True # Garante que a thread feche se o bot parar
    t.start()

# --- CONFIGURAÇÃO ---
# No Render, a variável deve ser TOKEN_BOT
TOKEN = os.environ.get("TOKEN_BOT")
ID_CANAL = "@raposaqueimaestoque" 

if not TOKEN:
    print("❌ ERRO: A variável TOKEN_BOT não foi encontrada!")

bot = telebot.TeleBot(TOKEN)

# --- LÓGICA DE POSTAGEM ---
@bot.message_handler(func=lambda message: True)
def processar_links(message):
    texto = message.text.lower()
    
    try:
        # Limpa o link removendo rastreadores após o '?'
        link_match = re.search(r'(https?://[^\s]+)', message.text)
        if not link_match:
            return
            
        link_original = link_match.group(0)
        link_limpo = link_original.split('?')[0]

        # Identifica se é Shopee ou Mercado Livre
        if "shope.ee" in texto or "shopee.com.br" in texto:
            msg = f"🦊 *ACHADO NA SHOPEE!* 🛍️\n\n👉 {link_limpo}\n\n#Shopee #Ofertas"
            bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado na Shopee!")

        elif "mercadolivre.com.br" in texto or "mlb.io" in texto or "meli.la" in texto:
            msg = f"🦊 *OFERTA NO MERCADO LIVRE!* 📦\n\n👉 {link_limpo}\n\n#ML #Promo"
            bot.send_message(ID_CANAL, msg, parse_mode="Markdown")
            bot.reply_to(message, "✅ Postado no Mercado Livre!")

    except Exception as e:
        print(f"Erro ao postar: {e}")

# --- EXECUÇÃO COM LIMPEZA DE CONFLITO ---
if __name__ == "__main__":
    # 1. Inicia o servidor para o UptimeRobot ficar verde
    start_flask()
    
    try:
        # 2. Remove webhooks antigos para evitar Erro 409
        bot.remove_webhook()
        print(f"🚀 Bot Shopee Iniciado com Sucesso!")
        
        # 3. Inicia o polling ignorando mensagens enviadas enquanto estava OFF
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(f"❌ Erro fatal no bot: {e}")
