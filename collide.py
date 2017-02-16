#!/usr/bin/env python3

import binascii, string, random, fileinput, re

def hash(message):
    return binascii.crc_hqx(message.encode('utf-8'), 0)

def collide(hash_sum, chars, length):
    max_iters = 1000000

    found = False
    for i in range(max_iters):
        cand = ''.join(random.choice(chars) for _ in range(length))
        
        if hash(cand) == hash_sum:
            found = cand
            break
                
    return found

def create_package(message, chars, length):
    result = collide(hash(message), chars, length)
    if result:
        print("[{}],{}".format(result, message))
        exit(0)
    else:
        print("No collision found.")
        exit(1)

def verify_package(message, collision):
    if hash(message) == hash(collision):
        print("OK.")
        exit(0)
    else:
        print("Invalid.")
        exit(1)

input = ""
for line in fileinput.input():
    input = input + line

input = input.strip()
allowed_chars = string.ascii_letters + string.digits
collider_length = 32

regex = re.compile(r'\[([' + allowed_chars + r']{' + str(collider_length) + r'})\],(.*)', re.DOTALL)
match = regex.match(input)

if match:
    verify_package(match.group(1), match.group(2))
else:
    create_package(input, allowed_chars, collider_length)
    
