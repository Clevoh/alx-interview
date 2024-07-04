def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]
    
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)
