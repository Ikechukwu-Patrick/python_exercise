class InvalidPinException(Exception):
    def __init__(self, Message="Invalid pin number"):
        self.Message = Message
