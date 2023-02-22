from wallet import Wallet

def test_getAmount():
  obj = Wallet()
  obj.setAmount(500)
  assert(obj.getAmount() == 500)
