users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }

for username, user_info in users.items(): # перебираем все значения в словаре
    print("\nUsername: " + username)    # выводим значение ключа
    full_name = user_info['first'] + " " + user_info['last'] # создаём переменную в которую записываем ФИО
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tlocation " + location.title())
