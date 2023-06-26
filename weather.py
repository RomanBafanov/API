import requests


url = 'http://wttr.dvmn.org'
location = [
        'san%20francisco?nTqu&lang=en',
        'svo',
        'London',
        'Череповец?M&n&q&T&lang=ru',
    ]

def go_weather():
    for param in location:
        response = requests.get(url, params=param)
        if response.status_code == 200:
            print(response.text)
        else:
            print(response.raise_for_status)
