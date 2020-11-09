num1 = int(input("Write a number: "))
num2 = int(input("Write a number: "))
num3 = int(input("Write a number: "))
if num1<num2:
  if num1<num3:
    print("Minimum:" , num1)
  else:
    print("Minimum:" , num3)
else: 
  if num1 < num3:
    print("Minimum:" , num2)
  else: 
    print("Minimum:" , num3)
  
     
              