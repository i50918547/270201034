age = int(input("Write your age: "))
Normal_bus_ticket = 3
Discount_value = 0.5
if 6 <= age <= 60:
  if 6 <= age <= 18:
    print(Normal_bus_ticket * (1 - Discount_value))
  else:
    print("Ticket is 3 TL")
else:
  print("Ticket is free!")



