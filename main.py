from lesson_3 import UserService, User

user_service = UserService()

new_user1 = User(name="Isko", email="isko1@gmail.com", age=20)
user_service.add_user(new_user1)

new_user2 = User(name="Biloliddin", email="1dreammer@mail.ru", age=16)
user_service.add_user(new_user2)

new_user3 = User(name="Sodiq_Sariq", email="abdurasuljanovmuhammadsodiq@gmail.com", age=16)
user_service.add_user(new_user2)

found_user = user_service.find_user_by_email("isko1@gmail.com")
if found_user:
    print(f"Пользователь найден: {found_user.name}, {found_user.email}, {found_user.age}")

user_service.delete_user("abdurasuljanovmuhammadsodiq@gmail.com")
print("Пользователь удален")

user_service.close()
