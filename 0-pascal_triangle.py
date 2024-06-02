#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    list = []
    for x in range(n):
        templist = []
        for y in range(x+1):
            if (y == 0 or y == x):
                templist.append(1)
            else:
                templist.append(list[x-1][y-1] + list[x-1][y])
        list.append(templist)
    return list
