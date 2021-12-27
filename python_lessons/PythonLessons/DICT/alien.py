alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()
print('НОВОЕ ЗАДАНИЕ!!')
print()
aliens = [] # создание пустого списка для хранения пришельцев
for alien_number in range(30): # создаём 30 зелёных пришельцев
    if (alien_number % 2 == 0):
        new_alien = {'color':'yellow', 'points':10, 'speed':'medium'}
    elif (alien_number % 3 == 0):
        new_alien = {'color':'red', 'points':15, 'speed':'fast'}
    else:
        new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

print ("Общее количесво пришельцев: " + str(len(aliens)))
#----------------------------------------------------------
for alien in aliens[:5]:# выводим первых 5 пришельцев, они все одинаковые
    print(alien)        
