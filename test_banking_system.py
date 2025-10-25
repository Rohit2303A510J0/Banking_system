
# test_banking_system.py
# Unit Tests for Banking System


import unittest
from banking_system import Account, SavingsAccount, CurrentAccount, Transaction

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        """Create sample accounts before each test."""
        self.savings = SavingsAccount("S001", "Alice", 1000.0, 0.10)
        self.current = CurrentAccount("C001", "Bob", 500.0)

    # --- Deposit Tests ---
    def test_deposit_valid_amount(self):
        self.savings.deposit(200)
        self.assertEqual(self.savings.get_balance(), 1200.0)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.current.deposit(-100)

    # --- Withdrawal Tests ---
    def test_withdraw_valid_amount(self):
        self.current.withdraw(200)
        self.assertEqual(self.current.get_balance(), 300.0)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.current.withdraw(800)

    # --- Transfer Tests ---
    def test_transfer_valid(self):
        Transaction.transfer(self.savings, self.current, 300)
        self.assertEqual(self.savings.get_balance(), 700.0)
        self.assertEqual(self.current.get_balance(), 800.0)

    def test_transfer_negative_amount(self):
        with self.assertRaises(ValueError):
            Transaction.transfer(self.savings, self.current, -50)

    # --- Interest Calculation ---
    def test_interest_applied_only_to_savings(self):
        self.savings.apply_interest()
        self.assertEqual(self.savings.get_balance(), 1100.0)

    def test_current_account_no_interest_method(self):
        with self.assertRaises(AttributeError):
            self.current.apply_interest()


if __name__ == "__main__":
    unittest.main()
