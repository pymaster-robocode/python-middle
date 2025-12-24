import unittest
from unittest.mock import patch
from main import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("Cat", 100)
        self.acc2 = BankAccount("Bot", 50)

    def test_initial_balance(self):
        self.assertEqual(self.acc.balance, 100)

    def test_deposit(self):
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 150)

    def test_withdraw(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_transfer(self):
        self.acc.transfer(self.acc2, 40)
        self.assertEqual(self.acc.balance, 60)
        self.assertEqual(self.acc2.balance, 90)

    def test_transfer_invalid_account(self):
        with self.assertRaises(TypeError):
            self.acc.transfer("not account", 10)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-10)

    def test_withdraw_too_much(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(1000)

    @patch("main.send_notification")
    def test_deposit_sends_notification(self, mock_notify):
        self.acc.deposit(50)

        mock_notify.assert_called_once_with(
            "Cat",
            "Deposit: 50"
        )

    def test_get_data(self):
        with patch("main.requests.get") as mock_data:
            mock_data.return_value.ok = True
            mock_data.return_value.text = "Success"

            user_data = self.acc.get_data("balance")
            mock_data.assert_called_with("https://bank.data/Cat/balance")
            self.assertEqual(user_data, "Success")

            mock_data.return_value.ok = False

            user_data = self.acc2.get_data("apikey")
            mock_data.assert_called_with("https://bank.data/Bot/apikey")
            self.assertEqual(user_data, "Bad Response!")


if __name__ == "__main__":
    unittest.main()
