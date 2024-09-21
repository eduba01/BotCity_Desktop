 
# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Import classe do excel da botcity
from botcity.plugins.excel import BotExcelPlugin

# Importar biblioteca para manipular diretórios
from pathlib import Path

# bibliotecas para imagem
import cv2
import pytesseract
from PIL import Image
 

#from botcity.core import DesktopBot
#from botcity.maestro import *
from random import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
 

# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())
 
# Variaveis  

# PETR4 ######################  
acao1 = "PETR4"
x = 125  # linha
y = 145  # coluna
                    # 3614
acao1_valor_compra = "3510"
acao1_valor_venda = "3710"

# VALE3 ######################  
acao2 = "VALE3"
x = 125  
y = 145
acao2_valor_compra = "6000"
acao2_valor_venda = "6500"
##############################



def main():
    try:
 
        bot = DesktopBot()
        
        # Abrir o programa
        dir_exec_app = r"C:\\Program Files\\Clear Investimentos MT5 Terminal\\terminal64.exe"
        bot.execute(dir_exec_app)
        
        # Identificando o PID do processo do App no Windows
        app_windows_process = bot.find_process("terminal64.exe")
        
###################################################################################################
 
        if not bot.find( "petr4", matching=0.97, waiting_time=10000):
            not_found("petr4")
        bot.click()
        
        if not bot.find( "Petr4-click", matching=0.97, waiting_time=10000):
            not_found("Petr4-click")
        
                # # To get the mouse coordinate.
                # xx = bot.get_last_x()
                # yy = bot.get_last_y()

                # print(f'The last saved mouse position is: {xx}, {yy}')


 
        # capturando a imagem com o valor da ação
        #img = bot.screen_cut(x, y, l, p)
        img = bot.screen_cut(x, y, width=40, height=20)
        img.save("cotacao.png")

 
        # Convertendo a imagem em texto
        imagem = cv2.imread("cotacao.png")
        caminho = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
        cotacao = pytesseract.image_to_string(imagem)

        # Cotação da açao
        print()
        print("COTAÇÃO")
        print()
        print(f'{acao1}    R$ {cotacao}')
        print(f'{acao2}    R$ {cotacao}')
         

        if  cotacao <= acao1_valor_compra:
            #bot.execute(dir_exec_app)
            print(f'{acao1} A cotação esta dentro do valor esperado para a compra:  R$ {acao1_valor_compra}')
            print(f'{acao1} ------- COMPRAR -------')
            print()
        if  cotacao >= acao1_valor_venda:
            #bot.execute(dir_exec_app)
            print(f'{acao1} A cotação esta dentro do valor esperado para a venda:  R$ {acao1_valor_venda}')
            print(f'{acao1} ------- VENDER -------')
            print()
   
        # # Criar um for e um while

        # if  cotacao <= acao2_valor_compra:
        #     #bot.execute(dir_exec_app)
        #     print(f'{acao2} A cotação esta dentro do valor esperado para a compra:  R$ {acao2_valor_compra}')
        #     print(f'{acao2} ------- COMPRAR -------')
        #     print()
        # if  cotacao >= acao2_valor_venda:
        #     #bot.execute(dir_exec_app)
        #     print(f'{acao2} A cotação esta dentro do valor esperado para a venda:  R$ {acao2_valor_venda}')
        #     print(f'{acao2} ------- VENDER -------')
        #     print()



                # coord_elemento = bot.get_element_coords(label="Petr4-click", x="", y="" ,width="", height="", matching=0.97)
                # print(f'--coordenadas da imagem Petr4-click.png: {coord_elemento}')
                

###################################################################################################

    except Exception as e:
        # Handles the exception
        print(f"##########################################################################################################################")
        print(f"An error occurred: {e}")
        print(f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        # Log the exception to Rollbar
     
    finally:
        if not app_windows_process is None:
            # Encerra o App
            bot.terminate_process(app_windows_process)
            print(f"------------ F I M ------------") 
            
###################################################################################################

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()


