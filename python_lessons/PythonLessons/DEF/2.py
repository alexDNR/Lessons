def describe_pet(animal_type, pet_name):
    """Выводи информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "s name is " + pet_name.title() + ".")

describe_pet('сулсик', 'Ali')    # позиционные аргументы в функции
describe_pet(pet_name = 'ali', animal_type = 'суслик') # именованные аргументы

def describe_pet(pet_name, animal_type='dog'):
    """Выводи информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "s name is " + pet_name.title() + ".")

describe_pet('Ali', 'cat')
# даже если по умолчанию и стоит значение в параметре
# animal_type, можно задать ему другое значение
# Если вы используете значения по умолчанию, все параметры со
# значением по умолчанию должны
# следовать после параметров, у которых значений по умолчанию нет .
# Это необходимо для того,
# чтобы Python правильно интерпретировал позиционные аргументы .
describe_pet(pet_name = 'ali') # именованные аргументы
