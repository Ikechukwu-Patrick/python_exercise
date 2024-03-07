class InsufficientFundError(Exception):
    def __init__(self, Message="InsufficientFundError"):
        self.Message = Message
