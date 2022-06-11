from brownie import accounts, config, Owner, network
import os


def deploy():
    print("Deployment started")

    account = get_account()
    print(account)
    owner = Owner.deploy({"from": account})
    s = owner.getOwner()
    print(s)
    txn = owner.changeOwner(
        accounts[1],
        {"from": account},
    )
    txn.wait(1)
    s = owner.getOwner()
    print(s)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        pk = config["wallets"]["from_key"]
        account = accounts.add(pk)
        return account


def main():
    deploy()
