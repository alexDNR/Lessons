# попробуем написать пару простых тестов на типы полей в ответе с сайта openWeather
# проверим по каждому словарю поля и их типы и значения

import pytest

# фикстура получает данные с запроса на сайт и возвращает его в виде json объекта
@pytest.fixture(scope="session")
def response(): 
    import requests
    from configuration_tests import SERVICE_URL, TOKEN, CITY

    params = {"q" : CITY, "appid" : TOKEN, "units" : "metric", "lang" : "ru"} 
    response = requests.get(url=SERVICE_URL, params=params)
    if response.status_code == 200:
        answer = response.json()
        return answer
    else:
        return None     
#----------------------------------------------------------------------------------

# тест на проверку типа ответа на запрос - должен быть словарь
def test_answer_type(response): 
    assert isinstance(response, dict) 
#----------------------------------------------------------------------------------

def test_answer_field(response):
    from src.pydantic_schemas.post import Model

    assert Model.parse_obj(response)
#----------------------------------------------------------------------------------

def test_answer_fields_data(response):
    from datetime import datetime
    from datetime import date

    assert response['coord']['lon'] != 0.0 and response['coord']['lat'] != 0.0
#----------------------------------------------------------------------------------
    assert response['weather'][0]['id'] > 0 # Идентификатор погодных условий
    assert response['weather'][0]['main'] # Группа погодных параметров
    assert response['weather'][0]['description'] # Погодные условия в группе
    assert response['weather'][0]['icon'] # Идентификатор значка погоды
#----------------------------------------------------------------------------------
    assert -80.0 < response['main']['temp'] < 60.0 # температура фактическая
    assert -80.0 < response['main']['feels_like'] < 60.0 # температура ощущения  
    assert -80.0 < response['main']['temp_min'] < 60.0 # температура минимальная
    assert -80.0 < response['main']['temp_max'] < 60.0 # температура максимальная  
#----------------------------------------------------------------------------------
    assert response['main']['pressure'] > 0 # давление      
    assert response['main']['humidity'] > 0 # влажность     
    assert response['main']['sea_level'] > 0 # давление на уровне моря
    assert response['wind']['speed'] >= 0.0 # это скорость ветра
    assert response['wind']['speed'] >= 0 # это градусы, они должны быть >= 0
    assert response['wind']['gust'] >= 0.0 # это скорость порыва ветра, она должна быть >= 0
#----------------------------------------------------------------------------------
    assert datetime.fromtimestamp(response['sys']['sunrise'])
    assert datetime.fromtimestamp(response['sys']['sunset'])
    # Теперь надо проверить что приходит текущая дата
    date_now = datetime.today().date() # Получение текущей даты 
    assert datetime.fromtimestamp(response['sys']['sunrise']).date() == date_now
    assert datetime.fromtimestamp(response['sys']['sunset']).date() == date_now
#----------------------------------------------------------------------------------
    assert response['id'] > 0 # ID города
    assert response['cod'] > 0 # Внутренний параметр
    assert response['visibility'] > 0 # Видимость, метр. Максимальное значение видимости 10км
    assert response['base'] # Внутренний параметр
    assert response['name'] # Название города
#----------------------------------------------------------------------------------
    # Два временных поля
    assert datetime.fromtimestamp(response['timezone']) # Сдвиг в секундах от UTC 
    assert datetime.fromtimestamp(response['dt']) # Время расчета данных, unix, UTC