def ascii_caesar_shift(message, distance):
    encrypted = ""
    for char in message:
        value = ord(char) + distance
        encrypted += chr(value % 128) #128 for ASCII
    return encrypted
