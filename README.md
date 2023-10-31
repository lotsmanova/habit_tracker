# Tracker Habits

---

Бэкенд-часть SPA веб-приложения для создания трекера привычек.

## Технологии

---

- [ ]  Python
- [ ]  Django restframework
- [ ]  PostgreSQL
- [ ]  Celery
- [ ]  Celery beat
- [ ]  Redis

## Установка зависимостей

---

Для работы программы необходимо установить зависимости из файла `requirements.txt`.

Файл `.env.sample` содержит необходимые для работы переменные окружения.


## Структура проекта

---

### Приложения

- [ ]  user - интерфейсы для регистрации и авторизации пользователя.
- [ ]  tracker - интерфейс создания привычки (создание, просмотр, редактирование, удаление).
- [ ]  notification - приложение отложенной задачи для отправки уведомлений в телеграмм пользователям с напоминанием о выполнении привычки.

### Логика работы

Авторизированный пользователь может создать привычку. Пользователь может добавить вознаграждение или приятную привычку к полезной (`is_good_habit = True`). Каждые 30 минут запускается отложенная задача по отправке напоминаний пользователям в телеграмм. Напоминание можно отправить вручную с помощью кастомной команды `python3 [manage.py](http://manage.py/) send_message`.

### Модели

- [ ]  Habits - модель привычки
- [ ]  User - модель пользователя

### Валидация

- Нельзя одновременно выбрать связанную привычку и вознаграждение.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

### Права доступа

- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их редактирования или удаления.

### Безопасность

Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.

### Документация

Сгенерирована документация к проекту с помощью библиотеки `drf-yasg.`Документация доступна по ссылкам [`http://127.0.0.1:8000/](http://127.0.0.1:8000/)swagger/` или  `http://127.0.0.1:8000/redoc/`.

### Docker

Чтобы собрать контейнер, воспользуйтесь командой `docker compose build.` Чтобы запустить контейнер с проектом, воспользуйтесь командой `docker compose up`.