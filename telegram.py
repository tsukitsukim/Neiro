import telebot as tg
import openai

bot = tg.TeleBot('6404342844:AAFlEOUMeM8bfA7LQnzgjLaAELprmyUQlx4')
openai.api_key = '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'

def on_startup():
    print('[Консоль] Neiro в Телеграм запущен!')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - Neiro. Ваш персональный ассистент и Искусственный Интеллект! Я умею решать задачи... и болтать о философии.\n\n /help Для списка команд.")
    bot.reply_to(message, "Помечание разработчика: Это альфа версия, все функции ещё не добавлены. Пока что предоставляется бесплатный доступ к сети OpenAI, которая заблокирована в России. Пользуйтесь на здоровье. \n\n - Лавров Богдан (@plizikme)")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Список доступных команд:\n/start - запускает самого бота\n/help - список команд бота\n/openai - разговор с нейросетью OpenAI')

@bot.message_handler(commands=['openai'])
def chat(message):
    bot.reply_to(message, 'Приветствую! Чем могу помочь? (Чтобы остановиться, остановите бота через профиль.')
    bot.register_next_step_handler(message, do_openai)

@bot.message_handler()
def do_openai(message):
    print('creating request')
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.8,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=2000
    )
    print('sending request')
    bot.reply_to(message, response['choices'][0]['text'])
    print('request sent')

bot.polling(none_stop=True)
