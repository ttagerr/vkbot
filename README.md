

# VkBot - Интерактивный бот ВКонтакте для опроса кандидатов

## Описание

Этот бот предназначен для проведения опросов кандидатов через платформу ВКонтакте. Он собирает информацию от пользователей, включая имя, телефон, город, электронную почту и опыт работы. Затем бот отправляет собранные данные на указанный адрес электронной почты.

## Установка

1. **Клонируйте репозиторий:**
```bash

   git clone https://github.com/ваш_пользователь/vkbot.git

   ```
2. Перейдите в каталог проекта:
```bash

   cd vkbot

   ```
3. Создайте виртуальное окружение:
```bash

   python -m venv venv

   ```
4. Активируйте виртуальное окружение:
   - Для Windows:
```bash

     venv\Scripts\activate

     ```
- Для macOS/Linux:
```bash

     source venv/bin/activate

     ```
5. Установите зависимости:
```bash

   pip install -r requirements.txt

   ```
## Конфигурация
   ```
этот файл создан под таблицу 
пример: 1 столбец список почт, 2 столбец название города
example.gmail.ru Москва

Создайте файл `.env` в корне проекта и добавьте следующие переменные:


VK_ACCESS_TOKEN=ваш_токен_доступа

EMAIL_USER=ваш_email@example.com

EMAIL_PASSWORD=ваш_пароль

```
## Запуск бота

1. Убедитесь, что ваш файл `.env` правильно настроен.
2. Запустите бот:
```bash

   python main.py

   ```
## Использование

Напишите боту «Начать», чтобы начать опрос. Затем общайтесь в чате для предоставления необходимой информации.

## Лицензия

Этот проект осуществляется под лицензией MIT. См. файл ЛИЦЕНЗИЯ на детали.

## Контакты

Если у вас есть вопросы или предложения касательно проекта, не стесняйтесь обращаться в тг: @ttaggerr

**Не забудьте заменить:**
- `https://github.com/ваш_пользователь/vkbot.git` на актуальную ссылку на ваш репозиторий GitHub.
- `ваш_токен_доступа` на ваш токен доступа VK.
- `ваш_email@example.com` на ваш адрес электронной почты.
- `ваш_пароль` на ваш пароль от почты (храните пароли безопасно, лучше использовать переменные окружения или менеджеры паролей!).