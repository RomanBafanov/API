from typing import Any
import requests


Params = {
    'san': {
        'francisco': '',
        'lang': 'en',
        '?n': '',
        '?T': '',
    },
    'svo': '',
    'London': '',
    'Череповец': {
        'lang': 'en',
        'M': '',
        'nmq': '',
        'T': '',
    }

}

def request(city: Any) -> Any:
    url = f'http://wttr.in/{city}'
    response = requests.get(url, params=Params[city])
    response.raise_for_status()

    return response.text


def main() -> Any:
    locations = [
        'san',
        'svo',
        'London',
        'Череповец',
    ]
    for city in locations:
        print(request(city))


if __name__ == '__main__':
    main()


