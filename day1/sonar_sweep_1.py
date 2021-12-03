import sys
import logging

with open(sys.argv[1], 'r') as in_file:
    depth_list = [int(line.rstrip()) for line in in_file]

increased = -1

previous_measurement = -1
for measurement in depth_list:
    if measurement > previous_measurement:
        increased += 1
    previous_measurement = measurement

print(f"Increased {increased} times")
