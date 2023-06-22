#!/bin/bash

# Запуск тестов
python -m unittest discover -s tests

# Проверка кода на ошибки
if [ $? -eq 0 ]
then
    # Сборка Docker-образа
    docker build -t gpt .

    docker run -p 5000:5000 gpt
else
    echo "Тесты не прошли"
fi


