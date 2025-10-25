
# banking_system.py
# Banking System Implementation using OOP


class Account:
    """Base class representing a general bank account."""

    def __init__(self, acc_number, acc_holder, balance=0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance is available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Return current account balance."""
        return self.balance


class SavingsAccount(Account):
    """Represents a Savings account that earns interest."""

    def __init__(self, acc_number, acc_holder, balance=0.0, interest_rate=0.05):
        super().__init__(acc_number, acc_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Apply interest to the balance (specific to savings accounts)."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return round(self.balance, 2)


class CurrentAccount(Account):
    """Represents a Current account (no interest)."""
    pass


class Transaction:
    """Handles transfer operations between two accounts."""

    @staticmethod
    def transfer(sender, receiver, amount):
        """Transfer money from sender to receiver."""
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        sender.withdraw(amount)
        receiver.deposit(amount)
        return True
