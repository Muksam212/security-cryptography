import hashlib

def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        chunk = file.read(4096)
        while chunk:
            hasher.update(chunk)
            chunk = file.read(4096)
    return hasher.hexdigest()

def hash_string(string):
    hasher = hashlib.sha256()
    hasher.update(string.encode('utf-8'))
    return hasher.hexdigest()

# Example usage
file_path = 'myfile.txt'
print(f"SHA-256 hash of the file: {hash_file(file_path)}")

string = "Hello, World!"
print(f"SHA-256 hash of the string: {hash_string(string)}")