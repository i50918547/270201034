# ax**2 + bx + c  
a = int(input("Write a of equation:"))
b = int(input("Write b of equation:"))
c = int(input("Write c of equation:"))
roots = ((-b + b**2 - 4*a*c)**0.5 / 2*a) , ((-b - b**2 - 4*a*c)**0.5 / 2*a) 
discr = b**2 - 4*a*c   
if discr > 0 :
  print("There are two real roots: " , roots)
elif discr == 0 :
  print("There is one real root: " , roots)
elif discr < 0 :
  print("There are two complex roots: " , roots)



