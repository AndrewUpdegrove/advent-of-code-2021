import sys
import re


def find_easy_digits(output_set):
    easy_nums = 0
    for nums in output_set:
        for letters in nums:
            if len(letters) in [2, 3, 4, 7]:
                easy_nums += 1

    return easy_nums

class DigitClassifier:
    
    def __init__(self, digit_set, output):
        self.mapping = {
            1 : '',
            2 : '',
            3 : '',
            4 : '',
            5 : '',
            6 : '',
            7 : '',
            8 : '',
            9 : ''
        }
        self.output = output
        self.digit_set = digit_set
        self.solve()
        self.reverse_mapping = {v: k for k, v in self.mapping.items()}

    def solve(self):
        sixes = []
        fives = []
        for num in self.digit_set:
            if len(num) == 2:
                self.mapping[1] = num
            elif len(num) == 3:
                self.mapping[7] = num
            elif len(num) == 4:
                self.mapping[4] = num
            elif len(num) == 7:
                self.mapping[8] = num
            elif len(num) == 6:
                sixes.append(num)
            else:
                fives.append(num)

        self.decode_five(fives)
        self.decode_six(sixes)
            
    def decode_five(self, sub):
        for num in sub:
            if set(self.mapping[1]) <= set(num):
                self.mapping[3] = num
            elif (set(self.mapping[4]) - set(self.mapping[1])) <= set(num):
                self.mapping[5] = num
            else:
                self.mapping[2] = num

    def decode_six(self, sub):
        for num in sub:
            if set(self.mapping[4]) <= set(num):
                self.mapping[9] = num
            elif set(self.mapping[7]) <= set(num):
                self.mapping[0] = num
            else:
                self.mapping[6] = num
    
    def decode_output(self):
        number = ''
        for num in self.output:
            number += str(self.reverse_mapping[num])

        return int(number)



with open(sys.argv[1], 'r') as in_file:
    line_set = [line.rstrip() for line in in_file]


all_numbers = []
output = []
for x in line_set:
    split_up = re.findall('[a-g]{2,7}', x)
    split_up = ["".join(sorted(a)) for a in split_up]
    all_numbers.append(split_up[:10])
    output.append(split_up[10:])

total = 0
for helpers, outs in zip(all_numbers, output):
    subject = DigitClassifier(helpers, outs)
    total += subject.decode_output()

print(total)

