import sys
import math

with open(sys.argv[1], 'r') as in_file:
    report = [line.rstrip() for line in in_file]

num_readings = len(report)
count_array = [0] * len(report[0])
for reading in report:
   count_array = [a + b for a, b in zip(list(map(int, list(reading))), count_array)]

bit_array = [1 if v > math.floor(num_readings/2) else 0 for v in count_array]

inverse_bit_array = [ 0 if a == 1 else 1 for a in bit_array]

str1 = ''
gamma_rate = int(str1.join(list(map(str, list(bit_array)))), 2)
epsilon_rate = int(str1.join(list(map(str, list(inverse_bit_array)))), 2)

print(gamma_rate)
print(epsilon_rate)

print(gamma_rate * epsilon_rate)
