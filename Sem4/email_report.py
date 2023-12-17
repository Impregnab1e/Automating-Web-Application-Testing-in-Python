import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendemail():
    fromaddr = 'kissk@mail.ru'
    toaddr = 'kissk@mail.ru'
    mypass = 'uUdBVZxtkihN0iuUCphf'
    reportname = 'E:/Учеба/Учусь/Automating Web Application Testing in Python/Sem4/log.txt'

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Отчет Тестовый стенд'

    with open(reportname, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(
            reportname)
        msg.attach(part)

    body = 'Test'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smpt.mail.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    sendemail()
