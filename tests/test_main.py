import os
import sys
from unittest.mock import patch
from main import main

def test_integration_assembler(tmp_path):
    # 1. Cria um arquivo ASM de teste simulando a soma de variáveis
    asm_file = tmp_path / "add.asm"
    asm_file.write_text(
        "@2\n"
        "D=A\n"
        "@3\n"
        "D=D+A\n"
        "@0\n"
        "M=D\n"
    )
    
    expected_hack_file = tmp_path / "add.hack"
    
    # 2. Roda a função main passando o caminho do arquivo criado como argumento
    with patch.object(sys, 'argv', ['main.py', str(asm_file)]):
        main()
        
    # 3. Verifica se o arquivo .hack foi criado
    assert expected_hack_file.exists()
    
    # 4. Verifica o conteúdo binário gerado
    linhas_geradas = expected_hack_file.read_text().strip().split('\n')
    
    assert linhas_geradas[0] == "0000000000000010" # @2
    assert linhas_geradas[1] == "1110110000010000" # D=A
    assert linhas_geradas[2] == "0000000000000011" # @3
    assert linhas_geradas[3] == "1110000010010000" # D=D+A
    assert linhas_geradas[4] == "0000000000000000" # @0
    assert linhas_geradas[5] == "1110001100001000" # M=D