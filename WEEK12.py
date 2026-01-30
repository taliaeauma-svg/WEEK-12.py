class Course:
    def __init__(self, code, name):
        self.courseCode = code
        self.courseName = name


class Student:
    def __init__(self, regNo, name, course):
        self.regNo = regNo
        self.name = name
        self.course = course   # Association


class Registration:
    def registerStudent(self, student):
        print("Student", student.name,
              "registered for",
              student.course.courseName)


course1 = Course("CIT2210", "Computer Programming II")
student1 = Student("ENC222-0246/2024", "Talia Auma", course1)

reg = Registration()
reg.registerStudent(student1)