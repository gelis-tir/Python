import smtplib
from email.mime.text import MIMEText
from email.header import Header

# SMTP sunucusu ve kimlik bilgilerini ayarla
smtp_server = ""  # SMTP sunucusunun adresini girin
smtp_port = 000  # SMTP sunucusunun bağlantı noktasını girin örn: 587
username = "kullanici@adi.com"  # E-posta hesabının kullanıcı adını girin
password = ""  # E-posta hesabının parolasını girin

# E-posta gönderenin adresini ayarla
from_address = "mail@adresi.com"

# Mailleri oku
with open("mail.txt", "r", encoding="utf-8") as file:
    mail_list = file.readlines()

# E-posta konusu ve içeriğini mailicerik.txt dosyasından al
with open("mailicerik.txt", "r", encoding="utf-8") as file:
    subject = "E-posta Konusu"
    subject = "E-posta Konusu"
    content = file.read()

# SMTP sunucusuna bağlan ve kimlik doğrulaması yap
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

try:
    # Her bir mail adresine e-posta gönder
    for to_address in mail_list:
        to_address = to_address.strip()  # Satır sonu karakterlerini kaldır

        # E-posta gövdesini oluştur
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = from_address
        message['To'] = to_address
        message['Subject'] = Header(subject, 'utf-8')

        # E-postayı gönder
        server.sendmail(from_address, to_address, message.as_string())

    # Başarılı bir şekilde e-posta gönderildiğini bildir
    print("E-postalar gönderildi!")
except Exception as e:
    # E-posta gönderme sırasında bir hata oluştu
    print("E-postalar gönderilirken bir hata oluştu:", str(e))

# SMTP bağlantısını kapat
server.quit()