from brownie import accounts, config, Owner, network


def test_deploy():

    owner = Owner.deploy({"from": accounts[0]})
    s = owner.getOwner()
    expected = accounts[0]
    assert s == expected


def test_update():

    owner = Owner.deploy({"from": accounts[0]})
    txn = owner.changeOwner(
        accounts[1],
        {"from": accounts[0]},
    )
    txn.wait(1)
    s = owner.getOwner()
    expected = accounts[1]
    assert s == expected
