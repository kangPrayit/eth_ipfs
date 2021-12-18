import requests
import pandas as pd
import numpy as np
import json
from web3 import Web3, HTTPProvider

IPFS_URL = 'http://127.0.0.1:5001/'


# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/IPFSContract.json'
# Deployed contract address (see `migrate` command output: `contract address`)
# deployed_contract_address = '0x3d14eD1FCe0Fd6Cb1A6D5C78bf33B5587a1e3e15'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    deployed_contract_address = contract_json['networks']["5777"]["address"]

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

def upload_file_to_ipfs(uploaded_file):
    files = {
        'file': uploaded_file.getvalue()
    }
    response = requests.post(f"{IPFS_URL}api/v0/add", files=files)
    cid = response.json()['Hash']
    filename = uploaded_file.name
    return cid, filename


def get_data_from_contracts():
    jumlahData = contract.functions.getJumlahData().call()

    data = []
    for i in range(jumlahData):
        d = contract.functions.data_manufacturers(i).call()
        data.append(d)

    column_names = ["sid","system_information","system_create","mid","manufacture_id","manufacture_date","filename","ipfs_file_cid"]
    df = pd.DataFrame(data, columns = column_names)

    return df

def simpan_data_to_smart_contract(
    sid,
    system_information,
    system_create,
    mid,
    manufacture_id,
    manufacture_date,
    filename,
    ipfs_file_cid
    ):
    tx_hash = contract.functions.addDataManufacturer(
                        sid,
                        system_information,
                        system_create,
                        mid,
                        manufacture_id,
                        manufacture_date,
                        filename,
                        ipfs_file_cid
                    ).transact()


# print(deployed_contract_address)
# df = get_data_from_contracts()
# print(df)