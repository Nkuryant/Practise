import os, module, time
try:
    with open("users.txt") as file_obj:
        all_users=file_obj.readlines()
except FileNotFoundError:
    with open("users.txt","w") as file_obj:
        pass
    with open("users.txt") as file_obj:
        all_users=file_obj.readlines()
while True:
    choice=str(input("Что вы хотите от бота?:"))
    if choice.lower() == "добавить":
        module.add_user()
        time.sleep(1)
        os.system("cls")
    elif choice.lower() == "просмотр":
        module.watch_users()
        time.sleep(4)
        os.system("cls")        
    elif choice.lower() == "инструкция":
        module.show_instruction()
        time.sleep(5)
        os.system("cls")
    elif choice.lower() == "выход":
        os.system("exit")
    else:
        print("Такой команды нет")
        time.sleep(1)
        os.system("cls")
