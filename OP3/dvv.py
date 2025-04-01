CAPACITY = {'Responsible AI': 25,
            'AI, Decision Making, and Society': 10,
            'Representation, Inference, and Reasoning in AI': 15}

PREREQUISITES = {
    'Responsible AI': {
        'Fundamentals of Programming': 40,
        'Linear Algebra': 30,
        'Probability and Statistics': 30},
    'AI, Decision Making, and Society': {
        'Worldview core': 40,
        'Decision Making': 40,
        'Fundamentals of Programming': 20},
    'Representation, Inference, and Reasoning in AI': {
        'Introduction to Algorithms': 40,
        'Probability and Statistics': 40,
        'Data Visualisation': 20}}


def read_file(filename):
    '''
    Read file with registrations and
    return this information as a dictionary.
    'Number' is the ordinal number at the moment of registrations.
    For our file Robert Wilson was the first, and James Davis
    was the last (therefore it has number 50).
    'Scores' are the scores of students for corresponding
    prerequisites.
    'Prioritization' is a prioritization of the corresponding students.
    >>> read_file('registrations.txt')['James Davis'] == \
    {'Number': 50, 'Scores': {'Fundamentals of Programming': 70, \
'Linear Algebra': 63, 'Probability and Statistics': 71, 'Worldview core': 65, \
'Decision Making': 82, 'Introduction to Algorithms': 72, 'Data Visualisation': 93}, \
'Prioritization': {'AI, Decision Making, and Society': 1, \
'Representation, Inference, and Reasoning in AI': 2, 'Responsible AI': 3}}
    True
    '''
    registrations = dict()
    student_time = list()
    with open(filename, 'r') as reg_file:
        name = ""
        time = ""
        info = dict()
        line = reg_file.readline()
        while line:
            if "Date and Time" in line:
                time = line.strip().split(": ")[1]
            if "Name" in line:
                name = line.strip().split(": ")[1]
            if "Prioritization of Subjects" in line:
                subjs = line.strip().split(": ")[1].split("; ")
                info["Prioritization"] = dict()
                for s in subjs:
                    key = s.split(". ")[1]
                    value = int(s.split(". ")[0])
                    info["Prioritization"][key] = value
            if "Scores" in line:
                info["Scores"] = dict()
                line = reg_file.readline()
                while "-" in line:
                    subject, score = line.strip().split(": ")
                    subject = subject[2:]
                    info["Scores"][subject] = int(score)

                    line = reg_file.readline()

            if line == "\n":
                student_time.append((name, time))
                registrations[name] = info

                name = ""
                time = ""
                info = dict()

            line = reg_file.readline()

    if name != "":
        student_time.append((name, time))
        registrations[name] = info

    student_time = sorted(student_time, key=lambda x: x[1])
    for i, (student, _) in enumerate(student_time):
        registrations[student]["Number"] = i + 1

    return registrations


def selection(registration):
    '''
    Make selection of students based on
    the registration information (please, read the
    corresponding algorithm on CMS).
    Returns the dictionary, where the keys are subjects to choose
    and values are lists of tuples with students name and ranking score
    sorted by ratnking score in descending order.
    >>> selection(read_file('registrations.txt'))['Responsible AI']
    [('Robert Davis', 92.0), ('Linda Wilson', 91.6), \
('Patricia Williams', 89.5), ('Mary Brown', 85.8), \
('Robert Rodriguez', 85.3), ('William Wilson', 85.3), \
('Michael Davis', 83.4), ('Elizabeth Miller', 82.3), \
('Elizabeth Jones', 81.4), ('James Miller', 80.7), \
('Jennifer Johnson', 80.4), ('James Jones', 79.5), \
('Robert Williams', 79.3), ('John Williams', 77.3), \
('Mary Jones', 75.9), ('William Williams', 75.8), \
('Elizabeth Wilson', 74.0), ('Linda Johnson', 73.7), \
('Robert Miller', 71.5), ('Robert Wilson', 69.5), \
('William Rodriguez', 69.4), ('Jennifer Rodriguez', 69.0), \
('Patricia Johnson', 68.6), ('James Davis', 68.2), ('Jennifer Jones', 65.1)]
    '''

    def get_score(student, subject):
        """
        Return score for a student for a given subject.
        """
        score = 0
        for preq in PREREQUISITES[subject]:
            score += registration[student]["Scores"][preq] * PREREQUISITES[subject][preq]
        return score / 100

    def get_students_for_subject(all_students, subject, priority):
        students = list()
        for student in all_students:
            if registration[student]["Prioritization"][subject] == priority:
                students.append(student)
        return students

    student_not_placed = [surname for surname in registration]
    course_placed = {subject: list() for subject in CAPACITY}

    i = 1
    while student_not_placed:
        for subject in CAPACITY:
            students = get_students_for_subject(student_not_placed, subject, i)
            scores = [
                get_score(student, subject) for student in students
            ]
            students_scores = list(zip(students, scores))
            students_scores = sorted(students_scores, key=lambda x: (x[1], -registration[x[0]]["Number"]), reverse=True)

            for student, score in students_scores[:CAPACITY[subject] - len(course_placed[subject])]:
                student_not_placed.remove(student)
                course_placed[subject].append((student, score))
        i += 1

    for subject in course_placed:
        course_placed[subject] = sorted(
            course_placed[subject], key=lambda x: x[1], reverse=True
        )

    return course_placed


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
