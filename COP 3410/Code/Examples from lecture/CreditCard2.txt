# anyone can use the class if they import it
# including methods & help


# parent class
class CreditCard:
    '''A consumer credit card.'''     #docstring, the first set of comments after the name of class is considered the help for that class. help(CreditCard)  

    # have to create initiator / constructor for any class you create
    # include all variables / objects you are bringing in from outside
    # self is in every class, points to current object 
    def __init__ (self, customer, bank, acnt, limit):   #The constructor is the very first method

        # docstring with each element clearly defined
        '''Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman )
        bank: the name of the bank (e.g., California Savings )
        acnt : the acount identifier (e.g., 5391 0375 9387 5309 )
        limit: credit limit (measured in dollars)
        '''

        # doesn't have to be the same name
        self._customer = customer 
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0         # we start with a balance of zero, this is private, nobody can change it


    # methods- start with a verb- tells what function does
    def get_customer(self):   #The get functions are a must, they're called accessor functions (methods)
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

    # changing the balance- bring balance from outside to change set it
    # update set balance function?
    def set_balance(self,balance):
        
        self._balance = balance
        # decrease the limit if the balance goes up
        self._limit -= balance

    def make_purchase(self,purchase):

        if (purchase + self._balance) <= self._limit:
            # add purchase price to balance
            self._balance += purchase
            self._limit -= purchase
            return True 
        else:
            return False
        
    def make_payment(self,payment):
        self._limit += payment


# inheritance- adding to parent card
# inheriting all methods & allowed to use all of the instances of CreditCard
# parent class in side parenthesis
class ModernCreditCard(CreditCard):

    # still needs constructor
    # adding apr
    def __init__ (self, customer, bank, acnt, limit, apr):
     '''Create a new predatory credit card instance.
     The initial balance is zero.

     customer the name of the customer (e.g., John Bowman )
     bank the name of the bank (e.g., California Savings )
     acnt the acount identifier (e.g., 5391 0375 9387 5309 )
     limit credit limit (measured in dollars)
     apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
     '''

     #calls parent constructor 
     super(). __init__ (customer, bank, acnt, limit) # call super constructor
     # self imports apr into the class
     self._apr = apr

     def make_purchase(self, purchase):                   #may not be fully operation yet
         '''Charge given price to the card, assuming sufficient credit limit.
            Return True if charge was processed.
            Return False and assess 5 fee if charge is denied.
         '''
         success = super().make_purchase(purchase)     #inherited method- use super
         if not success:
            # override parent's action, 5 dollar charge if it does not go through
             self._balance += 5
         return success

    # create new method that parent cannot use
    def process_month(self):
        '''Assess monthly interest on outstanding balance'''
        if self. balance > 0:
            #if positive balance, convert APR to monthly multiplicative factor
            # square root of 12 on apr
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance = monthly_factor
      

# uses test cases to test the class inside the same script file
# allows you to test the entire class inside the script
# won't see the test case when someone else uses it- not their main file
# always add this as a test case in your file
# creditcard2 is automatically the main file
# main acts as stop driver
# if removed, will execute automatically
# for assignments create class, then use first line to create test case
# call all of the methods- can use loop
if __name__ == "__main__":
    wallet = []    
    visa = ModernCreditCard('Sally Shoo', 'Vells','1234 5678 9012 3456', 5000,0.0825)   #calling the constructor
    cc = CreditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)
    wallet.append(visa)
    wallet.append(cc)
    print('visa balance:', visa.get_balance())
    print('visa limit:', visa.get_limit())
    print('visa account:', visa.get_account())

    balance = int(input("put in your balance: "))
    visa.set_balance(balance)
    print('visa balance has become:', visa.get_balance())

    '''for val in range(1, 17):
        wallet[0].make_purchase(val)
        wallet[1].make_purchase(2*val)'''


    new_laptop = cc.make_purchase(1000)
    print("The new balance and limit are", cc.get_balance(), cc.get_limit())

    
    visa.process_month()
    print ("process month for visa:", visa.get_balance())
