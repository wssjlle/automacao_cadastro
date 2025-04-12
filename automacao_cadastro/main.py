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
    "botao_login": (668, 564),
    "campo_codigo": (653, 294)
}

def abrir_navegador():
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write(URL_LOGIN)
    pyautogui.press("enter")
    time.sleep(3)

def fazer_login(email, senha):
    pyautogui.click(*COORDS["campo_email"])
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.click(*COORDS["botao_login"])
    time.sleep(3)

def carregar_tabela(caminho_csv):
    return pd.read_csv(caminho_csv)

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

def main():
    abrir_navegador()
    fazer_login(EMAIL, SENHA)
    tabela = carregar_tabela(ARQUIVO_CSV)
    cadastrar_produtos(tabela)

if __name__ == "__main__":
    main()
