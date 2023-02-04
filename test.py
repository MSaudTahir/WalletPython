from wallet import Wallet

def test_getAmount():
  obj = Wallet()
  obj.setAmount(400)
  assert(obj.getAmount() == 400)
  
test_getAmount()
print('Tests ran successfully')
