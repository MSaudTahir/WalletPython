from wallet import Wallet

def test_getAmount():
  obj = Wallet()
  obj.setAmount(400)
  assert(obj.getAmount() == 4)
