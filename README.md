# Blockchain with Data Encryption

This project is a simple Python implementation of a blockchain with data encryption. It uses the `cryptography.fernet` library for encryption and offers basic functionalities for creating and managing blockchain blocks.

## Features

- **Block Class**: The project defines a `Block` class to represent individual blocks in the blockchain. Each block contains:
  - `previous_block_hash`: Hash of the previous block.
  - `data`: Encrypted data.
  - `timestamp`: The time when the block was created.
  - `hash`: The block's hash.

- **Genesis Block**: A special method, `create_genesis_block()`, is provided to create the initial or "genesis" block of the blockchain.

- **Encryption**: Data within each block is encrypted using the `cryptography.fernet` library, enhancing the security of stored information.

- **Key Management**: Encryption keys are stored in a separate blockchain called `Keylist_Block`. This separation ensures that encryption keys are not exposed in the main blockchain.

## Usage

1. Make sure you have the necessary libraries installed, including `cryptography`.

2. Execute the Python script to create the blockchain. It generates a random number of data blocks, encrypts the data, and stores it in the blockchain.

3. Keys are stored securely in the `Keylist_Block` blockchain for decryption. For added security, keys are removed from the main blockchain.

## Code

```python
# Insert your Python code here
