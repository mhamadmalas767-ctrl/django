import telebot
import time  # لاستعمال التأخير بين إعادة التشغيل

TOKEN = "8429607879:AAF22DxyXpO3Gar-X0ONkoJb-ZucHdo0LcI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اهلا وسهلا بك!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "شكراً لرسالتك!")

# حلقة لإعادة تشغيل البوت تلقائيًا عند أي خطأ
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"حدث خطأ: {e}. سيتم إعادة التشغيل بعد 5 ثواني...")
        time.sleep(5)  # تأخير قبل إعادة التشغيل
