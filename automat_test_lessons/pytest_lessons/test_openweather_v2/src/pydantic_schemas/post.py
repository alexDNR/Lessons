'''
для файла test_openwweather_v2.py приходит вот такой ответ. Надо создать для неё схему и передать в файл
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

from typing import List
from pydantic import BaseModel, Field

class IntType(int):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, int):
            raise ValueError(f'not int, valute type: {type(value)}')
        return value

class FloatType(float):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, float):
            raise ValueError(f'not float, valute type: {type(value)}')
        return value

class Coord(BaseModel):
    lon: FloatType
    lat: FloatType

class WeatherItem(BaseModel):
    id: IntType
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: FloatType
    feels_like: FloatType
    temp_min: FloatType
    temp_max: FloatType
    pressure: IntType
    humidity: IntType
    sea_level: IntType
    grnd_level: IntType

class Wind(BaseModel):
    speed: FloatType
    deg: IntType
    gust: FloatType

class Clouds(BaseModel):
    all: IntType

class Sys(BaseModel):
    country: str
    sunrise: IntType
    sunset: IntType

class Model(BaseModel):
    coord: Coord
    weather: List[WeatherItem]
    base: str
    main: Main
    visibility: IntType
    wind: Wind
    clouds: Clouds
    dt: IntType
    sys: Sys
    timezone: IntType
    id: IntType
    name: str
    cod: IntType
