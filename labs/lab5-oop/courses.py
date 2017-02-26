class Course:
    def __init__(self, department, number, title, *instructors):
        self.department = department
        self.number = number
        self.title = title
        self.students = set()
        self.instructors = list(instructors)

    def __repr__(self):
        return '{}{}:"{}"'.format(self.department, self.number, self.title)

    def mark_attendance(self, *students):
        for student in students:
            self.students.add(student)

    def is_present(self, student):
        return student in self.students

    def __le__(self, other):
        return int(self.number) <= int(other.number)


class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded