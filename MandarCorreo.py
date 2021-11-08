import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Envio_Correo():
    username = input("Ingresa el correo que enviará el mensaje: ")
    password = getpass.getpass("Ingresa la contraseña: ")

    destinatario = input("Ingresa el correo de tu destinatario: ")
    asunto = input("Ingresa el asunto del correo: ")

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = asunto
    mensaje["From"] = username
    mensaje["To"] = destinatario

    html = f"""
    <html>
    <body>
        Hola {destinatario}
        Esta imagen que te mando es de prueba
    </body>
    </html>
    """

    parte_html = MIMEText(html, "html")
    mensaje.attach(parte_html)

    archivo = input("Ingresa la direccion de la imagen a mandar: ")

    with open(archivo, "rb") as adj:
        contenido_adj = MIMEBase("application", "octet-stream")
        contenido_adj.set_payload(adj.read())

    encoders.encode_base64(contenido_adj)

    contenido_adj.add_header(
        "Content-Disposition",
        f"attachment; filename= {archivo}",
    )

    mensaje.attach(contenido_adj)
    text = mensaje.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        print("Sesión iniciada")
        server.sendmail(username, destinatario, text)
        print("Mensaje enviado")

