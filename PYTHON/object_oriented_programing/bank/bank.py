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
""" 
static <it does not change>.<class properties>.<Belong to class>
Static Method<>. class method. <function belong to class>

why would you want to use class properties?
"""
class BankAccount:
    clients=0 #static property
    bank_name="Post Bank" #static property

    def __init__(self,name, balance, account_no):
        self.name = name
        self._balance = balance
        self.account_no = account_no
        #BannkAccount.clients=BankAccount.clients+1
        #self.__class__.clients=self.__class__.clients+1
        #self.__class__.add_client()
        BankAccount.add_client()
        #self.__class__.bank_name=name_bank
        #self.__class__.clients+=1
        #BankAccount.clients +=self.clients

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

    #-------------------
    #static method.<class method><cls> @staticmethod->
    #-------------------
    @staticmethod
    def calculate_interest(amount, year):
        rate=10
        interest_per_year=amount*(rate/100)
        interest_total=interest_per_year*year
        total=amount+interest_total
        print(f"if you take a loan of {amount} ,interest rate per year {interest_per_year}")
        print(f"Total interest {interest_total} and total to pay {total} after {year} years")

        #---------------------
        #class method
        #class itself
        #-----------------------
    @classmethod
    def add_client(cls):
        cls.clients=cls.clients+1

john=BankAccount(name="John Mwangi", balance=0, account_no="223344223")
#samuel=BankAccount(name="Samuel Mwangi", balance=0, account_no="223344224")
#print("john balance is", john.balance)
#john.show_account_details()
# print("bank name is", BankAccount.bank_name)#class property
# print("clients", BankAccount.clients)#class property
# print(john.account_no)#john is an instance of the class
print("Total clients", BankAccount.clients)
samuel=BankAccount(name="Samuel Mwangi", balance=0, account_no="223344224")
print("Total clients", BankAccount.clients)
BankAccount.calculate_interest(50000, 5)