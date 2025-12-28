1. Ручка: Сохранить объявление (POST /api/1/item)
    Позитивные тест-кейсы
    TC-1: Успешное создание объявления с валидными данными
        Предусловие: API доступно
        Request body:
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
            - HTTP Status: 200 OK
            - Response body:
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
                
                id (непустая строка)

                sellerId (соответствует переданному sellerID)

                name, price, statistics (соответствуют переданным)

                createdAt (валидная дата-время)