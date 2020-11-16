x1 = int(input("Give a number: "))
x2 = int(input("Give a number: "))
countOfMatcDigits = 0

while x1 > 0 and x2 > 0:
  if x1 % 10 == x2 % 10:
    countOfMatcDigits += 1
  x1 //= 10
  x2 //= 10

print(countOfMatcDigits)

