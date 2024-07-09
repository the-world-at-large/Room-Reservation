# Room Reservation System

## Описание
Проект представляет собой систему бронирования переговорных комнат.
Используется **FastAPI** для создания _RESTful API_ и **SQLAlchemy** для работы с _базой данных_.


## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/room_reservation.git
    cd room_reservation
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Настройте базу данных, заменив `DATABASE_URL` на вашу строку подключения в файле `app/core/config.py`:
    ```python
    SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # пример для SQLite
    ```

5. Иницилизируйте _alembic_ и примените миграции для создания таблицы в базе данных:
   ```sh
    alembic init alembic
    ```
   ```sh
    alembic revision --autogenerate -m "Add DATABASE"
    ```
   ```sh
    alembic upgrade head
    ```

## Запуск

1. Запустите приложение:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Откройте браузер и перейдите по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) для просмотра документации _Swagger_ или _Redoc_.

## Структура проекта

```plaintext
room_reservation/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── meeting_room.py
│   │   │   └── reservation.py
│   │   ├── __init__.py
│   │   └── validators.py
│   ├── core/
│   │   ├── config.py
│   │   ├── db.py
│   │   └── __init__.py
│   ├── crud/
│   │   ├── base.py
│   │   ├── meeting_room.py
│   │   ├── reservation.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── meeting_room.py
│   │   ├── reservation.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── meeting_room.py
│   │   ├── reservation.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
├── migrations/
│   └── ...
├── tests/
│   ├── __init__.py
│   └── test_reservation.py
├── alembic.ini
├── .gitignore
├── requirements.txt
└── README.md
```

# Endpoints

## Meeting Room Endpoints
- ```POST /meeting_rooms/```: Создать новую переговорную комнату
- ```GET /meeting_rooms/```: Получить список всех переговорных комнат
- ```PATCH /meeting_rooms/{meeting_room_id}```: Частично обновить переговорную комнату
- ```DELETE /meeting_rooms/{meeting_room_id}```: Удалить переговорную комнату

## Reservation Endpoints
- ```POST /reservations/```: Создать новую бронь
- ```GET /reservations/```: Получить список всех броней
- ```DELETE /reservations/{reservation_id}```: Удалить бронь

# Валидация и проверки

Проект включает несколько уровней валидации и проверки данных:
- Проверка на наличие дубликатов имен переговорных комнат.
- Проверка существования переговорной комнаты перед созданием или изменением брони.
- Проверка временных интервалов бронирования.
- Проверка пересечения временных интервалов бронирования.

Также настроена работа системы пользователей - **FastAPI** ***Users***.

# Требования
- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Alembic

# Лицензия
Этот проект лицензирован под MIT License.
