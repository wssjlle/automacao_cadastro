# Automação de Cadastro de Produtos

Este projeto realiza o cadastro automatizado de produtos em um sistema web usando Python e a biblioteca PyAutoGUI.

## Funcionalidades

- Abre o navegador automaticamente.
- Acessa o sistema de login da empresa.
- Realiza login com e-mail e senha.
- Lê uma planilha `.csv` com dados dos produtos.
- Cadastra cada produto no sistema de forma automatizada.

## Como usar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

2. Insira o arquivo `produtos.csv` na pasta `data/`.

3. Execute o script:
   ```
   python automacao_cadastro/main.py
   ```

> **Atenção:** Certifique-se de ajustar as coordenadas de clique no seu monitor, se necessário.

## Licença

MIT
