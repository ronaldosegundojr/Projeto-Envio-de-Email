import os, smtplib
from email.message import EmailMessage

# Configurar login do email e senha. Inserir manualmente ou importar de algum arquivo.
EMAIL_ADDRESS = 'email@gmail.com' #Endereço de email responsável por fazer envios
EMAIL_PASSWORD = 'senha' #Senha do endereço de e-mail

# Escopo do e-mail
msg = EmailMessage()
msg['Subject'] = 'Inserir assunto do E-mail' #Assunto, Titulo do E-mail
msg['From'] = 'email@gmail.com' #Endereço de E-mail que está enviando o email, origem.
msg['To'] = 'emailrecebedor@gmail.com' #Endereço(s) de email que estará recebendo o email.
msg.set_content('Olá, esse é um email teste') #Corpo do email, texto que será enviado no e-mail.

# Enviar o e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg) #função que envia o email.