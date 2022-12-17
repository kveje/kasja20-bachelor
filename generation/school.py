import math
import random

from room import Room
from student import Student


class School:
    """Object representing a school"""

    def __init__(
        self,
        student_count: int,
        female_percent: int,
        second_year_percent: int,
        school_class_norm: int,
        group_norm: int,
        postal_code_distribution: dict,
        room_distribution: dict,
        hall_distribution: list,
    ) -> None:

        # Defining information regarding the students
        self.student_count = student_count
        self.female_count = math.ceil(student_count * female_percent)
        self.male_count = student_count - self.female_count
        self.second_year_percent = second_year_percent
        self.school_class_max = school_class_norm
        self.group_max = group_norm

        self.school_classes = list(range(1, math.ceil(student_count / school_class_norm) + 1))
        self.groups = list(range(1, math.ceil(student_count / group_norm) + 1))

        # Defining information regarding the rooms
        room_sizes = []
        room_percent = []

        for key in room_distribution:
            room_sizes.append(key)
            room_percent.append(room_distribution[key])

        self.max_room_size = max(room_sizes)
        self.min_room_size = min(room_sizes)

        self.rooms = []
        self.beds = 0

        while self.beds < self.student_count:
            if self.beds >= self.student_count - self.max_room_size:
                self.rooms.append(self.student_count - self.beds)
                self.beds += self.student_count - self.beds

            else:
                bed = random.choices(population=room_sizes, weights=room_percent)[0]
                self.rooms.append(bed)
                self.beds += bed

        # Information regarding the hall
        self.halls = []
        self.halls_percent = []
        self.hall_counter = {}
        self.hall_max = {}
        for key in hall_distribution:
            self.hall_counter[key] = 0
            self.hall_max[key] = math.ceil(student_count * hall_distribution[key])
            self.halls.append(key)
            self.halls_percent.append(hall_distribution[key])

        self.hall_distribution = hall_distribution

        # Variables for counting number of students in class and group
        self.school_class_counter = {}
        self.group_counter = {}
        for i in range(1, math.ceil(student_count / school_class_norm) + 1):
            self.school_class_counter[i] = 0

        for i in range(1, math.ceil(student_count / group_norm) + 1):
            self.group_counter[i] = 0

        # Variables for generation
        self.student_list = []
        self.room_list = []

        self.__generate_students()
        self.__generate_rooms()

    def __generate_rooms(self) -> None:
        id = 1
        beds = 0
        # While loop generating male rooms
        while beds < self.male_count:
            if beds >= self.male_count - self.max_room_size:
                n = self.male_count - beds
            else:
                n = random.choices(self.rooms)[0]
                while beds + n > self.male_count - self.min_room_size:
                    n = random.choices(self.rooms)[0]

            beds += n
            self.rooms.remove(n)

            hall = random.choices(population=self.halls, weights=self.halls_percent)[0]
            self.room_list.append(Room(id, hall, n, "M"))

            # Update hall-counter
            self.__update_hall_count(hall, n)

            # Update id
            id += 1
            print(id, beds, "M")

        # While loop generating female rooms
        while beds < self.student_count:
            n = random.choices(self.rooms)[0]
            beds += n
            self.rooms.remove(n)

            hall = random.choices(population=self.halls, weights=self.halls_percent)[0]
            self.room_list.append(Room(id, hall, n, "F"))

            # Update hall-counter
            self.__update_hall_count(hall, n)

            # Update id
            id += 1
            print(id, beds, "K")

    def __update_hall_count(self, hall, beds) -> None:
        self.hall_counter[hall] += beds

        if self.hall_counter[hall] >= self.hall_max[hall]:
            self.halls_percent.pop(self.halls.index(hall))
            self.halls.remove(hall)

    def __generate_students(self) -> None:
        # For loop creating students
        for i in range(0, self.student_count):
            id = i + 1
            if i < self.female_count:
                gender = "K"
            else:
                gender = "M"

            school_class = random.choices(self.school_classes)[0]
            group = random.choices(self.groups)[0]
            second_year = random.choices(
                [True, False], weights=[self.second_year_percent, 1 - self.second_year_percent]
            )[0]

            postal_code = 4000

            self.student_list.append(Student(id, gender, postal_code, school_class, group, second_year))
            self.__update_student_count(school_class, group)

    def __update_student_count(self, school_class: int, group: int) -> None:
        # Updates the count
        self.school_class_counter[school_class] += 1
        self.group_counter[group] += 1

        # Checks whether the classes and groups are "full" and removes them from the list
        if self.school_class_counter[school_class] == self.school_class_max:
            self.school_classes.remove(school_class)

        if self.group_counter[group] == self.group_max:
            self.groups.remove(group)

    def export_school(self, name: str):
        pass

    def __repr__(self) -> str:
        pass
