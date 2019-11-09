from test import test

def zadanie2(list1, list2):
    mixedList = []
    iterator = 0
    if (len(list1) > len(list2)):
        iterator = len(list1)
    else:
        iterator = len(list2)

    for i in range(iterator):
        if i < len(list1):
            mixedList.append(list1[i])
        if i < len(list2):
            mixedList.append(list2[i])
    
    return mixedList

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12,'c','5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])