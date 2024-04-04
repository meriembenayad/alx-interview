def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        - data: A list of integers, each integer represents 1 byte of data
    Returns:
        - True if data is a valid UTF-8 encoding, otherwise False
    """
    byte_count = 0
    for byte in data:
        # Convert byte to binary and get the first 8 bits
        byte_bin = format(byte, '08b')

        if byte_count == 0:
            # determine the number of bytes in the character
            if (byte_bin.startswith('11110')):
                byte_count = 3
            elif (byte_bin.startswith('1110')):
                byte_count = 2
            elif (byte_bin.startswith('110')):
                byte_count = 1
            elif not byte_bin.startswith('0'):
                return False
        else:
            # Check if byte is continuation byte (starts with '10')
            if not byte_bin.startswith('10'):
                return False
            byte_count -= 1

    return byte_count == 0
