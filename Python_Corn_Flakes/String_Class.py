def scanner(param):
    pass


def getString():
    scanner("Enter your data...")


class Input:
    def __init__(self):
        self.data = None

    def __int__(self):
        self.data = ""

    def printString(self):
        return f'{self.data.upper()}'


bolaji = Input()
getString()
print(bolaji.printString())


