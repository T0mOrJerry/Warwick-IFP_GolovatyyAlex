class Student:
    def __init__(self, name, id, group):
        self.name = name
        self.id = id
        self.group = group

    def __str__(self):
        return f'Student {self.name} with id {self.id} studies in class group {self.group}'


common_student = Student('Alex', 5583329, 4)
print(common_student)
