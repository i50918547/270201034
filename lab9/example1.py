def harmonic(n):
  if n == 0:
    return 0
  else:
    return 1/n + harmonic(n-1)

print(harmonic(5))