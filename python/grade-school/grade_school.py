class School:
    def __init__(self):
        self.classes = {}

    def add_student(self, name, grade):
        self.studentGrade = grade
        self.name = name
        self.classes.setdefault(self.studentGrade,[]).append(self.name)

    def roster(self):
        roster = []
        for x in sorted(self.classes.keys()):
            roster += sorted(self.classes[x])
        return roster

    def grade(self, grade_number):
        self.grade_number = grade_number
        return sorted(self.classes[self.grade_number]) if self.grade_number in self.classes else []