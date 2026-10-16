class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = 0
        self.set_age(age)

    #setter and getter methods for name
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    #setter and getter methods for age
    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

myStudent = Student("Sir JM", 33)
myStudent.set_name("Ma'am Hannah")
myStudent.set_age(20)
print(myStudent.get_name())
print(myStudent.get_age())
