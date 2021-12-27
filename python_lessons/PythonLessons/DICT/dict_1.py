favorite_lang = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name, lang in favorite_lang.items(): # выводим полностью словарь
    print(name.title() + "s любимый язык программирования - " +
          lang.title() + ".")

for name in favorite_lang.keys():  # выводим только ключи словаря, без значений, на которые ключи указывают
    print(name.title())

for name in favorite_lang:  # аналогична предыдущей записи, цикл по умолчанию перебирает ключи словаря
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_lang.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + " Я вижу твой любимый язык программирования " +
              favorite_lang[name].title() + "!")
