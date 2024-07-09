import hashlib

import os

salt = os.urandom(16)
'''
    pbkdf2 stands for password base key deviation function and it's version is 2
    sha256 is a basic algorithm
    salt means to make complex password

    always remember that sha256 give the same number of bits

    one digits can make completely different in hash value
'''
hash = hashlib.pbkdf2_hmac('sha256', b'pasrword', salt, 100000)

import binascii
hexhash = binascii.hexlify(hash)

print(hexhash)