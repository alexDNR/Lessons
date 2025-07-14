def get_formatted_name(first_name, middle_name, last_name):
    """ Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()  # возвращает значение fill_name

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



def build_person(first_name, last_name):
    """ Возвращает словарь с информацией о человеке"""
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
