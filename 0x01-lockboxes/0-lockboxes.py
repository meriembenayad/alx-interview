#!/usr/bin/python3
""" Lockbox """


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    # the first box is already opened.
    opened_boxes = {0}
    # add keys from the first box in a set of keys
    keys = set(boxes[0])

    # while there are keys can open boxes that still locked
    while keys - opened_boxes:
        # key that can open a box still locked
        key = (keys - opened_boxes).pop()
        # we add it to the set of opened_boxes
        opened_boxes.add(key)
        # we add the keys from the boxwe just opened to our set
        keys.update(boxes[key])

    # Check if the opened_box is equal to number of boxe, return True
    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
