import pytest
from symbol_table.symbol_table import SymbolTable

def test_initialization():
    st = SymbolTable()
    # Verifica símbolos predefinidos
    assert st.get_address("R0") == 0
    assert st.get_address("R15") == 15
    assert st.get_address("SCREEN") == 16384
    assert st.get_address("KBD") == 24576
    assert st.next_address == 16

def test_add_entry_for_labels():
    st = SymbolTable()
    st.add_entry("LOOP", 10)
    assert st.get_address("LOOP") == 10
    assert st.contains("LOOP") == True

def test_add_variable():
    st = SymbolTable()
    
    # Primeira variável deve ir para o endereço 16
    addr1 = st.add_variable("i")
    assert addr1 == 16
    
    # Segunda variável deve ir para o endereço 17
    addr2 = st.add_variable("sum")
    assert addr2 == 17
    
    # Tentar adicionar a mesma variável de novo não deve incrementar o endereço
    addr1_again = st.add_variable("i")
    assert addr1_again == 16
    assert st.next_address == 18