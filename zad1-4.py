def test(fun, *args):
    print("".join(['-' for i in range(40)]))
    print(fun.__name__[:-1].upper()+" "+fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print("Yes, "+decoded.replace("my","your"))
        else:
            print("No, "+decoded.replace("my","your").replace("has","has not")+" yet")
    else:
        print("Is correct? "+ str(res == args[-1]))
    print( "".join(['-' for i in range(40)]))

def zadanie1(listObject):
    clearList = []
    for value in listObject:
        if not clearList or value != clearList[-1]:
            clearList.append(value)
    return clearList

test(zadanie1,[1, 2, 3, 3, 5, 68, 68, 24], [1,2,3,5,68,24])

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

def zadanie3(listTuples):
    sortedList=[]
    for i in range(len(listTuples)):
        if not sortedList:
            sortedList.append(listTuples[i])
        else:
            for j in range(len(sortedList)):
                if listTuples[i][-1] < sortedList[j][-1]:
                    sortedList.insert(j,listTuples[i])
                    break
                if j == len(sortedList)-1:
                    sortedList.append(listTuples[i]) 
        
    print(sortedList)
    return sortedList

test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])

def zadanie4(text):
    words = [word.replace('ok','') for word in text.split('$') if word.startswith('ok')]

    return ' '.join(words)

test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af", [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])
