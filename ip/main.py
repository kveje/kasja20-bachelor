import numpy as np
from cpmpy import *

m = Model()

# Data input
students_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students_school_class = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
students_group = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
hall_id = [1, 2]
room_id = [1, 2, 3, 4, 5]
room_hall_id = [1, 1, 2, 2, 2]
room_sizes = [2, 2, 2, 2, 2]

student_count = len(students_id)
room_count = len(room_sizes)
hall_count = len(hall_id)

# Variable creation
student_hall_var = boolvar(shape=(student_count, hall_count))
student_room_var = boolvar(shape=(student_count, room_count))

# Variable name definition
for x in range(0, student_count):
    for y in range(0, hall_count):
        student_hall_var[x, y] = boolvar(name="S{},H{}".format(students_id[x], hall_id[y]))

for x in range(0, student_count):
    for y in range(0, room_count):
        student_room_var[x, y] = boolvar(name="S{},R{}".format(students_id[x], room_id[y]))

### Constraints
# A student has to live in EXACTLY one room
for i in range(0, student_count):
    m += sum(student_room_var[i]) == 1

# A student has to live in EXACTLY one hall
for i in range(0, student_count):
    m += sum(student_hall_var[i]) == 1

# Connection between rooms and halls
for x in range(0, room_count):
    hall_idx = room_hall_id[x] - 1
    for y in range(0, student_count):
        m += student_room_var[y, x].implies(student_hall_var[y, hall_idx])

# Declaring number of beds in the rooms
for i in range(0, room_count):
    m += sum(student_room_var[:, i]) == room_sizes[i]

# Students from the same class or school cannot live in room together
for i in range(0, room_count):
    for x in range(0, student_count):
        for y in range(0, student_count):

            if x == y:
                break

            if students_school_class[x] == students_school_class[y]:
                m += student_room_var[x, i] + student_room_var[y, i] <= 1

            if students_group[x] == students_group[y]:
                m += student_room_var[x, i] + student_room_var[y, i] <= 1

print(student_hall_var)
print(student_room_var)

# Objective function (optional)
# m.maximize(sum(x) + 100 * b)

print(m)
print(m.solve(), "\n", student_hall_var.value(), "\n", student_room_var.value())
