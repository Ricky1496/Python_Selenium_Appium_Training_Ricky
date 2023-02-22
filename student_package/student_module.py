class Student:
    SCHOOL_NAME = None
    SCHOOL_ADDRESS = None

    def __init__(self, student_id=None, student_name=None, student_mailid=None, student_percentage=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage


    def get_stud_name(self):
        return  self.student_name

    @property
    def get_stud_percentage(self):
        return  self.student_percentage

    @property
    def get_name_with_percentage(self):
        return f"Hi, {self.student_name}, your percentage is {int(self.student_percentage)}%"

    @staticmethod
    def get_school_details():
        return f"Address of {Student.SCHOOL_NAME} is {Student.SCHOOL_ADDRESS}"


    def print_grade(self):
        if self.student_percentage > 100 or self.student_percentage < 0:
            print("Invalid Input..!")
        elif self.student_percentage >= 90:
            print("Grade A")
        elif self.student_percentage >= 75:
            print("Grade B")
        elif self.student_percentage >=60:
            print("Grade C")
        elif self.student_percentage >= 45:
            print("Grade D")
        elif self.student_percentage < 45:
            print("Failed..!")
