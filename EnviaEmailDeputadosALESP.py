# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''Senhor Deputado,
Amanhã, 15 de março de 2021 será um dia muito importante para o nosso Estado de SP: será decidido o presidente da ALESP.
O governador atual vem se comportando de maneira não condizente com o cargo e eu acredito que o começo da mudança passa por esta casa, 
pelo teu voto amanhã no Major Mecca, que se mostra o único capaz de ser oposição à TIRANIA DE JOÃO DÓRIA.
Honre os votos recebidos nas eleições passadas concedidos pelo povo Paulista. Isso não será esquecido.
Obrigado'''


#The mail addresses and password
sender_address = 'maciel.oliveira.reinaldo@gmail.com'
sender_pass = 'XXXXXXXXXXXX'
message = MIMEMultipart()
message['Subject'] = 'Prezado deputado, APOIE O MAJOR MECCA'   #The subject line
message['From'] = sender_address
f = open("Lista.csv", "r")
for x in f:
    x = x.rstrip('\n').rstrip('\r')
    x = x.decode('utf-8-sig')
    print('Enviando email para: ', x)
    receiver_address = x
    #Setup the MIME
    message['To'] = receiver_address
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    try:
        session.sendmail(sender_address, receiver_address, text)
        print('Mail Sent to: ', x)
    except:
        print('Erro ao mandar email para: ', x)
    session.quit()
f.close()