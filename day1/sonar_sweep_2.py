import sys
import logging

with open(sys.argv[1], 'r') as in_file:
    depth_list = [int(line.rstrip()) for line in in_file]

increased = -1

previous_measurement = -1
for count, measurement in enumerate(depth_list):
    try:
        current = measurement + depth_list[count+1] + depth_list[count+2]
    except IndexError:
        print(f"Found end of list")
        break
    if current > previous_measurement:
        increased += 1
    previous_measurement = current

print(f"Increased {increased} times")
