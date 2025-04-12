import pyautogui
import time
import pandas as pd
from pathlib import Path

# Configurações iniciais
pyautogui.PAUSE = 0.5
URL_LOGIN = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
EMAIL = "wssjlle@gmail.com"
SENHA = "suasenha"
ARQUIVO_CSV = Path(__file__).resolve().parent.parent / "data" / "produtos.csv"



# Coordenadas (ajustar conforme o seu monitor)
COORDS = {
    "campo_email": (470, 406),
    "botao_login": (528, 375),
    "campo_codigo": (573, 262)
}

# Para pegar as coordenadas do mouse e setar aqui nas COORDS, use:
# print(pyautogui.position())
# Dicas:    
# - Mantenha o mouse parado na posição desejada e execute o código.
# - O código vai exibir as coordenadas do mouse no terminal.
# - Quando terminar, copie as coordenadas e cole no dicionário COORDS.
# - Ajuste as coordenadas conforme necessário.



# Funções
# Função para abrir o navegador e acessar a URL de login    

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write(URL_LOGIN)
    pyautogui.press("enter")
    time.sleep(3)

# Função para fazer login no sistema
def fazer_login(email, senha):
    pyautogui.click(*COORDS["campo_email"])
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(3)

# Função para carregar a tabela de produtos
def carregar_tabela(caminho_csv):
    return pd.read_csv(caminho_csv)

# Função para cadastrar produtos
def cadastrar_produtos(tabela):
    for linha in tabela.index:
        pyautogui.click(*COORDS["campo_codigo"])
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):
            pyautogui.write(str(obs))
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(5000)


# Função principal
def main():
    abrir_navegador()
    fazer_login(EMAIL, SENHA)
    tabela = carregar_tabela(ARQUIVO_CSV)
    cadastrar_produtos(tabela)

if __name__ == "__main__":
    main()
