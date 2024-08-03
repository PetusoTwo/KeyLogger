# Keylogger

Este proyecto es un keylogger en Python que captura las teclas presionadas en una máquina con Windows y envía la información a través de correo electrónico.

## Autor

PetusoTwo

## Descripción

Este keylogger utiliza las bibliotecas `win32console`, `win32gui`, `pynput`, `smtplib`, y `email` para:

- Ejecutar el keylogger en segundo plano sin mostrar la ventana de consola.
- Registrar las teclas presionadas en un archivo de texto.
- Enviar el contenido del archivo a una dirección de correo electrónico mediante el protocolo SMTP.

## Requisitos

- Python 3.x
- Bibliotecas: `pywin32`, `pynput`

## Uso

### Configuración del Correo Electrónico

Abre el archivo de código y establece las credenciales de tu correo electrónico en el bloque de código `enviar_datos()`:

- `password`: Contraseña del correo electrónico desde el cual se enviarán los datos.
- `msg['From']`: Dirección de correo electrónico desde la cual se enviarán los datos.
- `msg['To']`: Dirección de correo electrónico a la cual se enviarán los datos.

### Ejecución

- Ejecuta el script de Python. El keylogger se ejecutará en segundo plano y comenzará a registrar las teclas presionadas.
- El archivo `log.txt` en el directorio de trabajo contendrá las teclas registradas.

### Terminación

- Para detener el keylogger, presiona la tecla 'Esc'. El script finalizará y enviará el contenido registrado a la dirección de correo electrónico configurada.

## Consideraciones Legales y Éticas

> **Advertencia:** El uso de keyloggers puede ser ilegal y está sujeto a regulaciones estrictas en muchos países. Utiliza este software solo en entornos legales y con el consentimiento adecuado.
>
> **Responsabilidad:** El autor del código no se hace responsable del uso indebido de este software.

Puedes instalar las bibliotecas necesarias usando `pip`:

```bash
pip install pywin32 pynput
