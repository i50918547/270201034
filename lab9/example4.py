import time

def recursive_timer(n):
  if n == 0:
    print("The end")
    return None

  print(f"time remaining: {n}")
  time.sleep(1)
  return recursive_timer(n - 1)

recursive_timer(6)  