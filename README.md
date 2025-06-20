# API Yandex Samocat

## 📌 Описание проекта

Этот проект содержит автотесты для проверки работы REST API сервиса Яндекс Самокат
Покрытие включает сценарии по работе с сущностями **Курьер** и **Заказ**. Используются фреймворк `pytest`, генерация тестовых данных через `Faker`, отчётность через `Allure`.

---

## 🧰 Стек технологий

- Python 3.13
- Pytest
- Requests
- Faker
- Allure-pytest
- VS Code

---

## ✅ Что покрывают автотесты

### 🛵 Курьер

#### 📌 Создание курьера:
- ✅ Успешная регистрация нового курьера;
- 🚫 Попытка создать курьера с уже существующим логином (проверка дублирования);
- 🚫 Проверка валидации: создание курьера с отсутствующим `login`, `password` или `firstName`.

#### 🔐 Аутентификация курьера:
- ✅ Успешный логин с валидными данными;
- 🚫 Ошибка при отсутствии одного из обязательных полей (`login` или `password`);
- 🚫 Ошибка при попытке входа с несуществующими данными.

#### ❌ Удаление курьера:
- ✅ Успешное удаление курьера (`{"ok": true}`);
- 🚫 Ошибка при отсутствии `id` в теле запроса;
- 🚫 Ошибка при передаче несуществующего `id` курьера;
- 🔍 Проверка статус-кодов и сообщений об ошибке.

---

### 📦 Заказ

#### 🧾 Создание заказа:
- ✅ С одним цветом (`BLACK` или `GREY`);
- ✅ С обоими цветами одновременно;
- ✅ Без указания цвета (опциональный параметр);
- 🔍 Проверка, что в ответе присутствует ключ `track`.

#### 📥 Принятие заказа:
- ✅ Успешная привязка заказа к курьеру (`{"ok": true}`);
- 🚫 Ошибка, если не передать `id` курьера;
- 🚫 Ошибка, если `id` курьера не существует;
- 🚫 Ошибка, если не передан `id` заказа;
- 🚫 Ошибка при попытке принять несуществующий заказ.

#### 🔍 Получение заказа по номеру (track):
- ✅ Успешный возврат информации о заказе по корректному `track`;
- 🚫 Ошибка при отсутствии номера заказа;
- 🚫 Ошибка при передаче несуществующего `track`.

---

### 📋 Список заказов

- ✅ Успешное получение списка заказов;
- 🔍 Проверка, что в теле ответа присутствует ключ `orders` (и он является списком).
    
    