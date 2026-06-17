class SymbolTable:
    def __init__(self):
        self.symbols = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
        }

        self.next_address = 16

    def add_entry(self, symbol, address):
        self.symbols[symbol] = address

    def add_variable(self, symbol):
        if symbol not in self.symbols:
            self.symbols[symbol] = self.next_address
            self.next_address += 1

        return self.symbols[symbol]

    def get_address(self, symbol):
        return self.symbols.get(symbol)

    def contains(self, symbol):
        return symbol in self.symbols