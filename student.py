class student:
    courseMarks = {}
    name = ""

    def __init__(self, name, family):
        self.name = name
    
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        int markSum
        for mark in courseMarks:
            markSum =+ mark
        return markSum / courseMarks.len()

