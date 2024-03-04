import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

def find_nonce(data, previous_hash, difficulty):
    index = 0
    timestamp = datetime.datetime.now()
    nonce = 0
    while True:
        block = Block(index, timestamp, data, previous_hash, nonce)
        if block.hash.startswith('0' * difficulty):
            return nonce, block.hash
        nonce += 1

# Example usage
data = "Example Data"
previous_hash = "Previous Hash"
difficulty = 4  # Adjust the difficulty as needed
nonce, hash_result = find_nonce(data, previous_hash, difficulty)
print(f"Nonce: {nonce}")
print(f"Hash: {hash_result}")
