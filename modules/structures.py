# Manipuler les structures de données

from random import randint

# Params -- second_index_value
L = [13, 15, 12, 17, 15, 18, 15, 17]
A = 15


def second_index_value(array, value):
    """
    Get index if number is identical 2 times
    :param array: Get an array
    :param value: Get a value
    :return:
    """
    table_length = len(array)
    index = 0
    count = 0
    while index < table_length:
        table_value = array[index]
        if table_value == value:
            count += 1
        if count == 2:
            return index
        index += 1
    if count < 2:
        return -1


def generate_1000_items_in_array_and_sort_them():
    m = []
    while len(m) < 1000:
        m.append(randint(1, 1000))
    return sorted(m)


# Params -- merge_lists_1_by_1
list1 = [13, 15, 12, 17, 15]
list2 = ["Riri", "Fifi", "Loulou"]


def merge_lists_1_by_1(list1, list2):
    """
    Merging arrays step by step
    :param list1: Get array list 1
    :param list2: Get array list 2
    :return: list 3 array
    """
    list3 = []
    index = 0

    if len(list1) > len(list2):
        max_index = len(list1)
    else:
        max_index = len(list2)

    while index < max_index:
        try:
            if index < len(list1):
                list3.append(list1[index])
            if index < len(list2):
                list3.append(list2[index])
        except ValueError:
            return ValueError
        index += 1

    return list3


# Params -- merge_list_without_duplicates
L2 = [18, 15, 14, 13, 19, 20]


def merge_list_without_duplicates(list1, list2):

    list3 = list1 + list2
    [list3.remove(x) for x in list3 if list3.count(x) > 1]

    return sorted(list3)


# Params -- val_and_coef_from_given_values
val = [12.5, 13.6, 18.4, 9.7]
coef = [2, 3, 5, 4]


def val_and_coef_from_given_values(val, coef):

    total_val = 0
    total_coef = 0
    calc_value_and_coef = [val[x] * coef[x] for x in range(0, len(val))]

    for x in calc_value_and_coef:
        total_val += x

    for y in coef:
        total_coef += y

    return total_val / total_coef


def structure():
    print(second_index_value(L, A))
    print(generate_1000_items_in_array_and_sort_them())
    print(merge_lists_1_by_1(list1, list2))
    print(merge_list_without_duplicates(list1, L2))
    print(val_and_coef_from_given_values(val, coef))