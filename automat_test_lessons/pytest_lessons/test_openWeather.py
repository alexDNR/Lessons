# попробуем написать пару простых тестов на типы полей в ответе с сайта openWeather
# проверим по каждому словарю поля и их типы

import pytest

@pytest.fixture(scope="session")
def answer_request(): # фикстура получает данные с запроса на сайт и возвращает его в виде json объекта
    import requests

    params = {"q" : "Kirovskoe", "appid" : "b13525faf9ad6f7036a2a6cb1b9aad9b", "units" : "metric", "lang" : "ru"} 
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    if response.status_code == 200:
        answer = response.json()
        return answer
    else:
        return None     

#print(answer_request())

def test_answer_type(answer_request): # тест на проверку типа ответа на запрос - должен быть словарь
    response = answer_request
    assert isinstance(response, dict) 

# группа тестов по объекту --coord-- из ответа
def test_find_object_coord_in_answer(answer_request): # тест на проверку наличия объекта coord в ответе на запрос
    response = answer_request
    assert 'coord' in response   

def test_object_coord_type(answer_request): # тест на проверку типа ответа на запрос - должен быть словарь
    response = answer_request
    assert isinstance(response['coord'], dict)        

def test_object_coord_data_type(answer_request): # тест на проверку типов данных в этом объекте
    response = answer_request
    assert isinstance(response['coord']['lon'], float)
    assert isinstance(response['coord']['lat'], float) 