import sys
import math
import operator

with open(sys.argv[1], 'r') as in_file:
    report = [line.rstrip() for line in in_file]

def recursion_driver(all_readings, operation = operator.ge):
    return find_reading(all_readings, 0, operation)


def find_reading(subset, pos, operation):
    # Base Cases
    num_readings = len(subset)
    print(f"For reading position {pos} there are {num_readings} readings")
    if len(subset) == 1:
        return subset
    elif len(subset[0]) == 1:
        return subset
    elif len(subset) < 1:
        raise RecursionError
    
    # Count bits
    bit_sum = 0
    for reading in subset:
        bit_sum += int(list(reading)[pos])

    print(bit_sum)
    # find least or most sig bit depending on operation
    sig_bit_at_pos = 1 if operation(bit_sum, math.ceil(num_readings/2)) else 0
    print(sig_bit_at_pos)

    # filter list
    filtered = [a for a in subset if int(list(a)[pos]) == sig_bit_at_pos]
    return find_reading(filtered, pos+1, operation)

oxygen_generator_rating = int(recursion_driver(report)[0], 2)
c02_scrubber_rating = int(recursion_driver(report, operator.lt)[0], 2)

print(oxygen_generator_rating)
print(c02_scrubber_rating)

print(oxygen_generator_rating * c02_scrubber_rating)
