#class- CamelCase
class CreditCard:
	#docstring, the first set of comments after the name of class is considered the help for that class
	#help(CreditCard)
	#docstring should be as informative as possible
    '''A consumer credit card.'''
    def __init__ (self, customer, bank, acnt, limit): #constructor- very first method, use def keyword + __init__
        '''Create a new credit card instance.
        The initial balance is zero.
        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt: the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        '''
        #self brings info, use instead of return variableName
        #can use self._customer to show its internal
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        #get()- accessor functions to access private
        #create a get() for each input
    def get_customer(self):
        '''Return name of the customer.'''
        return self._customer
    def get_bank(self):
        '''Return the bank s name.'''
        return self._bank
    def get_account(self):
        '''Return the card identifying number (typically stored as a string).'''
        return self._account
    def get_limit(self):
        '''Return current credit limit.'''
        return self._limit
    def get_balance(self):
        '''Return current balance.'''
        return self._balance
    
    #creating a function to set balance
    #self should accompany all input arguments                                                           ???
    def set_balance(self, balance):
        self._balance = balance

    #create purchase funciton
    #create stop driver?
    def make_purchase(self, amount):
        self._balance += amount
        self._limit -= amount
        
#visa is an instace of class CreditCard
#calling the constructor, don't need __init__
visa = CreditCard('Sally Shoo', 'Vells','1234 5678 9012 3456', 5000)
#cc is another object of type CreditCard
cc = CreditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)
print('visa balance:', visa.get_balance())
print('visa limit:', visa.get_limit())
print('visa account:', visa.get_account())

#ask for balance
#balance = int(input("put in your balance: "))
#put in class
#visa.set_balance(balance)
#print('visa balance has become: ', visa.get_balance()) #get does not take any arguments

new_laptop = visa.make_purchase (1000)
print("The new balance and limit are", visa.get_balance(), visa.get_limit())


