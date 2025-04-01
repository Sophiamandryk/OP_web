import dvv
import json


class Course:
    name: str
    capacity: int
    prerequisites: dict[str, int]

    def __init__(self, name: str, capacity: int, prerequisites: dict[str, int]):
        self.name = name
        self.capacity = capacity
        self.prerequisites = prerequisites


class Student:
    name: str
    number: int
    __scores: dict[str, float]
    prioritization: dict[str, int]

    def __init__(self, name: str, number: int, scores: dict[str, float], prioritization: dict[str, int]):
        self.name = name
        self.number = number
        self.__scores = scores
        self.prioritization = prioritization

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
    
    def set_scores(self, scores: dict[str, float]):
        for course_name, score in scores.items():
            self.__scores[course_name] = score


    def rating_by_score(self, course:Course) -> float:
        summ = 0
        weights = 0
        for course_name, value in course.prerequisites.items():
            summ += self.__scores[course_name] * value
            weights += value
        return summ / weights


class RegistrationProcessor:
    __registrations_pathname: str
    __courses_pathname: str
    students: list[Student]
    courses: list[Course]

    def __init__(self, registrations_pathname: str, courses_pathname: str):
        self.__registrations_pathname = registrations_pathname
        self.__courses_pathname = courses_pathname
        self.students = self.__process_students()
        self.courses = self.__process_courses()

    def __process_students(self) -> list[Student]:
        registrations = dvv.read_file(self.__registrations_pathname)
        student_list = []
        for student_name, student_info in registrations.items():
            student = Student(student_name, student_info['Number'],
                              student_info['Scores'], student_info['Prioritization'])
            student_list.append(student)
        return student_list

    def __process_courses(self) -> list[Course]:
        courses_list = []
        with open(self.__courses_pathname, "r", encoding='utf-8') as file:
            data = json.load(file)
            for course_name, course_info in data.items():
                course = Course(course_name, course_info['capacity'], course_info['prerequisites'])
                courses_list.append(course)
        return courses_list


if __name__ == '__main__':
    processor = RegistrationProcessor('/Users/sofiyamandryk/Desktop/OP3/mini_regestration.txt', '/Users/sofiyamandryk/Downloads/courses_data.json')
    print(str(processor.students))
    assert str(processor.students) == '[Linda Wilson, Robert Rodriguezes, Mary Miller]'
    assert set(dvv.read_file('/Users/sofiyamandryk/Desktop/OP3/mini_regestration.txt').keys()) == {student.name for student in processor.students}
    assert dvv.read_file('/Users/sofiyamandryk/Desktop/OP3/mini_regestration.txt') == {
        student.name: {'Number': student.number, 'Scores': student.scores, 'Prioritization': student.prioritization} for
        student in processor.students}
    assert dvv.PREREQUISITES == {course.name: course.prerequisites for course in processor.courses}
    assert dvv.CAPACITY == {course.name: course.capacity for course in processor.courses}
