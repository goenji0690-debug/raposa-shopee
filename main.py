import telebot
import os
from flask import Flask
from threading import Thread

# Configuração do Servidor para a Render não derrubar o bot
app = Flask('')
@app.route('/')
def home(): 
    return "Bot Shopee Ativo", 200

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÃO ---
# Ele tenta pegar o token da Render primeiro (TOKEN_BOT), se não achar, usa o seu fixo.
TOKEN = os.environ.get('TOKEN_BOT', "8722324715:AAEb8rcwcXD95jEInrj7WmWDXfhukTteRVk")
ID_CANAL = "-1002581284569"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar_shopee(message):
    link = message.text.strip()
    # Verifica se o link é da Shopee
    if "shopee" in link.lower() or "shp.ee" in link.lower() or "shope.ee" in link.lower():
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
            bot.reply_to(message, "✅ Postado no Canal da Raposa (Shopee)!")
        except Exception as e:
            print(f"Erro ao postar: {e}")
            bot.reply_to(message, "❌ Erro ao postar. Verifique se sou admin do canal.")

if __name__ == "__main__":
    t = Thread(target=run)
    t.daemon = True
    t.start()
    
    print("🛍️ BOT SHOPEE LIGADO!")
    bot.infinity_polling()
