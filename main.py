import sys

from parser.parser import Parser
from symbol_table.symbol_table import SymbolTable


def main():
    input_file = sys.argv[1]

    parser = Parser(input_file)
    symbols = SymbolTable()

    address = 0

    while parser.has_more_instructions():
        parser.advance()

        if parser.instruction_type() == "LABEL":
            symbols.add_entry(
                parser.symbol(),
                address
            )
        else:
            address += 1

    print(symbols.symbols)


if __name__ == "__main__":
    main()