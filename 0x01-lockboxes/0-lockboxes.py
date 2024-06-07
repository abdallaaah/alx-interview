#!/usr/bin/python3
"""
this is lockboxes problem
"""


def canUnlockAll(boxes):
    """just loop on list and track every index + 1 of my current box if it """
    if (type(boxes)) is not list:
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
