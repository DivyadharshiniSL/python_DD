balance=1000
def check_balance():
    print(f"\n Your current balance is: ₹{balance}\n")
def deposit(amount):
    global balance
    if amount>0:
        balance+= amount
        print(f"₹{amount} deposited successfully")
    else:
        print("Please enter a valid amount")
def withdrawl(amount):
    global balance
    if amount>balance:
        print("")   