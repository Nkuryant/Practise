def add_user():
    active=True
    censor_name="""1234567890!@#$%^\"&*()_+\|/№;%:?  """
    while active:
        correct_input=True        
        while correct_input:        
            name=str(input("Введите ваше имя:"))
            name=name.strip()
            name=name.title()
            if name.lower() == "выход":
                active=False
                correct_input=False
                break
            for letter in censor_name:
                if name.find(letter)>-1:
                    print("Недопустимый символ в имени")
                    correct_input=False
                    break
            if len(name)<=1:
                print("Короткое имя ¯\_(0_0)_/¯")
                correct_input=False
            elif len(name)>16:
                print("Слишком длинное имя ¯\_(0_0)_/¯")
                correct_input=False
            else:
                break                   
        while correct_input:
            age=str(input("Введите ваш возраст:"))
            if age.lower() == "выход":
                active=False
                correct_input=False
                break
            if age.isdigit():
                if int(age) not in range(0,121):
                    print("Некоректный возраст")
                    correct_input=False
                else:
                    break
            else:
                print("Некоректное число")
                correct_input=False
        if correct_input:
            with open("users.txt","a") as file_obj:
                file_obj.write("<name=%s:age=%s>\n"%(name,age))
                print("Пользователь добавлен")
                active=False
                
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
    else:
        print("Такой команды нет")
def show_instruction():
            print("""\nДля того чтобы добавить в базу пользователя - напишите 'добавить'
Для просмотра пользователей напишите 'просмотр'
Для выхода из команд бота напишите 'выход'
              """)


