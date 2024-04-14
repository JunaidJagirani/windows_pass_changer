import subprocess as sp
import ctypes
import os
import sys

def title():
    print("****************************")
    print("* Windows Password Changer *")
    print("*       Written by         *")
    print("*     Junaid Jagirani      *")
    print("****************************")
def is_user_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
def get_users():
    if sys.platform == "win32" or sys.platform == "cygwin":
        user_list = set(os.listdir("c://Users"))
        not_allowed = set(["All Users", "Default", "Default User", "desktop.ini", "Public"])
        users = list(user_list - not_allowed)  # subtratcting sets
        return users
    else:
        print("I did not support this platform")
def main():
    title()
    user_num = 0
    current_user = sp.os.getlogin()  #get current user name
    print("Checking for privileges")
    if is_user_admin():
        print("[+] You have admin privileges")
        users = get_users()
        for i in users:
            print(f"{user_num+1}. {i}")
            user_num+=1
        print("Enter your choice : ",end=" ")
        choice = input()
        try:
            choice=int(choice)
            if choice<=0:
                raise ValueError
        except ValueError:
            print("Invalid input")
            sys.exit()
        try:
            user_selected = users[choice - 1]
            print(f"User => {user_selected}")
            print("Enter your password (default=empty) : ",end=" ")
            password = input()
            if password=="":
                print("Password => [none]")
            else:
                print(f"Password => {password}")
            cmd = "net user \""+user_selected+"\" \""+password+"\""
            # print(cmd)
            output = sp.call(cmd, shell=True)
            print(output)
        except IndexError:
            print("Out of range")
            sys.exit()
    else:
        print("[!] You have no admin privileges")
        print("[!] You need admin privileges to continue")
if __name__ == '__main__':
    main()
