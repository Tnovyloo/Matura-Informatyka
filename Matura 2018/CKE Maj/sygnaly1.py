with open('sygnaly.txt','r') as file:
    file_lines = [line.rstrip() for line in file]

def decode(lines):
    text = ''
    for num, line in enumerate(lines, start=1):
        if num % 40 == 0:
            text += line[9]
    return text

def find_text(lines):
    text = ''
    maximal = 0
    for line in lines:
        temp = 0
        chars = []
        for char in line:
            if chars.__contains__(char):
                continue
            chars.append(char)
            temp += 1
        if temp > maximal:
            maximal = temp
            text = line
    return text, maximal

def find_len(lines):
    words = []
    for line in lines:
        boolean = True
        for char in line:
            if boolean:
                for char2 in line[1:]:
                    diff = abs(ord(char) - ord(char2))
                    if diff > 10:
                        boolean = False
            else:
                break
        if boolean:
            words.append(line)
    return words


print(decode(file_lines))
print(find_text(file_lines))
print(find_len(file_lines))