import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "ВАШ_ТОКЕН"
bot = telebot.TeleBot(TOKEN)

#расписание
SCHEDULE = {
    "Понедельник": ["Математика (10:00)", "История (12:00)", "Физика (14:00)"],
    "Вторник": ["Литература (10:00)", "Химия (12:00)", "География (14:00)"],
    "Среда": ["Биология (10:00)", "Английский (12:00)", "Информатика (14:00)"],
    "Четверг": ["Обществознание (10:00)", "Физкультура (12:00)", "Музыка (14:00)"],
    "Пятница": ["Математика (10:00)", "Химия (12:00)", "Английский (14:00)"],
}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn_schedule = InlineKeyboardButton("📅 Получить расписание", callback_data="get_schedule")
    markup.add(btn_schedule)

    bot.send_message(
        message.chat.id,
        "Привет Я бот для расписания уроков. Нажми на кнопку снизу чтобы получить расписание.",
        reply_markup=markup,
    )

@bot.callback_query_handler(func=lambda call: call.data == "get_schedule")
def send_schedule(call):
    schedule_text = "📚 *Расписание уроков:*\n\n"
    for day, lessons in SCHEDULE.items():
        schedule_text += f"*{day}:*\n" + "\n".join(f"• {lesson}" for lesson in lessons) + "\n\n"

    bot.send_message(call.message.chat.id, schedule_text, parse_mode="Markdown")

if __name__ == "__main__":
    print("Бот запущен!")
    bot.infinity_polling()
