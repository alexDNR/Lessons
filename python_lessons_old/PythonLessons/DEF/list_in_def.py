# Список моделей, которые необходимо напечатать
unprinted_designs = ['iphone case', 'robot pedant', 'dodecahedron']
complited_models = []

# Цикл последовательно печатает каждую модель до конца списка
# После печати каждая модель перемещается в список complited_models
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Печать модели на 3D принтере
    print("Printing model: " + current_design)
    complited_models.append(current_design)

# Вывод всех готовых изделий
print("\nThe following models have been printed:")
for complited_model in complited_models:
    print(complited_model)




# Теперь создаём такую же программу, только с использованием функции
#
#

print()
print()
print()

#
#
#

def print_models(unprinted_designs, complited_models):
    """
    имитирует печать моделей, пока список не станет пустым
    Каждая модель после печати перемещается в complited_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Имитация печати на 3D принтере
        print("Printed model: " + current_design)
        complited_models.append(current_design)

def show_complited_models(complited_models):
    """ Выводи инфу о напечатанных изделиях """
    print("\nThe following models have been printed:")
    for complited_model in complited_models:
        print(complited_model)

unprinted_designs = ['iphone case', 'robot pedant', 'dodecahedron']
complited_models = []
print_models(unprinted_designs, complited_models)
show_complited_models(complited_models)

        
