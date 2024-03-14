#!/usr/bin/python3
""" Lockbox """


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened
    """
    # the first box is already opened.
    opened_boxes = [0]
    # add keys from the first box in a set of keys
    keys = set(boxes[0])

    # while there are keys can open boxes that still locked
    while keys:
        new_keys = set()
        for key in keys:
            # if key corresponds to a box and the box still locked
            if key < len(boxes) and key not in opened_boxes:
                # add the box to opened_boxes
                opened_boxes.append(key)
                # Add new keysfound in thebox to new_keys
                new_keys.update(boxes[key])
        # if no new keys found, break the loop
        if not new_keys:
            break

        # Update keys with newly found keys for next iteration
        keys = new_keys

    # if opened boxes is equal to number of boxes, all can be opened
    return len(opened_boxes) == len(boxes)
