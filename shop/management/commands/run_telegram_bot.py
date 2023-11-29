import telebot
from shop.models import Order

from django.core.management.base import BaseCommand



bot_token = '6014766028:AAGQtwWJuFpOFvDeEYGKlzzPgc2gZAMJkfc' 
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = ("Доступные команды:\n"
                 "/start - Начало работы с ботом\n"
                 "/order - Заказать еду\n"
                 "/orders - Просмотреть все заказы\n"
                 "/help - Показать это сообщение с информацией о командах")
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я бот для заказа еды.")

@bot.message_handler(commands=['orders'])
def orders(message):
    orders = Order.objects.all()  
    for order in orders:
        response = f"Заказ: {order.item}\nОписание: {order.special_requests}"
        bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['order'])
def add_order(message):
    try:
        content = message.text.split(maxsplit=1)[1]  
        item, special_requests = content.split(';') 
        item = item.strip()
        special_requests = special_requests.strip()

        Order.objects.create(
            item=item, 
            special_requests=special_requests
        )
        bot.reply_to(message, "Заказ успешно создан!")
    except (IndexError, ValueError):
        bot.reply_to(message, "Пожалуйста, следуйте формату: /order Название блюда; Дополнительные пожелания")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Сообщение получено.")





bot.polling()