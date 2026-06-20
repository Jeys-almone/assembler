import pytest
from code_generator.code import encode_a_instruction, dest, comp, jump, encode_c_instruction
from symbol_table.symbol_table import SymbolTable

def test_encode_a_instruction_numeric():
    # Testa um valor numérico direto
    binary = encode_a_instruction("2")
    assert binary == "0000000000000010"

def test_encode_a_instruction_with_symbol():
    st = SymbolTable()
    st.add_variable("counter") # Vai para o endereço 16
    binary = encode_a_instruction("counter", st)
    assert binary == "0000000000010000"

def test_dest_table():
    assert dest("MD") == "011"
    assert dest("AMD") == "111"
    assert dest(None) == "000"

def test_comp_table():
    assert comp("D+1") == "0011111"
    assert comp("M") == "1110000"
    assert comp("0") == "0101010"

def test_jump_table():
    assert jump("JMP") == "111"
    assert jump("JGT") == "001"
    assert jump(None) == "000"

def test_encode_c_instruction():
    # Instrução: D=M (dest=D, comp=M, jump=None)
    binary = encode_c_instruction("M", "D", None)
    # 111 (C-inst) + 1110000 (M) + 010 (D) + 000 (None)
    assert binary == "1111110000010000"
    
    # Instrução: 0;JMP (dest=None, comp=0, jump=JMP)
    binary_jump = encode_c_instruction("0", None, "JMP")
    # 111 (C-inst) + 0101010 (0) + 000 (None) + 111 (JMP)
    assert binary_jump == "1110101010000111"