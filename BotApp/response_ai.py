import os
import requests
from dotenv import load_dotenv


load_dotenv()

CHAD_API_KEY = os.getenv("API_AI_TOKEN")


def get_response_ai(text: str):
    request_json = {
        "message": text,
        "api_key": CHAD_API_KEY
    }

    response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini',
                             json=request_json)

    if response.status_code != 200:
        print(f'Ошибка! Код http-ответа: {response.status_code}')
    else:
        resp_json = response.json()

        if resp_json['is_success']:
            resp_msg = resp_json['response']
            used_words = resp_json['used_words_count']
            print(f'Ответ от бота: {resp_msg}\nПотрачено слов: {used_words}')
        else:
            error = resp_json['error_message']
            print(f'Ошибка: {error}')
