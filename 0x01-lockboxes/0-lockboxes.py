#!/usr/bin/python3
"""
this is lockboxes problem
"""
def canUnlockAll(boxes):
    """just loop on list and track every index + 1 of my current box if it in the currenct or not"""
    [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    true_boxes = 0
    i = 1
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