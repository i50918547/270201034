num_of_lectures = int(input("Lecture Number:"))
gpa_ = float(input("Write your GPA: "))
if gpa_ < 2.0:
  if num_of_lectures < 47.0:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if num_of_lectures < 47.0:
    print("Not enough number of lectures!")
  else: 
    print("Graudated!")
