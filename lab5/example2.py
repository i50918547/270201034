numNums = int(input("How many numbers? : "))
evens = 0
for i in range(numNums):
  ints = int(input("Enter an integer: "))
  if ints % 2 == 0:
     evens += 1


print(evens/numNums * 100, "%")

