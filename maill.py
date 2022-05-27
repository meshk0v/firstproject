import smtplib

sender = input('Введите отправителя: ')
password = input('Введите пароль от вашей почты: ')
getter = input('Введите получателя: ')
tema = input('Тема сообщения: ')
messager = input('Введите текст: ')

smtp_server = smtplib.SMTP("smtp.rambler.ru", 587)
smtp_server.starttls()
smtp_server.login(sender, password)
subject = tema
body = messager
message = f'Subject: {subject}\n\n{body}'
smtp_server.sendmail(sender, getter, message)
