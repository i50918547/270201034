def is_prime(n):
  if n <= 1:
    return False
  for x in range(2,n):
    if n % x == 0:
      return False
  return True

def print_primes_between(n,m):
  for x in range(n, m)
    if is_prime(x):
      print(x)

first = int(input("First:"))
last = int(input("Last:"))
print_primes_between(first,last)
