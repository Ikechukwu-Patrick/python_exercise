class InsufficientFundsException(Exception):
    def __init__(self, Message="InsufficientFundsException"):
        Exception.__init__(self)
        self.Message = Message


