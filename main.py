from weather import req_weather


url = 'http://wttr.in'
locations = [
        {'san': ['francisco', 'n', 'qu', 'lang=en',]},
        {'svo': ''},
        {'London': ''},
        {'Череповец': ['M', 'nmq', 'T', 'lang=ru',]},
    ]

def main():
    for city in locations:
        req_weather(url, city)


if __name__ == '__main__':
    main()


