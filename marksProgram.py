marks = int(input("Enter the marks :"))
if marks > 100 or marks < 0:
    print("invalid input")
elif marks >=80:
    print("Grade A")
elif marks >=60 :
    print("Grade B")
elif marks >=40:
    print("Grade C")
else:
    print("Fail")
