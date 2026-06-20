import pytest
from parser.parser import Parser

@pytest.fixture
def mock_asm_file(tmp_path):
    """Cria um arquivo ASM temporário para os testes."""
    file_path = tmp_path / "test.asm"
    file_path.write_text(
        "// Comentário solto\n"
        "@2\n"
        "D=A // Outro comentário\n"
        "(LOOP)\n"
        "0;JMP\n",
        encoding="utf-8"
    )
    return file_path

def test_parser_cleans_lines(mock_asm_file):
    p = Parser(mock_asm_file)
    # Deve ignorar as linhas vazias e remover os comentários inline
    assert len(p.lines) == 4
    assert p.lines[0] == "@2"
    assert p.lines[1] == "D=A"

def test_parser_instruction_types_and_components(mock_asm_file):
    p = Parser(mock_asm_file)
    
    # 1ª Instrução: @2
    p.advance()
    assert p.instruction_type() == "A_INSTRUCTION"
    assert p.symbol() == "2"
    
    # 2ª Instrução: D=A
    p.advance()
    assert p.instruction_type() == "C_INSTRUCTION"
    assert p.dest() == "D"
    assert p.comp() == "A"
    assert p.jump() is None
    
    # 3ª Instrução: (LOOP)
    p.advance()
    assert p.instruction_type() == "LABEL"
    assert p.symbol() == "LOOP"
    
    # 4ª Instrução: 0;JMP
    p.advance()
    assert p.instruction_type() == "C_INSTRUCTION"
    assert p.dest() is None
    assert p.comp() == "0"
    assert p.jump() == "JMP"
    
    assert p.has_more_instructions() is False