import json
import hashlib
from time import time
import requests
from urllib.parse import urlparse
from uuid import uuid1
from flask import request, Flask, jsonify

class E516Chain(object):

    def __init__(self):
        self.trans = []
        self.chain = []
        self.nodes = set()

        # Create the first block in the chain
        self.create_block(oldhash='1', proof=100)

    def node_registration(self, address):

        url = urlparse(address)
        if url.netloc:
            self.nodes.add(url.netloc)
        elif url.path:
            self.nodes.add(url.path)
        else:
            print("ERROR")


    @staticmethod
    def hashing(block):

        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def create_trans(self, sender_address, recipient_address, trans_amount):
        'Will create a new transaction that should be placed in the next block'
        self.trans.append({

            'sender_address': sender_address,
            'recipient_address': recipient_address,
            'trans_amount': trans_amount,

        })

        return self.prev_block['index'] + 1

    @property
    def prev_block(self):

        'Return the previous block in the chain'

        return self.chain[-1]

    def create_block(self, proof, oldhash):


        block = {

            'index': len(self.chain) + 1,
            'TS': time(),
            'trans': self.trans,
            'proof': proof,
            'oldhash': oldhash or self.Hashing(self.chain[-1]),

        }

        self.trans = []
        self.chain.append(block)

        return block

    def pow(self, oldBlock):
        'Proof of Work Algorithm'

        oldproof = oldBlock['proof']
        oldhash = self.hashing(oldBlock)
        newproof = 0

        while self.validation_block(oldproof, newproof, oldhash) is False:
            newproof += 1

        return newproof

    def consensus(self):

        replacement_chain = None
        others = self.nodes

        len_chain = len(self.chain)
        for node in others:

            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['len']
                chain = response.json()['chain']

                if length > len_chain and self.validation_chain(chain):
                    len_chain = length
                    replacement_chain = chain

        if replacement_chain:
            self.chain = replacement_chain

            return True
        return False

    @staticmethod
    def validation_block(oldproof, proof, oldhash):
        'Validates the solution to the PoW'

        encoding = f'{oldproof}{proof}{oldhash}'.encode()
        attempt = hashlib.sha224(encoding).hexdigest()
        return attempt[:3] == '000'

    def validation_chain(self, chain):

        last_block = chain[0]
        current_index = 1

        while len(chain) > current_index:
            block = chain[current_index]

            last_block_hash = self.hashing(last_block)
            if block['oldhash'] != last_block_hash:
                print(1)
                return False

            if not self.validation_block(last_block['proof'], block['proof'], last_block_hash):
                print(self.validation_block(last_block['proof'], block['proof'], last_block_hash))
                return False

            last_block = block
            current_index += 1

        return True

app = Flask(__name__)
nodeid = str(uuid1()).replace('-', '')
E516Chain = E516Chain()

@app.route('/mine', methods=['GET'])
def mine():
    prev_block = E516Chain.prev_block
    p = E516Chain.pow(prev_block)

    oldhash = E516Chain.hashing(prev_block)
    block = E516Chain.create_block(p, oldhash)

    response = {

        'message': "New Block Created",
        'block number': block['index'],
        'trans': block['trans'],
        'proof': block['proof'],
        'previous hash': block['oldhash'],

    }

    return jsonify(response), 200

@app.route('/newtransaction', methods=['POST'])
def new_trans():
    trans = json.loads(request.data)
    needed = ['sender', 'receiver', 'amount']

    if not all(k in trans for k in needed):
        return json.dumps(str('Missing Data'))

    block = E516Chain.create_trans(trans['sender'], trans['receiver'], trans['amount'])

    response = {'message': "Transaction will be added",
                'block number': block,
                'sender': trans['sender'],
                'receiver': trans['receiver'],
                'amount': trans['amount'],

                }

    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def dis_chain():
    response = {
        'chain':E516Chain.chain,
        'len':len(E516Chain.chain),
    }

    return jsonify(response), 200


@app.route('/register', methods=['POST'])
def reg_node():
    values = json.loads(request.data)
    nodes = values['nodes']

    if nodes is None:
        return json.dumps("Please supply nodes")

    for node in nodes:
        E516Chain.node_registration(node)

    response = {
        'message': 'Nodes Added',
        'nodes': list(E516Chain.nodes),
    }

    return jsonify(response), 200

@app.route('/consensus', methods=['GET'])
def consensus():

    new = E516Chain.consensus()

    if new:

        response = {

            'message': 'Chain Replaced',
            'replacement_chain': E516Chain.chain,
        }

    else:
        response = {

            'message': 'Chain not Replaced',
            'replacement_chain': E516Chain.chain,
        }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8888, type=int)
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)



