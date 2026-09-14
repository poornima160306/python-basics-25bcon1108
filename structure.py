class Student:
    def _init_(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


s1 = Student("PARTH", 101, "60")

print("Name:", s1.name)
print("Roll:", s1.roll)
print("Marks:", s1.marks)