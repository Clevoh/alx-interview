#!/usr/bin/python3
"""method that determines box to be opened"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    for keys in range(1, len(boxes) - 1):
        unlocked = False
        for i in range(len(boxes)):
            unlocked = keys in boxes[i] and keys != i
            if unlocked:
                break
        if unlocked is False:
            return unlocked
    return True
