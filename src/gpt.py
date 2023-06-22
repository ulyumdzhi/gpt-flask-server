import os
import openai

try:
    OPENAI_KEY = os.environ['OPENAI_KEY']
    ENGINE = os.environ['ENGINE']
    MAX_TOKENS = os.environ['MAX_TOKENS']
    TEMPERATURE = os.environ['TEMPERATURE']
except:
    from data.config import OPENAI_KEY, ENGINE, MAX_TOKENS, TEMPERATURE

# Устанавливаем токен OpenAI
openai.api_key = OPENAI_KEY


def gpt_process(input_text: str) -> str:

    # Твой шанс стать prompt-engineer
    prompt = 'Проверь решение и если оно не верное подскажи на русском как исправить ошибку. Но не говори это явно! Сделай намёк: ' + input_text

    response = openai.Completion.create(
        engine='text-davinci-003',  # Выбираем модель GPT
        prompt=prompt,
        max_tokens=300,  # Максимальное количество токенов в ответе
        temperature=0.3,  # Уровень разнообразия в ответе (0.0 - 1.0)
        n=1  # Генерируем только один ответ
    )

    # Извлекаем сгенерированный ответ
    generated_text = response.choices[0].text.strip()

    stop_phrase = ['Сделай намёк:', 'Помоги!']
    for phrase in stop_phrase:
        if phrase in generated_text:
            generated_text = generated_text.split(phrase)[1]

    generated_text = ' '.join(generated_text.split())

    return generated_text
