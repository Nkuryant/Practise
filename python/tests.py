import unittest
def add_user(name,age):
    correct_input=True
    active=True
    censor_name="""1234567890!@#$%^\"&*()_+\|/№;%:?  """         
    name=name.strip()
    name=name.title()
    if name.lower() == "выход":
        active=False
        correct_input=False
    for letter in censor_name:
        if name.find(letter)>-1:
            return False
            correct_input=False
            break
    if len(name)<=1:
        return False
        correct_input=False
    elif len(name)>16:
        return False
        correct_input=False              
    if age.lower() == "выход":
        active=False
        correct_input=False
    if age.isdigit():
        if int(age) not in range(0,121):
            return False
            correct_input=False
    if correct_input:
        with open("users.txt","a") as file_obj:
            return True
                

class NameTestCase(unittest.TestCase):
    def test1(self):
        test1=add_user("vl@d","140")
        self.assertEqual(test1,False)
    def test2(self):
        test2=add_user("vlad","15")
        self.assertEqual(test2,True)
    def test3(self):
        test3=add_user("vlad","150")
        self.assertEqual(test3,False)
    def test4(self):
        test4=add_user("","10")
        self.assertEqual(test4,False)
unittest.main()

