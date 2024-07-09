import hashlib

'''
new methods represent the message digest

we have been using this algorithm because
it will always provide fixed number of characters no matter what

that's why this algorithm also known as compression technique
'''
# h = hashlib.new('sha256')
# h.update(b'I know Spanish') #converted into fixed length value
# print(h.hexdigest()) 

#file hashing

'''
File hashing in Python is the process of generating a fixed-size string (hash) from the contents of a file. 
This hash uniquely represents the data in the file. Hashes are commonly used to verify the integrity of files, 
ensuring that they haven't been altered or corrupted.
'''

hasher = hashlib.new('sha256')

SIZE = 65536

with open('myfile.txt', 'rb') as file:
    buffer = file.read(SIZE)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = file.read(SIZE)
print(hasher.hexdigest())


