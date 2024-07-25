#!/usr/bin/python3
"""UTF-8 validation"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints"""

    remainingBytes = 0
    bit7 = 1 << 7
    bit6 = 1 << 6

    for byte in data:
        currentBit = 1 << 7

        if remainingBytes == 0:
            while byte & currentBit:
                remainingBytes += 1
                currentBit = currentBit >> 1

            if remainingBytes == 0:
                continue

            if remainingBytes == 1 or remainingBytes > 4:
                return False
        else:
            if not (byte & bit7 and not (byte & bit6)):
                return False

        remainingBytes -= 1

    if remainingBytes == 0:
        return True

    return False
