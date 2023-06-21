import re

# Dosyayı oku
with open("mail.txt", "r", encoding="utf-8") as file:
    mail_list = file.readlines()

valid_mails = []
invalid_mails = []

# Mail adreslerini kontrol et ve geçerli/geçersiz olanları ayır
for mail in mail_list:
    mail = mail.strip()  # Satır sonu karakterlerini kaldır
    if re.match(r"[^@]+@[^@]+\.[^@]+", mail, re.UNICODE):
        valid_mails.append(mail)
    else:
        invalid_mails.append(mail)

# Geçerli mail sayısını ve geçersiz mail sayısını yazdır
print("Geçerli Mail Sayısı:", len(valid_mails))
print("Geçersiz Mail Sayısı:", len(invalid_mails))

# Geçerli mailleri yeni bir dosyaya kaydet
with open("duzeltilmis_mail.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(valid_mails))
