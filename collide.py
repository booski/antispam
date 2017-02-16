#!/usr/bin/env python3

import binascii, string, random, fileinput, re

def hash(msg):
    return binascii.crc_hqx(msg.encode('ascii'), 0)

def collide(hash_sum, sel, l):
    max_iters = 1000000

    found = False
    for i in range(max_iters):
        cand = ''.join(random.choice(sel) for _ in range(l))
        
        if hash(cand) == hash_sum:
            found = cand
            break
                
    return found

def create_package(msg, sel, l):
    result = collide(hash(msg), sel, l)
    if result:
        print("[{}],{}".format(result, msg))
        exit(0)
    else:
        print("No collision found.")
        exit(1)

def verify_package(msg, col):
    if hash(msg) == hash(col):
        print("OK.")
        exit(0)
    else:
        print("Invalid.")
        exit(1)

message=""
for line in fileinput.input():
    message = message + line

message = message.strip()
selections = string.ascii_letters + string.digits
length = 32

regex = re.compile(r'\[([' + selections + r']{' + str(length) + r'})\],(.*)', re.DOTALL)
match = regex.match(message)

if match:
    verify_package(match.group(1), match.group(2))
else:
    create_package(message, selections, length)
    
