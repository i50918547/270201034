a = -2
b = a**2+1
print(a,b)
c = b**3//2
d = c%b
print(c,d)
if a + d != 0:
  a += 3
else:
  a -= 3
  c = 1
print(a, b, c, d)
