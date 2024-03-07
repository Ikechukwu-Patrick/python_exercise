class InvalidAmountError(Exception):
    def __init__(self, Message="Invalid Amount"):
        self.Message = Message
