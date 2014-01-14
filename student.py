class Student:
    courseMarks = {}
    name = ""

    def __init__(self, name, family):
        self.name = '%s %s' % (name, family)

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        if len(self.courseMarks) > 0:
            markSum = 0
            for course in self.courseMarks:
                markSum += self.courseMarks[course]
            return markSum / len(self.courseMarks)
        else:
            print "No marks!"

john = Student('John', 'Lame')
print john.name
john.addCourseMark('CMPUT410', 87)
john.addCourseMark('CMPUT411', 97)
john.addCourseMark('CMPUT412', 77)
john.addCourseMark('CMPUT413', 76)
john.addCourseMark('CMPUT414', 95)
print "Average: %d" % john.average()

