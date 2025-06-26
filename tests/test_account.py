from lib.account import Account

def test_account_initialises_with_correct_attributes(db_connection):
    account = Account(1, "user1", "user1@example.com")
    assert isinstance(account, Account)
    assert account.id == 1
    assert account.username == "user1"
    assert account.email_address == "user1@example.com"


def test_account_repr_method_formats_nicely():
    account = Account(1, "user1", "user1@example.com")
    assert str(account) == "Account(1, user1, user1@example.com)"


def test_accounts_are_equal():
    account_1 = Account(1, "user1", "user1@example.com")
    account_2 = Account(1, "user1", "user1@example.com")
    assert account_1 == account_2