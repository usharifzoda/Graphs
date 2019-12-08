"""
def beer():
    print('Printing from a function')

beer()

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

bitcoin_to_usd(3)

"""

def allowed_age(my_age):
    new_age = my_age/2 + 7
    return new_age

limit = allowed_age(27)
print("Printing ages = ", limit)