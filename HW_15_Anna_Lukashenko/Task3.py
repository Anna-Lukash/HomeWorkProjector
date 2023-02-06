'''A Bank
A. Using the Account class as a base class, write two derived classes called SavingsAccount and CurrentAccount. A SavingsAccount object, in addition to the attributes of an Account object, should have an interest attribute and a method which adds interest to the account. A CurrentAccount object, in addition to the attributes of an Account object, should have an overdraft limit attribute.

B. Now create a Bank class, an object of which contains an array of Account objects. Accounts in the array could be instances of the Account class, the SavingsAccount class, or the CurrentAccount class. Create some test accounts (some of each type).

C. Write an update method in the Bank class. It iterates through each account, updating it in the following ways: Savings accounts get interest added (via the method you already wrote); CurrentAccounts get a letter sent if they are in overdraft. (use print to 'send' the letter).

D. The Bank class requires methods for opening and closing accounts, and for paying a dividend into each account.'''

class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number
    
    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance
    
    def get_account_number(self):
        return self._account_number
    
    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'

# derived class - SavingsAccount with new atribute interest.
class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest
    # method that adds interrest to a balance   
    def add_interest(self):
        self._balance += self._balance * self.interest/100
       
# derived class - CurrentAccount  with new atribute overdraft_limit.   
class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

 # test accounts (some of each class).
joe = Account(550, 93845146)
anna = Account(87_543, 53429876)
den = SavingsAccount(76_045, 76354797, 2.8)
julie = CurrentAccount(13_975, 34187534, -10_000)
elaine = CurrentAccount(-4564, 76345698, -9000)
fred = SavingsAccount(234_456, 65429309, 1.3)
kiki = CurrentAccount(-600, 54637898, -1000)
account_array = [joe, anna, den, julie, elaine, fred, kiki]

#Bank class, an object of which contains an array of Account objects
class Bank():
    def __init__(self, object_array):
        self.object_array = object_array
    # update method iterates through each account. Savings accounts get interest added. CurrentAccounts get a letter sent if they are in overdraft.
    def update(self):
        for object in self.object_array:
            if isinstance(object, SavingsAccount):
                object.add_interest()
                print(f"Your current balance on account {object.get_account_number()} is {object.get_balance()}$.")
            elif isinstance(object, CurrentAccount):
                if object.get_balance() < 0:
                    print(f"Oops. Your account {object.get_account_number()} is overdrawn. Current balance is {object.get_balance()}$. Your overdraft limit {object.overdraft_limit}$.") 
    #method for opening account              
    def open_account(self):
        new = Account(0,int(input('Please enter an account number:')))
        print(self.object_array)
        self.object_array.append(new)
        print(self.object_array)
        print(f"Account has been successfully created. Your account number is {new.get_account_number()}. Your balance is {new.get_balance()}$.")
    
    #method for closing account     
    def close_account(self):
        closing_account = int(input("Please enter account, which has to be closed. "))
        for object in self.object_array:
            if object.get_account_number() == closing_account:
                self.object_array.remove(object)
                print(f"Account {object.get_account_number()} has been successfully closed.")
    
    
            
new_acounts = Bank(account_array) 
print(new_acounts.update())
print(new_acounts.close_account())

