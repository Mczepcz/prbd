import numpy as np

def reduce(table, size):

    if isinstance(size,tuple) or isinstance(size, list):
        newX, newY = size
    elif isinstance(size,int):
        newX = size
        newY = newX
    else:
        raise Exception("Passed date is wrong type")

    oldX = len(table)
    oldY = len(table[0])

    if oldX < newX or oldY < newY:
        raise Exception("Passed size should be smaller then table")

    factorX = oldX / newX
    factorY = oldY / newY

    output = np.zeros((newX,newY))

    for i in range(newX):
        for j in range(newY):

            x = int(i*factorX)
            y = int(j*factorY)

            count = 1
            summedValue = table[x][y]
            for xi in (-1,1):
                for yj in (-1, 1):
                    ii = x+xi
                    jj = y + yj
                    if 0 <= ii < oldX and 0 <= jj < oldY:
                        summedValue += table[x+xi][y+yj]
                        count += 1
            output[i][j] = summedValue/count

    return output