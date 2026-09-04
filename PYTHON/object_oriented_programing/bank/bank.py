""" 
abstrctions
bank class->
deposit, withdraw
show account
getter and setter ->
->easy to scale function<understring>
-------------------------
login account
create account
deposit
withdraw
"""

class BankAccount:

    def __init__(self,name, balance, account_no):
        self.name = name
        self._balance = balance
        self.account_no = account_no

    #data i read
    @property
    def balance(self):
        print("somebody is trying to access the johns balance")
        return self._balance
    #to control updated
    #setterr
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            print("somebody is tried to read johns balance")
            return
        if value < 0:
            print("ensure new balance is not less than 0")
            return
        self._balance = value
    def deposit(self):
        pass
    
    def withdraw(self):
        pass

    def show_account_details(self):
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance}")
        print(f"Account Number: {self.account_no}")

john=BankAccount(name="John Mwangi", balance=0, account_no="223344223")
print("john balance is", john.balance)
#john.show_account_details()