class Student:
    def __init__(self, name:str, marks:list):
        self.set_name(name)
        self.set_marks(*marks)
    def set_marks(self, e1, e2, e3):
         self.e1 = e1
         self.e2 = e2
         self.e3 = e3

    def set_name(self, name):
        self.name = name
    def get_average_mark(self):
        print(self.name, ' - ', ((self.e1 + self.e2 + self.e3) / 3))


for i in range(int(input('Enter number of students: '))):

        name = input('\nStudent #{}\nEnter student\'s name: '.format(i+1))
        marks = [int(mark) for mark in input('Enter student\'s marks (separated by space): ').split()]
        Student(name, marks).get_average_mark()
