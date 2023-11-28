import re

from networkx import selfloop_edges
class Signup():
    def __init__(self,fn,ln,un,pwd):
        self.fn = fn
        self.ln = ln
        self.un = un
        self.pwd = pwd
        self.Validate_password()

    def Validate_password(self):
        while True:
            if(
                len(self.pwd) < 8
                or len(self.pwd) > 16
                or not re.search(r"[a-z]",self.pwd)
                or not re.search(r"[A-Z]",self.pwd)
                or not re.search(r"\d",self.pwd)
                or not re.search(r"[1234567]",self.pwd)
                ):
                print("password does not match the criterial. Try again! ")
                self.pwd = input("Enter a new password :")
            else:
                print("password successfully set...")
                break
class SignIn():
    def __init__(self,un,pwd):

        self.un = un
        self.pwd = pwd

    def logincheck(self,Signup_obj):

        if self.un == Signup_obj.un and self.pwd == Signup_obj.pwd:
            print(f"welcome,{Signup_obj.fn}{Signup_obj.ln}!")
        else:
            print("Login credentials do not match.")
            

fn=input("Enter your first name:")
ln=input("Enter your last name:")
un=input("Enter your user name:")
pwd=input("Enter your password:")

Signup_obj = Signup(fn,ln,un,pwd)

un_input = input("Enter your username: ")
pwd_input = input("Enter your password: ")

signin_obj = SignIn(un_input,pwd_input)
signin_obj.logincheck(Signup_obj)






    