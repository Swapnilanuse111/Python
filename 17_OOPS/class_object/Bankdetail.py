class student:
    name="swapnil"
    roll_number=102
    marks=90
    def Display(self):
        print("Student Name:-",self.name)
        print("Student Roll Number:-",self.roll_number)
        print("Student Marks:-",self.marks)

obj=student()
print(obj.Display())