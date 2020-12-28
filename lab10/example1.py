def multiply_by_3(n):
  if n == 1:
    return 3
  else:
    return 3 + multiply_by_3(n-1)

print(multiply_by_3(5))