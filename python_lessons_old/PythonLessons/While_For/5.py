# программа выводит весь список из sandwich_orders с текстом.
# потом переписывает этот список в другой и выводит его
sandwich_orders = ['1', '2', '3', '4', '5', '6', '7']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made sandwich " + current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

# выводим новый список
# так у нас новый список формировася последний элемент на первое место
# в цикле используем [-1::-1] с последнего элемента до первого с шагом -1
for sandwich in finished_sandwiches[-1::-1]:
    print("Finished sandwiches: " + sandwich.title())

print(sandwich_orders)
print()
print("Новое задание")
print()
sandwich_orders = ['1', 'pastrami', '3', 'pastrami', '5', 'pastrami', '7']
non_pastrami_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    non_pastrami_sandwiches.append(current_sandwich)
for sandwich in non_pastrami_sandwiches[-1::-1]:
    print(sandwich)
