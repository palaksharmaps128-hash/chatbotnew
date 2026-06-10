class student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks


    def get_marks(self):
        return self.__marks


    def set_marks(self,value):
        if value >= 0:
            self.__marks = value
        else:
            print("invalid")


s1 = student("palak", 90)

print(s1.get_marks())

s1.set_marks(95)
print(s1.get_marks())