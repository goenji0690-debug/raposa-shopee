import telebot
import requests
import os
from flask import Flask
from threading import Thread

# --- SISTEMA PARA O RENDER NÃO DAR TIMEOUT (FLASK) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Shopee Online! 🦊🛍️"

def run():
    # O Render fornece a porta automaticamente, mas usamos 8081 como padrão se local
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port)

def start_flask():
    t = Thread(target=run)
    t.start()

# --- CONFIGURAÇÕES DA SHOPEE ---
# IMPORTANTE: Usei o token da Shopee que você passou (8722...)
TOKEN_SHOPEE = "8722324715:AAEb8rcwcXD95jEInrj7WmWDXfhukTteRVk"
ID_CANAL_OFERTAS = "@raposaqueimaestoque" 

bot = telebot.TeleBot(TOKEN_SHOPEE)

@bot.message_handler(func=lambda message: "shope.ee" in message.text or "shopee.com.br" in message.text)
def processar_link_shopee(message):
    link_original = message.text
    
    try:
        # Aqui vai a sua lógica de conversão da Shopee (Link de Afiliado)
        # Por enquanto, ele apenas reposta o link limpo
        link_final = link_original.split('?')[0] 

        texto_canal = (
            "🦊 *ACHADO NA SHOPEE!* 🛍️\n\n"
            f"👉 {link_final}\n\n"
            "#Shopee #Ofertas #Raposa"
        )
        bot.send_message(ID_CANAL_OFERTAS, texto_canal, parse_mode="Markdown")
        bot.reply_to(message, "✅ Postado na Shopee com sucesso!")

    except Exception as e:
        bot.reply_to(message, f"❌ Erro Shopee: {e}")

# --- EXECUÇÃO DO BOT ---
if __name__ == "__main__":
    start_flask() # Inicia o servidor web para o Render ficar feliz
    print("🚀 Raposa Shopee Ativa!")
    bot.infinity_polling()
