class InvalidPinError(Exception):
    def __init__(self, Message="Invalid PIN"):
        self.Message = Message
