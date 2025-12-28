1. Успешный запрос на POST /api/1/item возвращает невалидное тело
   Критичность: Блокирующий
   Приоритет: Высокий
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
