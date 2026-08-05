# Create  a multiple Object And Show Theri details
class Collage:
    c_name="Shivaji University Kolhapur"
    def __init__(self,s_name,s_id,s_marks):
        self.s_name=s_name
        self.s_id=s_id
        self.s_marks=s_marks
object1=Collage("Swapnil",202,98)
print(object1.s_id)
object2=Collage("Rahul",201,99)
print(object2.s_name)