#!/usr/bin/env python


def return_pair(seq):
    seq_type = type(seq)
    return seq_type().join(seq[:1] + seq[-1:])


def transform_line(seq):
    new_seq = seq
    seq_type = type(seq)
    transform = {'one': '1',
                 'two': '2',
                 'three': '3',
                 'four': '4',
                 'five': '5',
                 'six': '6',
                 'seven': '7',
                 'eight': '8',
                 'nine': '9'
                 }
    for key,val in transform.items():
        new_seq = new_seq.replace(key, val)
    return new_seq


filename = 'test2.dat'


sum1 = 0
sum2 = 0
with open(filename, 'r') as f:
    lines = f.readlines()
for ln in lines:
    line_from_join = ''.join(c for c in ln.strip() if c.isdigit())
#    sum1 += int(return_pair(line_from_join))

    converted_line = transform_line(ln.strip())
    print(converted_line)
    line_from_join2 = ''.join(c for c in converted_line if c.isdigit())
#    print(line_from_join2)
    print(return_pair(line_from_join2))

    sum2 += int(return_pair(line_from_join2))

print("---\n" + str(sum1))
print("---\n" + str(sum2))
