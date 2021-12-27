# начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# проверяем каждого пользователя, пока остаются непроверенные пользователи
# Каждый пользователь, прошедший проверку, перемещается в список проверенных
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# вывод всех проверенных пользователей
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# print(unconfirmed_users) ----- непроверенные пользователи теперь пустой список
