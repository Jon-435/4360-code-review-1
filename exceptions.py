# 3. Fixed spelling error
class BankingException(Exception):
    pass
# 4. Changed to string for simplicity and for exception messages.

class InsufficientFundsException(BankingException):
    def __str__(self):
        return 'An error occurred: Insufficient Funds'

class InvalidAccountNumberException(BankingException):
    def __str__(self):
        return "An error occurred: Invalid Account Number"