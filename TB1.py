import math
import os
import random
import re
import sys

with open('input.txt', 'r') as file:
    lines = file.readlines()

first_multiple_input = lines[0].rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = lines[1:]

decoded = list(zip(*matrix))
endecoded = ''.join([''.join(item)for item in decoded])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'

print(re.sub(pat,' ',endecoded))


