import os

import telebot as tg
import requests

bot = tg.TeleBot('6404342844:AAFlEOUMeM8bfA7LQnzgjLaAELprmyUQlx4')

def on_startup():
    print('[Консоль] Neiro в Телеграм запущен!')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я - Neiro. Ваш персональный ассистент и Искусственный Интеллект! Я умею решать задачи... и болтать о философии.\n\n /help Для списка команд.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Список доступных команд:\n/start - запускает самого бота\n/help - список команд бота\n/openai - разговор с нейросетью OpenAI')

'''
@bot.message_handler(commands=['openai'])
def chat(message):
    bot.reply_to(message, 'Приветствую! Чем могу помочь? (Чтобы остановиться, остановите бота через профиль.')
    bot.register_next_step_handler(message, do_openai)

@bot.message_handler()
def do_openai(message):
    print('creating request')
    response = openai.ChatCompletion.create(
        model=g4f.models.gpt_4
        messages=[{"role": "user", "content": message}]
        stream = True
    )
    print('sending request')
    for msg in response:
        bot.reply_to(message, msg)
    print('request sent')
'''


@bot.message_handler(content_types=['document'])
def handle_document(message):
    file = bot.get_file(message.document.file_id)
    dfile = bot.download_file(file.file_path)
    msg = bot.send_message(text="Проверяю файл...", chat_id=message.chat.id)

    with open(f'temp/{message.document.file_name}', 'wb') as w:
        w.write(dfile)
        w.close()

    check = check_file_with_virustotal(f'temp/{message.document.file_name}')

    ifvirusornot = ''
    if check['undetected'] >= 40:
        ifvirusornot = 'Судя по всему, файл безопасный :)'
    else:
        ifvirusornot = 'Не думаю, что файл безопасный... Хотя, может он просто написан вами.'

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=f"""
    Результаты проверки файла {message.document.file_name}

Антивирусы выявили голосами, что:
- Безопасный: {check['harmless']}
- Тип не поддерживается: {check['type-unsupported']}
- Подозрительный: {check['suspicious']}
- Время проверки истекло (подтверждённый): {check['confirmed-timeout']}
- Время проверки истекло: {check['timeout']}
- Ошибка проверки: {check['failure']}
- Опасный файл: {check['malicious']}
- Не найден вирус: {check['undetected']}

{ifvirusornot}
""")
    for i in os.listdir('temp'):
        os.remove(f'temp/{i}')


def check_file_with_virustotal(file):
    virustotal_apikey = '2fa7d331a906ddee7a0001f17004f3a8a27c4f706bf3f253e3289fdcc26d0598'
    virustotal_apiurl = 'https://www.virustotal.com/api/v3/files'
    virustotal_analysisurl = 'https://www.virustotal.com/api/v3/analyses/'
    headers = {
        "accept": "application/json",
        'x-apikey': virustotal_apikey,
    }
    files = {
        'file': (file, open(file, "rb"), "application/octet-stream")
    }

    response = requests.post(virustotal_apiurl, headers=headers, files=files)
    json_response = response.json()

    file_id = json_response['data']['id']
    tlink = virustotal_analysisurl + file_id
    response = requests.get(tlink, headers=headers)
    print(response.text)
    analysis_result = response.json()
    stats = analysis_result['data']['attributes']['stats']
    print(stats)

    return stats



bot.polling(none_stop=True)
