# программка выводит получает ответ на запрос с сайта openWeather и выводит данные по
# некоторым полям, по нескольким городам

import requests
from datetime import datetime

citys = ["Kirovskoe", "London", "Tokyo"]

for i in citys:
    # координаты города (но чёт он находит Кировскоее, а не Жановку) и API ключ аккаунта
    params = {"q" : i, "appid" : "b13525faf9ad6f7036a2a6cb1b9aad9b", "units" : "metric", "lang" : "ru"} 

    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

    if response.status_code == 200:
        answer = response.json()

        print("Прогноз в городе:", answer["name"])
        timezone = answer["timezone"] # сдвиг в секундах

        if 'weather' in answer:
            sky = answer["weather"][0]["description"]
            print("Небо -", sky.capitalize())
        else:
            print("Нет в ответе ключа -- description")    

        if 'main' in answer:
            temp = answer["main"]["temp"]
            print("Температура воздуха -", temp, "°C")

            pressure = 0.00750062*answer["main"]["pressure"]*100
            print("Давление -", round(pressure, 2), "мм.рт.ст.")
        else:
            print("Нет в ответе ключа -- temp")

        if 'wind' in answer:
            speed_wind = answer["wind"]["speed"]*3.6
            print("Скорость ветра -", round(speed_wind,2), "км/ч ")
        else:
            print("Нет в ответе ключа -- wind")

        if 'sys' in answer:
            sunrise = datetime.fromtimestamp(answer["sys"]["sunrise"] + timezone)
            print("Рассвет -", sunrise.time(), "по местному времени")
            sunset = datetime.fromtimestamp(answer["sys"]["sunset"] + timezone)
            print("Закат -", sunset.time(), "по местному времени")
        else:
            print("Нет в ответе ключа -- sys")

    else:
        print("Error from request", response.status_code)

    print("---")