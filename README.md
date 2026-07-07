# 🚀 Assembler - UFMA 2026.1

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![Build Status](https://img.shields.io/badge/build-in%20development-yellow)

Projeto desenvolvido para a disciplina de **Compiladores** da Universidade Federal do Maranhão (UFMA). O objetivo é construir um **Assembler Hack**, responsável por traduzir programas escritos em Assembly Hack para código binário executável pela plataforma Hack.

---

## 👥 Integrantes

| Nome | Matrícula |
| :--- | :--- |
| Anderson Almeida da Silveira | 20240065590 |
| Jeysraelly Almone da Silva | 20250071222 |

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.13
- Ambiente: Anaconda
- Framework de Testes: pytest

---

## ⚙️ Instalação e Configuração

### Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/assembler.git
cd assembler
```

### Criar ambiente Conda

```bash
conda create -n assembler python=3.13 -y
conda activate assembler
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 📂 Estrutura do Projeto

```text
assembler/
│
├── parser/
├── code/
├── symbol_table/
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Módulos

- **parser/**: leitura e interpretação das instruções Assembly.
- **code/**: conversão das instruções para código binário.
- **symbol_table/**: gerenciamento da tabela de símbolos.
- **main.py**: coordena o processo completo de montagem.
- **tests/**: testes unitários do projeto.

---

## 🎯 Funcionalidades

### Parser

- Leitura de arquivos `.asm`
- Remoção de comentários
- Remoção de linhas em branco
- Identificação de instruções A, C e L

### Code

- Tradução do campo `dest`
- Tradução do campo `comp`
- Tradução do campo `jump`
- Geração das instruções binárias

### Symbol Table

- Símbolos predefinidos
- Registro de labels
- Registro de variáveis
- Resolução de endereços

---

## ▶️ Execução

```bash
python main.py arquivo.asm
```

O programa gerará automaticamente um arquivo `.hack`.

---

## 🧪 Testes

Para executar os testes:

```bash
python -m pytest -v
```

---
## 🎥 Vídeo de Apresentação

https://drive.google.com/file/d/1li1fwRI2lwwkQMLlIeMDW28jqAi7in4h/view?usp=sharing
