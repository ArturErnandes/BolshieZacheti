import telebot


with open('secretdata.txt', 'r') as file:
    creator_id = file.readline().strip().split(' ')[1]
    token = file.readline().strip().split(' ')[1]

bot = telebot.TeleBot(token)




def main():
    print("The program has been successfully started")
    bot.send_message(creator_id, "Программа запущена")

main()
bot.infinity_polling()