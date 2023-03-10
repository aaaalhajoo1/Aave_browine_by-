from brownie import accounts
from scripts.helpful_scripts import get_account
from brownie import network,config,interface



def get_weth():
   """
    Mints WETH by depositing ETH.
    """
   account = get_account()
   weth=interface.IWeth(config["networks"][network.show_active()]["weth_token"])
   tx=weth.deposit({"from":account,"value":0.1*10**18})
   tx.wait(1)
   print("received 0.1 Weth")
   return tx




def main():
   get_weth()