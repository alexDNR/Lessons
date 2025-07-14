HELP = """
1. help - напечатать справку по программе
2. add - добавить задачу в список (название задачи запрашиваем у пользователя)
3. show - напечатать все добавленные задачи. 
4. exit - выход из программы. 
5. save - сохранения даты и задач в файл"""

def show(): #функция - показать данные по дате
    date = input("Введите дату для отображения списка задач: ").lower().rstrip().lstrip()
    if date in tasks:
        for task in tasks[date]:
            print("- ", task)
    else:
        print("Такой даты в списке задач не указано!")  

def add(): # добавить задачу и дату задачи
    date = input("Введите дату выполнения задачи: ").lower().rstrip().lstrip()
    task = input("Введите название задачи: ")
    if date in tasks:
        # Дата есть в словаре
        # Доабвляем задачу в словарь
        tasks[date].append(task)
    else:
        # Иначе, создаём запись с ключём [date]
        tasks[date] = []
        tasks[date].append(task)
    print("Задача --- ", task, " --- добавлена на дату --- ", date)

def save(): #сохранение списка задач с датами в файл
    with open("tasks.txt", 'w', encoding='utf-8') as file:
        for key, value in tasks.items():
            file.write('{}:{}\n'.format(key, value))

tasks = {}

while True:
    command = input("Введите команду: ").lower().rstrip().lstrip()
    if command == "help":
         print(HELP)
    elif command == "show":
        show()
    elif command == "add":
        add()
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break   
    elif command == "save":
        save()
        print("Даты и задачи записаны в файл")        
    else:
        print("Неизвестная команда")
        break


      