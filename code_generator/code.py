COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}

DEST_TABLE = {
    None: "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

JUMP_TABLE = {
    None: "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}


def encode_a_instruction(symbol_or_value, symbol_table=None):
    if str(symbol_or_value).isdigit():
        value = int(symbol_or_value)
    else:
        value = symbol_table.get_address(symbol_or_value)

    return "0" + format(value, "015b")


def dest(mnemonic):
    return DEST_TABLE.get(mnemonic)


def comp(mnemonic):
    return COMP_TABLE.get(mnemonic)


def jump(mnemonic):
    return JUMP_TABLE.get(mnemonic)


def encode_c_instruction(comp_mnemonic, dest_mnemonic=None, jump_mnemonic=None):
    comp_bits = comp(comp_mnemonic)
    dest_bits = dest(dest_mnemonic)
    jump_bits = jump(jump_mnemonic)

    return "111" + comp_bits + dest_bits + jump_bits