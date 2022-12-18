from classes.school import School

if __name__ == "__main__":
    # Information regarding the students
    student_count = 250
    female_percent = 0.6
    second_year_percent = 0.05
    school_class_norm = 25
    group_norm = 11
    postal_code_distribution = {}

    # Information regarding the rooms
    room_distribution = {2: 0.7, 3: 0.2, 4: 0.1}

    # Information regarding the halls
    hall_distribution = {
        1: 0.15,
        2: 0.15,
        3: 0.15,
        4: 0.1,
        5: 0.1,
        6: 0.1,
        7: 0.05,
        8: 0.05,
        9: 0.05,
        10: 0.05,
        11: 0.05,
    }

    school = School(
        student_count,
        female_percent,
        second_year_percent,
        school_class_norm,
        group_norm,
        postal_code_distribution,
        room_distribution,
        hall_distribution,
    )

    for student in school.student_list:
        print(student)
    for room in school.room_list:
        print(room)
