
file = open("demofile.txt", "w")
file.write("ask_me.py")
file.close()

#open and read the file after the appending:
file = open("demofile.txt", "r")
print(file.read());
username =str(input("Please Enter username:"))
print("Username is: " + username)
def hello():
    username=str(input("enter the name : "))
print("hello,how are you doing " + str(username))


