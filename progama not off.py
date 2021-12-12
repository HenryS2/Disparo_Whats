#import seleium
#import webdriver
#import webdriver manager
#import time
#instalar chromedriver pelo navagedor que for usar 
# Esta não é uma API oficial então o whatsap podera bloquar o numero
#o whatap esta em constante mudança então qualquer mudança peleo whats poderá afetar o codigo 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
import time 


#Abre o Chrome.
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15) 

#Contatos =  você irar precisar colocar o nome dentro das chaves seguindo a indentação do exemplo 
contatos = ['Ovo',]

#Mensagem colocando a menssagem sempre dentro das aspas [ ' ' ] 
mensagem = 'teste '

#Midia = colocar o caminho sempre que for lançar fotos (Sempre colocando o caminho com barras invertidas [ / ] e colocando sempre a extensão seguindo do ponto [ . ] e)
midia = "C:/Users/user/Desktop/whtas/fotos/00248.PNG"

#Função que pesquisa o Contato/Grupo.
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1) #precisar revisar o tempo
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Função que envia a mensagem.
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(str(mensagem))
    campo_mensagem[1].send_keys(Keys.ENTER)

#Função que envia midia como mensagem.
def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(1)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()    
    
# percorre todas os Defs 
for contato in contatos:
    buscar_contato(contato)
    time.sleep(1)
    enviar_midia(midia)
    time.sleep(1)
    enviar_mensagem(mensagem)          
