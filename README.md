# Тестовое задание: Backend, Python

## Описание
Необходимо реализовать асинхронное веб-приложение в парадигме REST API.(проект во второй ветке)

### Стек:
- **База данных**: PostgreSQL
- **ORM**: SQLAlchemy
- **Веб-фреймворк**: Sanic (альтернативы возможны, но не Django)
- **Docker Compose**

## Сущности:
1. **Пользователь**: имеет email/password для авторизации, может просматривать свои данные, счета и платежи.
2. **Администратор**: управляет пользователями, может создавать, удалять и обновлять их.
3. **Счет**: связан с пользователем, имеет баланс.
4. **Платеж**: пополнение баланса пользователя, включает уникальный идентификатор и сумму.

## Возможности пользователей:
### Пользователь:
- Авторизация по email/password.
- Получение данных о себе (id, email, full_name).
- Список счетов с балансами и платежей.

### Администратор:
- Авторизация по email/password.
- Получение данных о себе (id, email, full_name).
- Управление пользователями: создание, удаление, обновление.
- Получение списка пользователей и их счетов с балансами.

## Платежи:
- Роут для обработки вебхука от сторонней платежной системы.
- Формат JSON вебхука:
  - `transaction_id`, `account_id`, `user_id`, `amount`, `signature`.
  - **Signature** формируется с помощью SHA256 хеша: `{account_id}{amount}{transaction_id}{user_id}{secret_key}`.

### Пример:
```json
{
  "transaction_id": "5eae174f-7cd0-472c-bd36-35660f00132b",
  "user_id": 1,
  "account_id": 1,
  "amount": 100,
  "signature": "7b47e41efe564a062029da3367bde8844bea0fb049f894687cee5d57f2858bc8"
}
