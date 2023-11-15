## Установка:

Клонируем проект:  

    git clone https://github.com/anza-afk/form_api_test_task.git

Установка зависимостей (в виртуальное окружение):

    pip install -r requirements.txt


## Запуск:

    uvicorn main:app --reload

## Тестовый скрипт:

    python test_api.py

Можно добавить больше форм для теста, путём добавления python dict с данными в файл initial.py в список test_data к остальным данным