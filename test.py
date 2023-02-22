from wallet import Wallet

def test_getAmount():
  obj = Wallet()
  obj.setAmount(400)
  assert(obj.getAmount() == 400)
  
  
def test_removeAmount():
  obj = Wallet()
  obj.setAmount(500)
  obj.removeAmount(100)
  assert(obj.getAmount() == 400)

def test_addAmount():
  obj = Wallet()
  obj.setAmount(400)
  obj.addAmount(100)
  assert(obj.getAmount() == 500)
