import os
import gspread
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from messages import ask_question, correct_city_name
from email_sender import send_email

load_dotenv()

# Загрузка учетных данных
gc = gspread.service_account(filename='C:\\Users\\Пример\\creds.json') #указать свой путь до файла cred.json
cities_ws = gc.open('Копия Сбор анкет').worksheet('Копия список почт с городами') # указать свои таблицы и листы указано для примера

def get_cities_list():
    cities_data = cities_ws.get_all_records()
    cities = {record['Город']: record['Список почт по городам'] for record in cities_data if 'Город' in record and 'Список почт по городам' in record}
    return cities

def main():
    vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    cities = get_cities_list()
    states = {}

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            user_id = event.user_id
            user_message = event.text.strip().lower()

            if user_id not in states:
                states[user_id] = {
                    "name": None,
                    "phone": None,
                    "city": None,
                    "email": None,
                    "experience_repair": None,
                    "experience_clients": None,
                    "confirmation": None
                }

            if user_message == 'начать':
                ask_question(vk, user_id, "Введите Ваше ФИО?")
                states[user_id] = {
                    "name": None,
                    "phone": None,
                    "city": None,
                    "email": None,
                    "experience_repair": None,
                    "experience_clients": None,
                    "confirmation": None
                }
            elif states[user_id]["name"] is None:
                states[user_id]["name"] = user_message
                ask_question(vk, user_id, "Введите Ваш номер телефона:")
            elif states[user_id]["phone"] is None:
                states[user_id]["phone"] = user_message
                ask_question(vk, user_id, "Введите Ваш город:")
            elif states[user_id]["city"] is None:
                corrected_city = correct_city_name(user_message, cities)
                if corrected_city:
                    states[user_id]["city"] = corrected_city
                    ask_question(vk, user_id, "Укажите Вашу почту:")
                else:
                    ask_question(vk, user_id, "Такого города не найдено. Повторите попытку.")
            elif states[user_id]["email"] is None:
                states[user_id]["email"] = user_message
                ask_question(vk, user_id, "Есть ли у Вас опыт работы в ремонте и работе с клиентами? (Да/Нет)")
            elif states[user_id]["experience_repair"] is None:
                states[user_id]["experience_repair"] = user_message
                ask_question(vk, user_id, "Ожидаемый заработок:")
            elif states[user_id]["experience_clients"] is None:
                states[user_id]["experience_clients"] = user_message
                summary = (
    f"Данные кандидата:\n"
    f"👤 Имя: {states[user_id]['name']}\n"
    f"🏙️ Город: {states[user_id]['city']}\n"
    f"📞 Телефон: {states[user_id]['phone']}\n"
    f"📧 Email: {states[user_id]['email']}\n"
    f"🔧 Опыт в ремонте и с клиентами: {states[user_id]['experience_repair']}\n"
    f"💲 Ожидаемый доход: {states[user_id]['experience_clients']}\n"
   
)

                ask_question(vk, user_id, summary + " Все верно? Напишите 'Да' для отправки или 'Нет' для обновления данных.")
            elif states[user_id]["confirmation"] is None:
                if user_message == 'да':
                    city_email = cities[states[user_id]["city"]]  # Получаем email по городу
                    subject = 'Данные анкеты'
                    send_email(city_email, subject, summary)
                    ask_question(vk, user_id, "Спасибо данные отправлены, свяжемся с Вами после рассмотрения Вашей заявки.")
                    del states[user_id]
                elif user_message == 'нет':
                    del states[user_id]
                    ask_question(vk, user_id, "Опрос сброшен. Чтобы отредактировать Ваши данные напишите 'Начать'.")

if __name__ == "__main__":
    main()
