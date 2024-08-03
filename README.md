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

Puedes instalar las bibliotecas necesarias usando `pip`:

```bash
pip install pywin32 pynput
