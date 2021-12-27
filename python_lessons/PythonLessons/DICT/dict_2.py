favorite_lang = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name in sorted(favorite_lang.keys()): # циклом выводим только ключи словаря
    print(name.title() + ", спасибо тебе за изучение!")
                                    # для этого исп. метод keys()
print()
for lang in favorite_lang.values(): # выводим циклом только значения словаря
    print(lang.title())             # для этого исп. метод values()
print()
for lang in set(favorite_lang.values()):
    print(lang.title())             # выводим значения словаря без возможных повторений
print()
print("НОВОЕ ЗАДАНИЕ!!!!!")
print()
rivers = {
    'dnepr':'ukrane',
    'volga':'russia',
    'rein':'germany',
    'nile':'egypt',
    }
# выводим сообщения с упоминанием названия реки и в какой стране течёт
for river, country in rivers.items():
    print("The " + river.title() + " runs though " + country.title())
print()
#выводим названия рек, которые есть в словаре RIVERS
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
    

    
