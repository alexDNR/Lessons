#в этом файле рассмотрим вариант POST запроса на форму ввода логина, пароля, почты и двух чек-боксов с сайта http://httpbin.org/forms/post
# для POST запросов необходимо передавать в headers данные браузера, чтобы сервис не думал, что робот
# для этого достотачно (для теста) передавать только поле User-Agent

import requests

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.0.2246 Yowser/2.5 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-64240eee-340dc7d455a3d1997957a9a5",
    "Accept-Language" : "ru,uk;q=0.9,en;q=0.8"
}

payload = {
    "custname" : "test_name", 
    "custtel" : "+71234567890",
    "custemail" : "email@test.ru",
    "size" : "small",
    "topping" : ["bacon", "cheese", "onion", "mushroom"],
    "delivery" : "12:00",
    "comments" : "test comment"
}

response = requests.post("http://httpbin.org/post", headers=headers, data=payload)

if response.status_code == 200:
    print(response.text)

else:
    print(response.status_code)    

# в ответе приходит то же, что и на самом сайте показывается в виде ответа за POST запрос