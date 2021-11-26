import operator

sells = {
    "Dupont": 14,
    "Henry": 19,
    "Geoffroy": 15,
    "Layec": 21
}


def calc_total_sells():
    total_sells = 0
    for sell in sells.values():
        total_sells += sell

    return total_sells


def calc_best_seller(sells_collection):
    return max(sells_collection.items(), key=operator.itemgetter(1))[0]


# Params -- construct_collection
student = """21354955;DUPONT;JEAN
21354935;PICO;AMIL
21343655;HERBE;BOB"""


def construct_collection(given_student):
    split_students = given_student.split("\n")
    construct = {}
    for i in range(len(split_students)):
        construct[i] = split_students[i].split(";")
    final = {construct[i][0]: construct[i][1] + " " + construct[i][2] for i in range(len(construct))}

    return final


# Params -- construct_collection
students = {"John": [13, 15, 20, 13], "Bob": [17, 14, 13, 19], "Jeanne": [15, 18, 18, 20],
            "johnny": [15, 18, 18, 20]}


def calc_average(notes):
    return sum(notes) / len(notes)


def calc_best_student_average(students_entry):
    best_students = [{key: calc_average(value)} for key, value in students_entry.items() if
                     calc_average(value) == max([calc_average(value) for value in students_entry.values()])]

    return best_students


def result():
    print(calc_total_sells())
    print(calc_best_seller(sells))
    print(construct_collection(student))
    print(calc_best_student_average(students))
