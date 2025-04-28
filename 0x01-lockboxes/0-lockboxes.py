#!usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    """
    if not isinstance(boxes, list):
        return False

    unlocked = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
