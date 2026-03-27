import pyautogui
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.pause = 1.5
pyautogui.press("win")
time.sleep (2)
pyautogui.write("chrome")
time.sleep(2.5)
pyautogui.press("enter")
time.sleep (3)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=561, y=304)
time.sleep(1.5)
pyautogui.write("Leonardo Hermano")
pyautogui.press('tab')
time.sleep(1.2)
pyautogui.write("15072008")
pyautogui.press("tab")
pyautogui.write("leoh")
pyautogui.press("enter")
time.sleep(5)
import pandas
tabela = pandas.read_csv (r"C:\Users\lidia\Downloads\produtos (2).csv")
print(tabela)
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=521, y=256)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
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
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write (obs)
    pyautogui.press("tab")
    time.sleep(1.2)
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    pyautogui.scroll(5000) # dar scroll de tudo pra cima
    time.sleep(2)