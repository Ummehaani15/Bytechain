from flask import Flask, request, jsonify
import datetime
import hashlib
import random as r
from cryptography.fernet import Fernet

class Block:
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.get_hash()
        # keys
        self.key = Fernet.generate_key()
        self.key_var = Fernet(self.key)
        self.encrypted_data = self.key_var.encrypt(bytes(self.data,'ascii'))
        self.decrypted_data = self.key_var.decrypt(self.encrypted_data)



    
    @staticmethod
    def create_genesis_block():
        return Block("0", "0", datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) +
                      str(self.data) +
                      str(self.timestamp))

        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

class Keylist_Block:
    def __init__(self,key,timestamp):
        self.key=key
        self.timestamp = timestamp

    @staticmethod
    def create_genesis_block():
        return Keylist_Block( "0", datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.previous_block_hash) +
                      str(self.key) +
                      str(self.timestamp))

        inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash



def get_data_from_block(block, key):
    decrypted_data = Fernet(key).decrypt(block.encrypted_data)
    return decrypted_data 

def get_user_info():
    name=input()
    wallet_balance=input()
    will_statements=input()


# main block begins here

# num_blocks_to_add = int(input('\n enter the number of data blocks to add\n'))
num_blocks_to_add = r.randint(100,200)

block_chain = [Block.create_genesis_block()]

print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)
print('')

for i in range(1, num_blocks_to_add+1):
    # data=input('\nenter the data to be stored in %d block\n' %i)
    data=str(  ''.join(  [ascii(r.randint(0,127)) for i in range( r.randint(1000,2000)  )]  )   )
    block_chain.append(Block(block_chain[i-1].hash, data, datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
    print(block_chain[i].decrypted_data.decode('utf-8'))


# seperating the key from the encrypted data

key_list_chain= [Keylist_Block.create_genesis_block()]

for i in range(1, num_blocks_to_add+1):
    key_list_chain.append(Keylist_Block(block_chain[i].key,datetime.datetime.now()))

print('The keylist has be seperated out into a different blockchain')

for i in range(1,num_blocks_to_add): block_chain[i].key=None

print(key_list_chain)
print()
print()
print(block_chain)
    
# while(True):
#     match int(input('\nEnter 1 to query data in a particular block \n0 to exit \n')):
#         case 1 :
#             index=int(input(
#                 'enter the block number to query from\n'
#             ))
#             data=get_data_from_block(block_chain[index], key_list_chain[index].key.decode('utf-8'))
#             print('data in block 1 is ')
#             print(data)

#         case 0:
#             exit(0)





app = Flask(__name__)

# @app.route('/api', methods = ['GET'])
# def returnascii():
#     d = {}
#     inputchr = str(request.args['query'])
#     answer = str(ord(inputchr))
#     d['output'] = answer
#     return d


@app.route('/numberofblocks', methods = ['GET'])
def returnascii():
    d = {}
    # inputchr = str(request.args['numberofblocks'])
    answer = str(num_blocks_to_add)
    d['output'] = answer
    return answer



if __name__ =="__main__":
    app.run()