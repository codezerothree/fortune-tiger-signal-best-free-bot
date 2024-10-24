import requests
import time
import telebot
import random 

api_key = 'API TOKEN TELEGRAM BOT' # Token do seu bot
chat_id = 'CHAT ID' # ID do Grupo ou Canal
bot = telebot.TeleBot(api_key)

# Links
LINK_SITE = 'https://t.me/luigiferraribot?start=bot_de_sinais_ft' # Link de afiliado
LINK_GRUPO = 'https://t.me/luigiferraribot?start=bot_de_sinais_ft' # Link do Grupo ou Canal VIP

# Mensagens
mens_ini = f'''
<i>Recebendo sinal...</i>
'''

mens2 = f'''
🏆⚡️ 𝗘𝗡𝗧𝗥𝗘 𝗣𝗔𝗥𝗔 𝗢 𝗩𝗜𝗣 ⚡️🏆

🚀 <b>Dicas e Estratégias</b> ✓
🚀 <b>Video Aulas na Prática</b> ✓
🚀 <b>100% Garantido</b> ✓
'''

mens3 = f'''
⏱ <i>Próximo sinal em <b>5 min</>...</i>
'''

mens_ini_id = None
mens3_id = None

def signal_1():
    global mens3_id, mens_ini_id
    
    number_aleat1 = random.randint(1, 20)
    number_aleat2 = random.randint(1, 20)
    
    mens1 = f'''
🧿 𝗦𝗜𝗡𝗔𝗟 𝗜𝗗𝗘𝗡𝗧𝗜𝗙𝗜𝗖𝗔𝗗𝗢! ✅

🎁 [𝗖𝗔𝗗𝗔𝗦𝗧𝗥𝗘-𝗦𝗘 𝗔𝗤𝗨𝗜]({LINK_SITE}) 🎁

🐯🧧 𝗙𝗼𝗿𝘁𝘂𝗻𝗲 𝗧𝗶𝗴𝗲𝗿 🧧🐯

🅿️ *PADRÃO: {number_aleat1}x*
⚡️ *TURBO: {number_aleat2}x*

⏱ *VÁLIDO POR 5 MINUTOS* ⏱

💸 Banca Recomendada: 𝗥*$*𝟮𝟬,𝟬𝟬
'''
    
    button = telebot.types.InlineKeyboardButton(text='🎁  CADASTRE-SE AQUI  🎁', url=LINK_SITE)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(button)
    
    try:
        # Enviar a mensagem inicial
        ini_msg = bot.send_message(chat_id=chat_id, text=mens_ini, parse_mode='HTML')
        mens_ini_id = ini_msg.message_id
        print('Mensagem inicial enviada!')
        
        # Apagar a mensagem 3
        if mens3_id:
            try:
                bot.delete_message(chat_id=chat_id, message_id=mens3_id)
                print('Mensagem 3 apagada com sucesso.')
            except Exception as e:
                print('Erro ao apagar mensagem 3')
        
        # Enviar a mensagem com o sinal
        time.sleep(10)
        with open('modelo1.png', 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo, caption=mens1, reply_markup=markup, parse_mode='Markdown')
        print('Sinal enviado!')

        # Apaga a mensagem inicial após o envio do sinal
        bot.delete_message(chat_id=chat_id, message_id=mens_ini_id)
        print('Mensagem inicial apagada com sucesso.')

    except Exception as e:
        print('Erro ao enviar mensagem 1')
        time.sleep(1)
        signal_1()
        
# Envia a mensagem de propaganda do seu Grupo / Canal VIP
def signal_2():
    button2 = telebot.types.InlineKeyboardButton(text='⚡️ ENTRAR NO GRUPO VIP ⚡️', url=LINK_GRUPO)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(button2)
    
    try:
        with open('modelo2.png', 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo, caption=mens2, reply_markup=markup, parse_mode='HTML')
        print('Mensagem 2 enviada!')
    
    except Exception as e:
        print('Erro ao enviar mensagem 2')
        print(e)
        time.sleep(1)
        signal_2()
        
# Envia a mensagem de informação para o próximo sinal
def signal_3():
    global mens3_id
    
    try:
        msg = bot.send_message(chat_id=chat_id, text=mens3, parse_mode='HTML')
        mens3_id = msg.message_id
        print('Mensagem 3 enviada!')
    
    except Exception as e:
        print('Erro ao enviar mensagem 3')
        print(e)
        time.sleep(1)
        signal_3()

def main():
    while True:
        signal_1()
        time.sleep(3)
        signal_2()
        time.sleep(3)
        signal_3()
        time.sleep(300) # Tempo para o próximo sinal - 5 min

if __name__ == '__main__':
    main()