# Сохранение информации о заказанной пицце
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese']
    }

# описание заказа
print("You ordered a " + pizza['crust'] + "- crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
