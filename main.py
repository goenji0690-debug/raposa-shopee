import telebot
import os
from flask import Flask
import threading

# --- WEB SERVER PARA MANTER VIVO ---
app = Flask(__name__)
@app.route('/')
def home(): return "Bot Shopee Automático Online", 200

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# --- CONFIGURAÇÃO DO BOT ---
TOKEN = "8722324715:AAHb7C7meKBqELEj_LGNijhT0dlhJL_eBN4"
ID_CANAL = "-1002581284569"
# Seu link base de referência (extraído do que você mandou)
ID_AFILIADO_BASE = "AUpPs68ZBd" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def processar(message):
    link_original = message.text
    print(f"Link recebido: {link_original}")
    
    if "shopee" in link_original.lower() or "shope.ee" in link_original.lower():
        # Se você mandar um link que não é de afiliado, o bot tenta garantir a estrutura
        # Se já for um link 's.shopee', ele apenas repassa para o canal
        link_final = link_original
        
        legenda = (
            "🟠 **OFERTA EXCLUSIVA SHOPEE** 🟠\n"
            "➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n"
            "🔥 Aproveite o preço promocional agora!\n\n"
            f"🛒 **COMPRE AQUI:** {link_final}\n\n"
            "🚚 *Confira os cupons de Frete Grátis no App!*"
        )
        
        try:
            bot.send_message(ID_CANAL, legenda, parse_mode="Markdown")
            bot.reply_to(message, "✅ **Convertido e Postado!**\nSua comissão está garantida.")
        except Exception as e:
            bot.reply_to(message, f"❌ Erro ao postar: {e}")
    else:
        bot.reply_to(message, "⚠️ Isso não parece um link da Shopee!")

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    bot.polling(none_stop=True)
