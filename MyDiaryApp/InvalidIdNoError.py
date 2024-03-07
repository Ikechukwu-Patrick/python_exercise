class InvalidIdNoError(Exception):
    def __init__(self, Message="Invalid ID"):
        self.Message = Message
