# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade nativa do Whatsapp de encaminhar mensagens
# Encaminhar de 5 em 5 mensagens

# Selenium -> permite fazer a automação
# Pyperclip -> permite dar ctrl c / ctrl v em mensagens
# Webdriver-manager -> conversa com o selenium


# 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) # Usado para impedir que o navegador feche após carregar o Whatsapp
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(options=options, service=service)
nav.get("https://web.whatsapp.com") # Abrir o Whatsapp no navegador

time.sleep(20) # Esperar 2 minutos antes de começar a executar o restante do código

mensagem = """Teste, teste, teste, teste, teste! Isso é um teste de mensagens automáticas! Não se assuste!"""

lista_contatos = ["Marcos", "Alan Olinto", "Arteeeeeees", "Trabalho de artes", "Bolinhas de Papel O Filme", "Canal Mister Gast"]

# Enviar a mensagem para meu número

nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click() # Clicar na lupa
time.sleep(1)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Marcos") # Escrever "Marcos"
time.sleep(1)
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER) # Apertar enter
time.sleep(1)
pyperclip.copy(mensagem) # Copiar a mensagem usando o pyperclip
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v') # Colar a mensagem copiada no navegador
time.sleep(1)
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER) # Apertar enter
time.sleep(2)

# Encaminhar a mensagem para a minha lista de contatos
lista_elementos = nav.find_elements('class name', '_2AOIt')
for item in lista_elementos:
    mensagem = mensagem.replace("\n", "")
    texto = item.text.replace("\n", "")
    if mensagem in texto:
        elemento = item
        break

ActionChains(nav).move_to_element(elemento).perform()
elemento.find_element('class name', '_3u9t-').click() # Clicar na setinha da mensagem
time.sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[5]/div/ul/div/li[4]/div').click() # Clicar no encaminhar
time.sleep(1)
nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click() # Clicar no botão encaminhar
time.sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Alan") # Escrever "Alan" na barra de pesquisa
time.sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER) # Apertar enter
time.sleep(1)
nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click() # Clicar no botão de enviar