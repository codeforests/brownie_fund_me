from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENV) \
        or network.show_active() in FORKED_LOCAL_ENV : 
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(
                DECIMALS, 
                Web3.toWei(STARTING_PRICE, "ether"), 
                {"from" : get_account()})