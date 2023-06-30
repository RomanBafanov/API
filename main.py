from typing import Any
import requests


PARAMS = {
        'lang': 'ru',
        'M': '',
        'nmq': '',
        'T': '',
    }

def request_weather(city: Any) -> Any:
    url = f'http://wttr.in/{city}'
    response = requests.get(url, params=PARAMS)
    response.raise_for_status()

    return response.text


def main() -> Any:
    locations = [
        'svo',
        'London',
        'Череповец',
    ]
    for city in locations:
        print(request_weather(city))


if __name__ == '__main__':
    main()


