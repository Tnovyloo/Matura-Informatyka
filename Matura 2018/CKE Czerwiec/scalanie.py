with open('dane1.txt','r') as file:
    datafile1 = [line.rstrip().rsplit() for line in file]
    print(datafile1)
with open('dane2.txt','r') as file:
    datafile2 = [line.rstrip().rsplit() for line in file]
    print(datafile2)

#4.1
def compare_last_number(data1, data2):
    count = 0
    for sequence in range(len(data1)):
        if data1[sequence][-1] == data2[sequence][-1]:
            count += 1
    return count

print(compare_last_number(datafile1, datafile2))

#4.2
def even_and_odd(data1, data2):
    count = 0
    for sequence in range(len(data1)):
        count_even_data1 = 0
        count_even_data2 = 0
        for number in data1[sequence]:
            if int(number) % 2 == 0:
                count_even_data1 += 1
        for number in data2[sequence]:
            if int(number) % 2 == 0:
                count_even_data2 += 1
        if count_even_data1 == 5 and count_even_data2 == 5  :
            count += 1
    return count

print(even_and_odd(datafile1, datafile2))

#4.3
def count_same_sequences(data1, data2):
    count = 0
    indexes = []
    for sequence in range(len(data1)):
        data1_merged = set(data1[sequence]) #Funkcja set() scala powtarzające sie elementy w liscie
        data2_merged = set(data2[sequence])
        if data1_merged == data2_merged:
            count += 1
            indexes.append(sequence+1)
    return count, indexes

print(count_same_sequences(datafile1, datafile2))

#4.4
def merge_data(data1, data2):
    result = []
    for sequence in range(len(data1)):
        data1[sequence] = [int(number) for number in data1[sequence]]
        data2[sequence] = [int(number) for number in data2[sequence]]
        result.append(sorted(data1[sequence] + data2[sequence]))
    return result

print(merge_data(datafile1, datafile2))
