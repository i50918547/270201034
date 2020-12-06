tuple = [("Jon", 15), ("Ned", 45), ("Arya", 9), ("Catelyn", 44), ("Bran", 10)]

for i in range(len(tuple)):
  if tuple[i][1] > 18:
    print(tuple[i][0])
