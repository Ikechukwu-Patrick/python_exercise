class AccountNotFoundException(Exception):
    def __init__(self, Message="Account Not Found"):
        self.message = Message
