# Object oriented programing

class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, account, limit, balance) -> None:
        """Create a new credit card instance

        The initial account balance is zero

        Customer : the name of the customer (eg: "Angufibo Lincoln")
        bank     : the name of the bank (eg: "Centenary Bank")
        account  : the account identifier (eg: "5391 0378 9078 7889)
        limit    : credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = balance

    def get_customer(self) -> None:
        """Returns the name of the customer"""
        return self.customer
        
    def get_bank (self) -> None:
        """Returns the bank name"""
        return self.bank
        
    def get_account (self) -> None:
        """Return  card identifying number"""
        return self.account
    
    def make_payment(self, amount):
        self.balance += amount
        
credit_card1 = CreditCard('Summayah Mutyaba', 'Equity Bank', '6578 7890 6578 3444', 999, 555)
print(credit_card1.customer)
print(credit_card1.bank)
print(credit_card1.account)

