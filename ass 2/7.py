
def par(name,birthyear,weight):
    today = 2022
    age = today-birthyear
    print("your age is", age )

    namme = name
    if namme == "":
        namme = "desire"
   
             
    print("you are", namme,  "your weight is", weight, "age is",age)

weight = int(input("Enter your weight"))
namme = str(input("what is your name?"))
par(namme,2002,weight)
