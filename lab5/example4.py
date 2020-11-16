staticPassw = "ceng113"

while True:
    p = input("Enter password: ")
    if (p == staticPassw):
         print("Welcome")
         break
    elif (p == "help"):
         print(staticPassw[0])
    else:
         print("Wrong")