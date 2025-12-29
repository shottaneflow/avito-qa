
# Тест-кейсы для API микросервиса объявлений

## 1. Ручка: Сохранить объявление (POST `/api/1/item`)

### Позитивные тест-кейсы

#### **TC-POST-001: Успешное создание объявления с валидными данными**
- **Request body:**
```json
{
    "sellerID": 132112,
    "name": "Камод",
    "price": 10000,
    "statistics": {
        "likes": 150,
        "viewCount": 2500,
        "contacts": 45
    }
}
Шаги:

    1. Отправить POST запрос на /api/1/item с валидным телом

Ожидаемый результат:

HTTP Status: 200 OK

Response body:
{
    "id": "<string>",
    "sellerId": "<integer>",
    "name": "<string>",
    "price": "<integer>",
    "statistics": {
        "likes": "<integer>",
        "viewCount": "<integer>",
        "contacts": "<integer>"
    },
    "createdAt": "<string>"
}

#### **TC-POST-002: Нулевые значения статистики**

Request body:

{
    "sellerID": 12345,
    "name": "Тестовый товар",
    "price": 1000,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

Ожидаемый результат: 200 OK

#### **TC-POST-101: Отсутствие обязательного поля sellerID**
Request body:

{
    "name": "Телефон",
    "price": 50000,
    "statistics": {
        "likes": 10,
        "viewCount": 100,
        "contacts": 5
    }
}

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле sellerID обязательно"}, "status": "400"}

#### **TC-POST-102: Отсутствие обязательного поля name**

Request body:

{
    "sellerID": 12345,
    "price": 50000,
    "statistics": {
        "likes": 10,
        "viewCount": 100,
        "contacts": 5
    }
}
Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле name обязательно"}, "status": "400"}

#### **TC-POST-103: Отсутствие обязательного поля price**

Request body:

{
    "sellerID": 12345,
    "name": "Телефон",
    "statistics": {
        "likes": 10,
        "viewCount": 100,
        "contacts": 5
    }
}
Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле price обязательно"}, "status": "400"}

#### **TC-POST-104: sellerID не integer**

Request body:

{
    "sellerID": "не число",
    "name": "Товар",
    "price": 1000,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}
Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле sellerID должно быть числом"}, "status": "400"}

#### **TC-POST-105: name не string**

Request body:

{
    "sellerID": 12345,
    "name": 12345,
    "price": 1000,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле name должно быть строкой"}, "status": "400"}

#### **TC-POST-106: price не integer**

Request body:

{
    "sellerID": 12345,
    "name": "Товар",
    "price": "сто рублей",
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле price должно быть числом"}, "status": "400"}

#### **TC-POST-107: Отрицательный price (БАГ API)**

Request body:

{
    "sellerID": 12345,
    "name": "Товар",
    "price": -100,
    "statistics": {
        "likes": 0,
        "viewCount": 0,
        "contacts": 0
    }
}

Ожидаемый результат: 400 Bad Request

Фактический результат: 200 OK

#### **TC-POST-108: Отрицательные значения в statistics **

Request body:

{
    "sellerID": 12345,
    "name": "Товар",
    "price": 100,
    "statistics": {
        "likes": -50,
        "viewCount": -100,
        "contacts": -10
    }
}

Ожидаемый результат: 400 Bad Request

Фактический результат (БАГ): 200 OK

#### **TC-POST-109: Отсутствие поля likes в statistics **

Request body:

{
    "sellerID": 12345,
    "name": "Товар",
    "price": 100,
    "statistics": {
        "viewCount": 100,
        "contacts": 50
    }
}

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле likes обязательно"}, "status": "400"}

#### **TC-POST-110: Отсутствие поля viewCount в statistics **

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле viewCount обязательно"}, "status": "400"}

#### **TC-POST-111: Отсутствие поля contacts в statistics**

Ожидаемый результат: 400 Bad Request

Response body: {"result": {"message": "поле contacts обязательно"}, "status": "400"}


## 2. Ручка: Получить объявление по идентификатору (GET `/api/1/item/:id`)

### Позитивные тест-кейсы

#### **TC-GET-ITEM-001: Получение существующего объявления**
- **Предусловие:** Создано объявление с валидным ID
- **Шаги:**
  1. Создать объявление через POST `/api/1/item`
  2. Отправить GET запрос на `/api/1/item/:id` с полученным ID
- **Ожидаемый результат:**
  - HTTP Status: 200 OK
  - Тело ответа содержит массив с одним объектом объявления
  - Все поля объявления соответствуют созданному:
    - `id` соответствует переданному ID
    - `sellerId` соответствует `sellerID` из запроса
    - `name`, `price`, `statistics` соответствуют переданным


### Негативные тест-кейсы

#### **TC-GET-ITEM-101: Невалидный формат ID (-1)**
- **URL:** `/api/1/item/-1`
- **Ожидаемый результат:** 400 Bad Request

## 3. Ручка: Получить все объявления пользователя (GET `/api/1/:sellerID/item`)

### Позитивные тест-кейсы

#### **TC-GET-SELLER-001: Получение объявлений существующего продавца**
- **Предусловие:** Продавец с ID = 111111 существует
- **Шаги:**
  1. Отправить GET запрос на `/api/1/111111/item`
- **Ожидаемый результат:**
  - HTTP Status: 200 OK
  - Тело ответа содержит массив объявлений
  - Все объявления в массиве имеют структуру:
    - `id` (string)
    - `sellerId` (integer, равен 111111)
    - `name` (string)
    - `price` (integer)
    - `statistics` (object с полями likes, viewCount, contacts)
    - `createdAt` (string)

### Негативные тест-кейсы



#### **TC-GET-SELLER-101: Отрицательный sellerID**
- **URL:** `/api/1/-123/item`
- **Ожидаемый результат:** 400 Bad Request

## 4. Ручка: Получить статистику по объявлению (GET `/api/1/statistic/:id`)

### Позитивные тест-кейсы

#### **TC-GET-STAT-001: Получение статистики существующего объявления**
- **Предусловие:** Создано объявление с известной статистикой
- **Шаги:**
  1. Создать объявление со статистикой: `{"likes": 100, "viewCount": 500, "contacts": 50}`
  2. Отправить GET запрос на `/api/1/statistic/:id`
- **Ожидаемый результат:**
  - HTTP Status: 200 OK
  - Тело ответа содержит массив объектов статистики
  - Каждый объект содержит поля: `likes`, `viewCount`, `contacts` (integer)
  - Значения соответствуют переданным при создании

### Негативные тест-кейсы

#### **TC-GET-STAT-101: Статистика несуществующего объявления**
- **URL:** `/api/1/statistic/несуществующий айди`
- **Ожидаемый результат:** 404 Not Found

#### **TC-GET-STAT-102: Невалидный формат ID (-1)**
- **URL:** `/api/1/statistic/-1`
- **Ожидаемый результат:** 400 Bad Request

#### **TC-GET-STAT-104: Пустой ID**
- **URL:** `/api/1/statistic/`
- **Ожидаемый результат:** 404 Not Found

