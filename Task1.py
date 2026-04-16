Student_name=input("Enter name of student=")
TotalMarks=500
ObtainedTotal_marks=0
for i in range(5):
   Marks=int(input(f"Enter marks obtained for subject {i+1} ="))
   ObtainedTotal_marks=ObtainedTotal_marks+Marks

print(f"Student name = {Student_name}")
print(f"Toatl marks obtained={ObtainedTotal_marks} ")
Percentage=int((ObtainedTotal_marks/TotalMarks)*100)
print(f"Percentage obtained= {Percentage}%")
if Percentage>=90:
   print("Grade obtained is A")
elif Percentage>=80 and Percentage<=89:
   print("Grade obtained is B")
elif Percentage>=70 and Percentage<=79:
   print("Grade obtained is C")
elif Percentage>=60 and Percentage<=69:
   print("Grade obtained is D")
else:
   print("Grade F is obtained")
