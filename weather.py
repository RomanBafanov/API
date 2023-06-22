import requests

loc = int(input('Выберите локацию:\n1 - Сан-Франциско\n2 - Шереметьево\n3 - Лондон\n4 - Череповец\n'))

if loc == 1:
    url = 'http://wttr.in/san%20francisco?nTqu&lang=en'
elif loc == 2:
    url = 'http://wttr.in/svo'
elif loc == 3:
    url = 'http://wttr.in/london'
elif loc == 4:
    url = 'http://wttr.in/Череповец?M&n&q&T&lang=ru'

response = requests.get(url)
print(response.text)
