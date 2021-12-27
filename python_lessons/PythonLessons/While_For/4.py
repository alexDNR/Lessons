# Программа, которая запрашивает имя участника и его ответ
responses = {}
answer = 120
# Установка влага продолжения опроса
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя
    name = input("\nWhat is your name? ")
    response = input("Сколько будет факториал 5? ")

    # Ответы сохраняем в словаре
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input("Кто-нибудь ещё гoтов ответить?(yes/no)")
    if repeat == 'no':
        polling_active = False

# Опрос завершён, нужно вывести результаты
print("\n--- Poll results ---")
for name, response in responses.items():
    print(name.title() + ", Ваш ответ: " + response + ".")


