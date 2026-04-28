
class classroom:
    def __init__(self):
        self.list = []
    def add_name(self, name):
        self.list.append(name)
    def count_students(self):
        print(f"Number of students is: {len(self.list)}")
    
a = classroom()

a.add_name("ahmad")
a.add_name("magdy")

a.count_students()
