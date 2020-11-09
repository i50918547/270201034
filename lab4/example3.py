year = int(input("Write the year: "))

if year%4 == 0:
     if year%100 == 0:
          if year%400 ==0:
            is_leap_year = True
          else: 
            is_leap_year = False
      else:
        is_leap_year = True
else:
  is_leap_year = False


if is_leap_year:
  print(year, "is a leap year.")
else: 
  print(year, "is not a leap year.")
  