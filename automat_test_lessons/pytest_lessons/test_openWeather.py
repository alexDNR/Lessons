# попробуем написать пару простых тестов на типы полей в ответе с сайта openWeather
# проверим по каждому словарю поля и их типы и значения

'''
Вот ответ на запрос по городу Кировское и какие поля и в каой размерности и типах приходят
{
    "coord": {
        "lon": 35.2011,
        "lat": 45.2306
    },
    "weather": [
        {
            "id": 804,
            "main": "Clouds",
            "description": "пасмурно",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 7.08,
        "feels_like": 4.38,
        "temp_min": 7.08,
        "temp_max": 7.08,
        "pressure": 1018,
        "humidity": 34,
        "sea_level": 1018,
        "grnd_level": 1016
    },
    "visibility": 10000,
    "wind": {
        "speed": 4.07,
        "deg": 301,
        "gust": 5.34
    },
    "clouds": {
        "all": 100
    },
    "dt": 1680177571,
    "sys": {
        "country": "UA",
        "sunrise": 1680146661,
        "sunset": 1680192180
    },
    "timezone": 10800,
    "id": 689374,
    "name": "Kirovskoe",
    "cod": 200
}
'''    

import pytest

# фикстура получает данные с запроса на сайт и возвращает его в виде json объекта
@pytest.fixture(scope="session")
def answer_request(): 
    import requests

    params = {"q" : "Kirovskoe", "appid" : "b13525faf9ad6f7036a2a6cb1b9aad9b", "units" : "metric", "lang" : "ru"} 
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    if response.status_code == 200:
        answer = response.json()
        return answer
    else:
        return None     
#----------------------------------------------------------------------------------

# тест на проверку типа ответа на запрос - должен быть словарь
def test__answer__type(answer_request): 
    response = answer_request
    assert isinstance(response, dict) 
#----------------------------------------------------------------------------------

# тест на проверку всех ключей в ответе
def test_the_presence_of_keys_in_response(answer_request): 
    response = answer_request
    list_keys = ["coord", "weather", "main", "wind", "clouds", "sys"]
    for i in list_keys:
        assert i in response
#----------------------------------------------------------------------------------

# тест на проверку объекта --coord-- на тип и что внутри
def test_object__coord__data_type_and_value(answer_request): 
    response = answer_request
    assert isinstance(response['coord'], dict)  

    # проверка на наличие --lon-- и --lat-- в словаре
    assert 'lon' in response['coord'] and 'lat' in response['coord']
    # проверка на тип данных float и что нет города с координатами 0 0 - эта точка находится в море
    assert isinstance(response['coord']['lon'], float) and isinstance(response['coord']['lat'], float)   
    assert response['coord']['lon'] != 0 and response['coord']['lat'] != 0 
     
#----------------------------------------------------------------------------------

# тест на проверку объекта --weather-- на тип и что внутри
def test_object__weather__data_type_and_value(answer_request): 
    response = answer_request
    assert isinstance(response['weather'], list) # сам объект должен быть список

    # так как у нас объект список состоящий из одного элемента, то в нём должен быть словарь
    assert isinstance(response['weather'][0], dict) 

    # проверка на наличие всех ключей в словаре, который находится в списке
    list_keys = ["id", "main", "description", "icon"]
    for i in list_keys:
        assert i in response['weather'][0]
   
    # проверка на тип поля с ключём --id-- и проверка на то, что это значение должно быть больше 0
    assert isinstance(response['weather'][0]['id'], int) and response['weather'][0]['id'] > 0 # Идентификатор погодных условий
    assert isinstance(response['weather'][0]['main'], str) and len(response['weather'][0]['main']) != 0 # Группа погодных параметров
    assert isinstance(response['weather'][0]['description'], str) and len(response['weather'][0]['description']) != 0 # Погодные условия в группе
    assert isinstance(response['weather'][0]['icon'], str) and len(response['weather'][0]['icon']) != 0 # Идентификатор значка погоды
#----------------------------------------------------------------------------------

# тест на проверку объекта --main-- на тип и что внутри
def test_object__main__data_type_and_value(answer_request): 
    response = answer_request
    assert isinstance(response['main'], dict) # сам объект должен быть словарь

    # проверка на наличие всех ключей в словаре
    list_keys = ["temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity", "sea_level"]
    for i in list_keys:
        assert i in response['main']

    # так как у нас в запросе параметр "units" указано "metric", то значения температуры приходят в градусах Цельсия 
    # проверка на тип поля с ключём --temp-- и проверка на то, что это значение должно лежать в пределах от -80 до +60 градусов Цельсия
    assert isinstance(response['main']['temp'], float) and  -80 < response['main']['temp'] < 60 # температура фактическая
    assert isinstance(response['main']['feels_like'], float) and -80 < response['main']['feels_like'] < 60 # температура ощущения  
    assert isinstance(response['main']['temp_min'], float) and -80 < response['main']['temp_min'] < 60 # температура минимальная
    assert isinstance(response['main']['temp_max'], float) and -80 < response['main']['temp_max'] < 60 # температура максимальная    
    assert isinstance(response['main']['pressure'], int) and response['main']['pressure'] > 0 # давление      
    assert isinstance(response['main']['humidity'], int) and response['main']['humidity'] > 0 # влажность     
    assert isinstance(response['main']['sea_level'], int) and response['main']['sea_level'] > 0 # давление на уровне моря
#----------------------------------------------------------------------------------

# тест на проверку объекта --wind-- на тип и что внутри
def test_object__wind__data_type_and_value(answer_request):
    response = answer_request
    assert isinstance(response['wind'], dict)

    # проверка на наличие всех ключей в словаре
    list_keys = ["speed", "deg", "gust"]
    for i in list_keys:
        assert i in response['wind']

    assert isinstance(response['wind']['speed'], float) and response['wind']['speed'] >= 0 # это скорость ветра
    assert isinstance(response['wind']['deg'], int) and response['wind']['speed'] >= 0 # это градусы, они должны быть >= 0
    assert isinstance(response['wind']['gust'], float) and response['wind']['gust'] >= 0 # это скорость порыва ветра, она должна быть >= 0
#----------------------------------------------------------------------------------

# тест на проверку объекта --sys-- на тип и что внутри
def test_object__sys__data_type_and_value(answer_request):
    import datetime

    response = answer_request
    assert isinstance(response['sys'], dict)
    
    # проверка на наличие всех ключей в словаре
    list_keys = ["country", "sunrise", "sunset"]
    for i in list_keys:
        assert i in response['sys']

    assert isinstance(response['sys']['country'], str) and len(response['sys']['country']) > 0 # Код страны

    # Дальше идут два временных поля. Сначала проверим преобразование этих полей в нормальную дату. Данные передаются в UTC
    assert response['sys']['sunrise'].datetime.fromtimestamp()
    assert response['sys']['sunset'].datetime.fromtimestamp()

    # Теперь надо проверить что приходит текущая дата
    #date_now = datetime.date.today() # Получение текущей даты

    # доделать завтра проверку на текущую дату и остальные поля, которые отдельно приходят, в основном словаре