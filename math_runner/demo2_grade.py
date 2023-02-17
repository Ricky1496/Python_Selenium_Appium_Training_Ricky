def Grades(marks):
    if 90 <= marks <=100:
        print("Grade A")
    elif 80 <= marks <= 89:
        print("Grade B")
    elif 60 <= marks <= 79:
        print("Grade C")
    elif marks < 60 or marks >= 35:
        print("Grade F")
    elif marks > 0:
        print("Invalid..!")

