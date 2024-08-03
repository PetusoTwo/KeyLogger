<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentación del Keylogger</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background: #e2e2e2;
            padding: 2px 4px;
            border-radius: 3px;
        }
        pre {
            background: #e2e2e2;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .warning {
            background-color: #fdd;
            border: 1px solid #fbb;
            padding: 10px;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Keylogger</h1>
        <p>Este proyecto es un keylogger en Python que captura las teclas presionadas en una máquina con Windows y envía la información a través de correo electrónico.</p>

        <h2>Autor</h2>
        <p>PetusoTwo</p>

        <h2>Descripción</h2>
        <p>Este keylogger utiliza las bibliotecas <code>win32console</code>, <code>win32gui</code>, <code>pynput</code>, <code>smtplib</code>, y <code>email</code> para:</p>
        <ul>
            <li>Ejecutar el keylogger en segundo plano sin mostrar la ventana de consola.</li>
            <li>Registrar las teclas presionadas en un archivo de texto.</li>
            <li>Enviar el contenido del archivo a una dirección de correo electrónico mediante el protocolo SMTP.</li>
        </ul>

        <h2>Requisitos</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Bibliotecas: <code>pywin32</code>, <code>pynput</code></li>
        </ul>
        <p>Puedes instalar las bibliotecas necesarias usando <code>pip</code>:</p>
        <pre><code>pip install pywin32 pynput</code></pre>

        <h2>Uso</h2>
        <ol>
            <li>
                <strong>Configuración del Correo Electrónico</strong>
                <ul>
                    <li>Abre el archivo de código y establece las credenciales de tu correo electrónico en el bloque de código <code>enviar_datos()</code>:
                        <ul>
                            <li><code>password</code>: Contraseña del correo electrónico desde el cual se enviarán los datos.</li>
                            <li><code>msg['From']</code>: Dirección de correo electrónico desde la cual se enviarán los datos.</li>
                            <li><code>msg['To']</code>: Dirección de correo electrónico a la cual se enviarán los datos.</li>
                        </ul>
                    </li>
                </ul>
            </li>
            <li>
                <strong>Ejecución</strong>
                <ul>
                    <li>Ejecuta el script de Python. El keylogger se ejecutará en segundo plano y comenzará a registrar las teclas presionadas.</li>
                    <li>El archivo <code>log.txt</code> en el directorio de trabajo contendrá las teclas registradas.</li>
                </ul>
            </li>
            <li>
                <strong>Terminación</strong>
                <ul>
                    <li>Para detener el keylogger, presiona la tecla 'Esc'. El script finalizará y enviará el contenido registrado a la dirección de correo electrónico configurada.</li>
                </ul>
            </li>
        </ol>

        <h2>Consideraciones Legales y Éticas</h2>
        <div class="warning">
            <strong>Advertencia:</strong> El uso de keyloggers puede ser ilegal y está sujeto a regulaciones estrictas en muchos países. Utiliza este software solo en entornos legales y con el consentimiento adecuado.
            <br><br>
            <strong>Responsabilidad:</strong> El autor del código no se hace responsable del uso indebido de este software.
        </div>
    </div>
</body>
</html>
