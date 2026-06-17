import sys

from parser.parser import Parser
from symbol_table.symbol_table import SymbolTable
from code_generator.code import encode_a_instruction, encode_c_instruction


def first_pass(input_file, symbols):
    parser = Parser(input_file)
    address = 0

    while parser.has_more_instructions():
        parser.advance()

        if parser.instruction_type() == "LABEL":
            symbols.add_entry(parser.symbol(), address)
        else:
            address += 1


def second_pass(input_file, output_file, symbols):
    parser = Parser(input_file)

    with open(output_file, "w", encoding="utf-8") as output:
        while parser.has_more_instructions():
            parser.advance()

            if parser.instruction_type() == "LABEL":
                continue

            if parser.instruction_type() == "A_INSTRUCTION":
                symbol = parser.symbol()

                if symbol.isdigit():
                    binary = encode_a_instruction(symbol)
                else:
                    address = symbols.add_variable(symbol)
                    binary = encode_a_instruction(str(address))

                output.write(binary + "\n")

            elif parser.instruction_type() == "C_INSTRUCTION":
                binary = encode_c_instruction(
                    parser.comp(),
                    parser.dest(),
                    parser.jump()
                )

                output.write(binary + "\n")


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py arquivo.asm")
        return

    input_file = sys.argv[1]
    output_file = input_file.replace(".asm", ".hack")

    symbols = SymbolTable()

    first_pass(input_file, symbols)
    second_pass(input_file, output_file, symbols)

    print(f"Arquivo gerado: {output_file}")


if __name__ == "__main__":
    main()