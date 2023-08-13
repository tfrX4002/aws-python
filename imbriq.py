list1 = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]

def remplacer_occurrences(list2, previous_value,  new_value):
    for i, element in enumerate(list2):
        if isinstance(element, list):
            remplacer_occurrences(element, previous_value, new_value)
        elif element == previous_value:
            list2[i] =  new_value

remplacer_occurrences(list1, 58, 5800)
print(list1)
