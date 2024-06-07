#!/usr/bin/python3
"""
this is lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    true_boxes = 0
    boxes = sorted(boxes)
    for i in range(len(boxes)):
        if (i == 0):
            i += 1
        for x in boxes[i]:
            z = x
            if z + 1 == i + 1:
                true_boxes += 1
                break
    if (true_boxes == len(boxes)):
        return True
    else:
        return False
