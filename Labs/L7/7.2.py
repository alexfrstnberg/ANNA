# Additional class 'Lab'
class Lab:
    def __init__(self, maxMark):
        self.attempts = 0
        self.mark = 0
        self.maxMark = maxMark
    
    def setMark(self, mark):
        if mark <= self.maxMark and mark > 0:
         self.attempts += 1
         self.mark = mark
        else:
            print('Mark {} is bigger than max.'.format(mark))

# Class for student managing
class Student:
    def __init__(self, name, maxIndMark, maxLabMark, countOfLabs, marksForAuto):
        self.name = name
        self.marksForAuto = marksForAuto
        self.journal = []
        self.individual = Lab(maxIndMark)
        for i in range(countOfLabs):
            self.journal.append(Lab(maxLabMark))
    
    def getMarks(self):
        marks = []
        for item in self.journal:
            marks.append(getattr(item, 'mark'))
        return marks

    def getIndividual(self):
        return getattr(self.individual, 'mark')
    
    def setLabMark (self):
        indexOfLab = int(input('--------\nEnter id of lab which you need: '))
        mark = int(input('Enter mark for lab: '))
        if indexOfLab >= len(self.journal):
            print('Exercise with index {} doesn\'t exist.'.format(indexOfLab))
            return -1
        getattr(self.journal[indexOfLab], 'setMark')(mark)
        print('--------')

    def setAllLabs(self):
        for _ in range(len(self.journal)):
            self.setLabMark()
    
    def setIndividualMark (self):
        mark = int(input('--------\nEnter mark for individual lab: '))
        getattr(self.individual, 'setMark')(mark)
        print('--------')

    def Summary (self):
        Sum = sum(self.getMarks()) + self.getIndividual()
        if Sum >= self.marksForAuto:
            print('All marks sum is \'{}\'. It\'s enough for auto.'.format(Sum))
        else:
            print('All marks sum is \'{}\'. It\'s not enough for auto.'.format(Sum))

    def printMarks (self):
        print('Marks: {marks}\nIndividual: {individual}'.format(
            marks = self.getMarks(),
            individual = self.getIndividual()))


name = input('Enter the student\'s name: ')
countOfLabs = int(input('Enter the count of lab works: '))
maxLabEx = int(input('Enter the max mark for lab work: '))
maxIndEx = int(input('Enter the max mark for individual lab work: '))
marksForAuto = int(input('Enter the required count of marks for auto: '))
student = Student(name, maxIndEx, maxLabEx, countOfLabs, marksForAuto)

student.printMarks()
student.setIndividualMark()
student.setAllLabs()
student.Summary()

