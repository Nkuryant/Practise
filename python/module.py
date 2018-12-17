def add_user():
    flag_1=True
    censor_name="""1234567890!@#$%^\"&*()_+\|/№;%:?  """
    flag_user=True
    while flag_user:        
            flag_1=True
            name=str(input("Введите имя:"))
            name=name.strip()
            if name.lower() == "выход":
                break
            if len(name)>1 and len(name) < 16:
                for letter in name:
                    if letter in censor_name:
                        print("Ошибка ввода имени")
                        flag_1=False
                        break
                if flag_1 ==  True:
                    name=name.title()
                    age=str(input("Введите ваш возраст:"))
                    if age == "выход":
                        break
                    elif age.isdigit():
                        if int(age) in range(0,121):
                            with open("users.txt","a") as file_obj:
                                file_obj.write("<name=%s:age=%s>\n"%(name,age))
                                print("Пользователь добавлен")
                                flag_user=False
                        else:
                            print("Ошибка ввода возраста")
                    else:
                        print("Ошибка ввода возраста")
            else:
                print("ошибка ввода имени")
def watch_users():    
    with open("users.txt") as file_obj:
        all_users=file_obj.readlines()
    choice_users=str(input("всех\по имени?:"))
    if choice_users.lower() == "всех":
        print()
        for i in range(len(all_users)):
            curr_row=all_users[i]
            print("Пользователь %s, возраст %s лет"%(curr_row[6:curr_row.find(":")],curr_row[curr_row.find(":")+5:curr_row.find(">")]))
    elif choice_users.lower() == "по имени":
        searching_users=[]
        searching_name=str(input("По какому имени ищем?:")).title()
        for row in (all_users):
            if row.find(searching_name) > 1:
                searching_users.append(row)
        if len(searching_users) == 0:
            print("Пользователей с таким именем не найдено")
        else:
            print()
            for i in range(len(searching_users)):
                curr_row=searching_users[i]
                print("Пользователь %s, возраст %s лет"%(curr_row[6:curr_row.find(":")],curr_row[curr_row.find(":")+5:curr_row.find(">")]))
                
def show_instruction():
            print("""\nДля того чтобы добавить в базу пользователя - напишите 'добавить'
Для просмотра пользователей напишите 'просмотр'
Для выхода из команд бота напишите 'выход'
              """)

