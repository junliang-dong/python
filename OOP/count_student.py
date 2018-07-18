# _*_ coding: utf-8 _*_
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1 

a = Student("Lily")
b = Student("Bob")
c = Student("c")
print(Student.count)
