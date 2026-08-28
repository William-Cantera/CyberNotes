# Cybersecurity educational code example
# Safe for learning only

```python
import hashlib
import time
import json

class SimpleBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block in the chain
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'transactions': [],
            'proof': 1,
            'previous_hash': '0'
        }
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        # Add a new block to the chain
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'transactions': transactions,
            'proof': self.proof_of_work(previous_block['proof']),
            'previous_hash': self.hash_block(previous_block)
        }
        self.chain.append(new_block)
        return new_block

    def proof_of_work(self, previous_proof):
        # Simple PoW algorithm: find a number p' such that hash(pp') contains 4 leading zeroes
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash_block(self, block):
        # Hash a block
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        # Check if the blockchain is valid
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            # Check if the previous hash of the current block is correct
            if block['previous_hash'] != self.hash_block(previous_block):
                return False
            # Check if the proof of work is correct
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

def simulate_attack():
    # Simulate a blockchain and an attack
    blockchain = SimpleBlockchain()
    
    # Add some legitimate blocks
    blockchain.add_block([{'sender': 'Alice', 'recipient': 'Bob', 'amount': 50}])
    blockchain.add_block([{'sender': 'Bob', 'recipient': 'Charlie', 'amount': 30}])
    
    print("Initial blockchain state:")
    print(json.dumps(blockchain.chain, indent=2))
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}")
    
    # Simulate an attack by modifying a transaction
    blockchain.chain[1]['transactions'][0]['amount'] = 100
    
    print("\nBlockchain state after attack:")
    print(json.dumps(blockchain.chain, indent=2))
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}")

# Run the simulation
simulate_attack()

# This script demonstrates a simple blockchain implementation and simulates a basic attack.
# It shows how changing data in a block invalidates the entire chain.
# 
# Usage:
# 1. Run the script to see the simulation output.
# 2. Modify the simulate_attack() function to test different scenarios.
#
# Why it's useful:
# - Helps understand basic blockchain structure and security.
# - Demonstrates the importance of data integrity in blockchains.
# - Can be extended to test more complex attack scenarios or security measures.

# Fallback content for Blockchain Security Considerations
Error 1

# Fallback content for Blockchain Security Considerations
Error 1

# Fallback content for Blockchain Security Considerations
Error 1

# Fallback content for Blockchain Security Considerations
Error 1

# Fallback content for Blockchain Security Considerations
Error 1

# Fallback content for Blockchain Security Considerations
Error 1

