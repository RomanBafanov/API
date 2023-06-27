import requests

def req_weather(Url, city):
        response = requests.get(Url, params=city)
        print(res_weather(response))

def res_weather(response):
    return response.text if response.ok else response.raise_for_status
