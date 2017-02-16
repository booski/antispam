#!/usr/bin/env python3

import fileinput

import binascii
def hash(msg):
    return binascii.crc_hqx(msg.encode('ascii'), 0)

import string, random
def collide(hash_sum):
    selections = string.ascii_letters + string.digits
    length = 32
    max_iters = 1000000
    i = 0

    found = False
    for i in range(max_iters):
        cand = ''.join(random.choice(selections) for _ in range(length))
        
        if hash(cand) == hash_sum:
            found = cand
            break
                
    return found
    
message=""
for line in fileinput.input():
    message = message + line

message = message.strip()
hsum = hash(message)
result = collide(hsum)

if result:
    print("Collider: {}".format(result))
    exit(0)
else:
    print("No collision found.")
    exit(1)

