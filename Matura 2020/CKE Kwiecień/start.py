from collections import Counter

with open('dane4.txt') as file:
    numbers = [int(line.rstrip()) for line in file]

def gaps_sequence(sequence):
    gaps = [abs(sequence[i-1] - sequence[i]) for i in range(len(sequence))]
    return gaps

def regular_gaps_sequence(gaps):
    maximal_sequence_len = 1
    sequence_len = 1
    values = [] # Indexes of first and last number in maximal length sequences
    gaps[0] = "-"
    prev = "-"
    for gap in gaps:
        if gap == prev:
            sequence_len += 1
        else:
            sequence_len = 1
            prev = gap
        values.append(sequence_len)

    maximal = max(values) + 1
    start = numbers[values.index(max(values)) - max(values)]
    end = numbers[values.index(max(values))]
    return maximal, start, end
    #Thanks to Zargothrax

seq_gaps = gaps_sequence(numbers)
print(max(seq_gaps), min(seq_gaps))

sequence_of_gaps = regular_gaps_sequence(seq_gaps)
print(sequence_of_gaps)

result = Counter(seq_gaps).most_common()
print(result)

with open('odpowiedzi','a') as file:
    file.write(f"1\n{max(seq_gaps), min(seq_gaps)}"
               f"2\n{sequence_of_gaps}"
               f"3\n{result}")