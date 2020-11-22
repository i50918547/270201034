desired = int(input("How many number do you want? :"))

n1 = 1 
n2 = 1
count = 0

while desired > count:
  print(n1)
  n3 = n2 + n1
  n1 = n2
  n2 = n3
  count += 1

  