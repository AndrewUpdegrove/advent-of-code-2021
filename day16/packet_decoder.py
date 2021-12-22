import sys
import numpy as np

# consumes first n characters of s and then returns
# tuple containing (first n chars, remaining string in s)
def get_first(n, s):
    return s[:n], s[n:]

class Packet:
    def __init__(self):
        self.version = None
        self._type_id = None
        self.packet_length = 0
        self.is_literal = None
        self.sub_packets = []

    @property
    def type_id(self):
        if isinstance(self._type_id, type(None)):
            raise TypeError("The packet has not been identified as an operator or literal yet.")
        return self._type_id

    @type_id.setter
    def type_id(self, n):
        self._type_id = n
        if n == 4:
            self.is_literal = True
            self.literal_val = None
        else:
            self.is_literal = False
            self.length_type_id = None

    
    # will return a tuple with first element, n, indicating number of bits found
    # second will be an array of Packets of length n
    @classmethod
    def interpret_bit_stream(cls, bit_stream):
        packets = []
        flag = True
        while flag:
            newest_packet, bit_stream = cls.find_next_packet(bit_stream)
            if newest_packet: packets.append(newest_packet)
            else: flag = False
        return packets

    # bit stream is string of arbitrary length
    # will return the next packet that starts at the first bit of the string
    # will recursively call this function on subpackets
    @classmethod
    def find_next_packet(cls, bit_stream):
        if len(bit_stream) < 11:
            return None, bit_stream
        new_pack = Packet()
        # get and set version and type id
        version, bit_stream = get_first(3, bit_stream)
        type_id, bit_stream = get_first(3, bit_stream)
        new_pack.packet_length += 6
        new_pack.version = int(version, 2)
        new_pack.type_id = int(type_id, 2)

        if new_pack.is_literal:
            # parsing for literal
            new_number = ''
            more_string = 1
            while int(more_string):
                more_string, bit_stream = get_first(1,bit_stream) # continuation bit
                next_bits, bit_stream = get_first(4, bit_stream) # payload
                new_number += next_bits
                new_pack.packet_length += 5
            new_pack.literal_val = int(new_number, 2)
            # remaining_bits = (((new_pack.packet_length // 4) + 1) * 4) - new_pack.packet_length
            # _, bit_stream = get_first(remaining_bits, bit_stream)
        else:
            # get and assign length type id
            length_type_id, bit_stream = get_first(1, bit_stream)
            new_pack.packet_length += 1
            new_pack.length_type_id = int(length_type_id, 2)
            
            if new_pack.length_type_id:
                num_sub_packets, bit_stream = get_first(11, bit_stream)
                new_pack.packet_length += 11
                for i in range(int(num_sub_packets, 2)):
                    next_pack, bit_stream = cls.find_next_packet(bit_stream)
                    new_pack.packet_length += next_pack.packet_length
                    new_pack.sub_packets.append(next_pack)
            else:
                sub_packet_len, bit_stream = get_first(15, bit_stream)
                new_pack.packet_length += 15
                sub_packet_len = int(sub_packet_len, 2)
                bits_read = 0
                while bits_read < sub_packet_len:
                    next_pack, bit_stream = cls.find_next_packet(bit_stream)
                    bits_read += next_pack.packet_length
                    new_pack.sub_packets.append(next_pack)
                assert bits_read == sub_packet_len, "Read more bits than expected when parsing operator packet with '0' length type id"
                new_pack.packet_length += bits_read

        return new_pack, bit_stream

    def sum_packet(self):
        total = self.version
        for sub in self.sub_packets:
            total += sub.sum_packet()
        return total

    def evaluate_packet(self):
        res = None
        if self.is_literal: res = self.literal_val
        elif self.type_id == 0: res = sum([p.evaluate_packet() for p in self.sub_packets])
        elif self.type_id == 1: res = np.prod([p.evaluate_packet() for p in self.sub_packets])
        elif self.type_id == 2: res = min([p.evaluate_packet() for p in self.sub_packets])
        elif self.type_id == 3: res = max([p.evaluate_packet() for p in self.sub_packets])
        elif self.type_id == 5:
            assert(len(self.sub_packets) == 2)
            res = 1 if self.sub_packets[0].evaluate_packet() > self.sub_packets[1].evaluate_packet() else 0
        elif self.type_id == 6:
            assert(len(self.sub_packets) == 2)
            res = 1 if self.sub_packets[0].evaluate_packet() < self.sub_packets[1].evaluate_packet() else 0
        elif self.type_id == 7:
            assert(len(self.sub_packets) == 2)
            res = 1 if self.sub_packets[0].evaluate_packet() == self.sub_packets[1].evaluate_packet() else 0
        return res

with open(sys.argv[1], 'r') as in_file:
    out = ''
    for line in in_file:
        for char in line.rstrip():
            out += (bin(int(char,16))[2:]).zfill(4)


#line = 'D8005AC2A8F0'
#out = ''
#for char in line:
#    out += (bin(int(char,16))[2:]).zfill(4)

packet_set = Packet.interpret_bit_stream(out)


# Part 1
packet_sum = 0
for pack in packet_set:
    packet_sum += pack.sum_packet()

print(packet_sum)


# Part 2
part_2_ans = packet_set[0].evaluate_packet()
print(part_2_ans)
