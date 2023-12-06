# Automação de encaminhamento de mensagens no Whatsapp
# Usando a funcionalidade nativa do Whatsapp de encaminhar mensagens
# Encaminhar de 5 em 5 mensagens

# Selenium -> permite fazer a automação
# Pyperclip -> permite dar ctrl c / ctrl v em mensagens
# Webdriver-manager -> conversa com o selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(options=options, service=service)
nav.get("https://web.whatsapp.com")