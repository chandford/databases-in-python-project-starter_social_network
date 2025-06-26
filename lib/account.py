class Account:
    
    def __init__(self, id, username, email_address):
        self.id = id
        self.username = username
        self.email_address = email_address

    def __repr__(self):
        return f"Account({self.id}, {self.username}, {self.email_address})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__