1. Успешный запрос на POST /api/1/item возвращает невалидное тело
   Критичность: Major
   Приоритет: High
   Шаги воспроизведение:
   1. Сделать запрос на POST /api/1/item с валидным телом
   
   Ожидаемый результат:
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
    Фактический результат:
    {
        "status": "Сохранили объявление - <string>"
    }

2. Ручка получить объявление по идентификатору (GET /api/1/item/:id)
   Критичность: Major
   Приоритет: High
   Описание: Вместо заявленного массива объявлений отдается только последнее указанное
   Шаги воспроизведение:
   1. Сделать запрос на GET /api/1/item/:id , передав несколько id 
   Ожидаемый результат:
   [
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
    },
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
   ]
   Фактический результат:
    [
        {
            "createdAt": "2025-12-28 19:22:12.339591 +0300 +0300",
            "id": "8155e299-5d54-4ed8-bd22-b6beb3ebd072",
            "name": "Камод",
            "price": 1000,
            "sellerId": 132112,
            "statistics": {
                "contacts": 1,
                "likes": 1,
                "viewCount": 1
            }
        }
    ]

3. В требованиях не сказано про минимальное значение полей likes, viewCount, contacts , но я подозреваю, что эти поля должны допускать 0.
4. При попытке сохранения объявления отрицаптельные поля: price,likes,viewCount.contacts