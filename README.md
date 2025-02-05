# Test Project

## Описание
### База данных - postgresql
### sqlalchemy
### FastAPI
### docker compose


### Сигнатура для вебхука печатается в консоли, данные в src/service/webhook должны совпадать с отправляемыми соответственно


## Запуск без Docker
1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
2. Настройте базу данных PostgreSQL (укажите настройки в `.env`).
3. Запустите миграции:
    ```bash
    alembic upgrade head
    ```
4. Запустите сервер:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## Запуск с Docker Compose
1. У вас установлен Docker и Docker Compose.
2. Запустите контейнеры:
    ```bash
    docker-compose up --build
    ```
3. API будет доступно по адресу `http://localhost:8000`.

## Данные для входа
### Администратор:
- **Email**: `test_admin@example.com`
- **Пароль**: `passwordadmin123`

### Обычный пользователь:
- **Email**: `test_user@example.com`
- **Пароль**: `password123`
