from test import test

def zadanie1(listObject):
    clearList = []
    for value in listObject:
        if not clearList or value != clearList[-1]:
            clearList.append(value)
    return clearList

test(zadanie1,[1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])