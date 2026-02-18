name = input("Enter student name:")
roll_no =input("Enter student roll number:")
age = int(input("Enter age :"))

sub1=int(input("Enter marks of subject1:"))
sub2=int(input("Enter marks of subject2:"))
sub3=int(input("Enter marks of subject3:"))
sub4=int(input("Enter marks of subject4:"))
sub5=int(input("Enter marks of subject5:"))

total_marks=sub1+sub2+sub3+sub4+sub5
average=total_marks/5
percentage=(total_marks/500)*100

print("\n-----------STUDENT RESULT------------")
print(f"name        :{name}")
print(f"Roll_no     :{roll_no}")
print(F"Age         :{age}")
print(f"total       :{total_marks}/500")
print(f"Average     :{average}")
print(f"percentage  :{percentage:.2f}%")
print("---------------------------------------")
