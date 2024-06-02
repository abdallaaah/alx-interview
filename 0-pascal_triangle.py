#!/usr/bin/python3
def pascal_triangle(n):
    list = []
    x = 0
    for x in range(n):
        templist = []
        y = 0
        for y in range(x+1):
            if (y == 0 or y == x):
                templist.append(1)
            else:
                templist.append(list[x-1][y-1] + list[x-1][y])
        list.append(templist)
        # x+=1
    return list
