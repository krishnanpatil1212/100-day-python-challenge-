print("=====STUDENT RESULT SYSTEM=====\n")

name = input("Enter student name:")
roll_no = input("Enter student roll number:")
age = int(input("Enter student age:"))

sub1=int(input("Enter marks for subject1:"))
sub2=int(input("Enter marks for subject2:"))
sub3=int(input("Enter marks for subject3:"))
sub4=int(input("Enter marks for subject4:"))
sub5=int(input("Enter marks for subject5:"))

total=sub1+sub2+sub3+sub4+sub5
percentage = (total/500)*100

if percentage>+40:
    result="PASS"
else:
    reult="FAIL"

if percentage>=90:
    grade="A+"
elif percentage>=75:
    grade="A"
elif percentage>=60:
    grade="B"
elif percentage>=40:
    grade="c"
else:
    grade="F"

if percentage>=85 and result=="PASS":
    scholarship ="yes"
else:
    scholarshiip="N0"

print("\n==========STUDENT REPORT===============")
print(f" Name             :{name}")
print(f"Roll_no           :{roll_no}")
print(f"Age               :{age}")
print(f"TOtal marks       :{total}/500")
print(f"Percentage        :{percentage:.2f}%")
print(f"Result            :{result}")
print(f"Grade             :{grade}")
print(f"Scholarship       :{scholarship}")
print("=========================================")

