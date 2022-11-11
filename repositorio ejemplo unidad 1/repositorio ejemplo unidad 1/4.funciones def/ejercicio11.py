import smtplib

fromaddr = 'car.caceres.ochoa@gmail.com'
toaddrs  = 'car.caceres.ochoa@hotmail.com'
msg = 'Correo enviado utilizano Python + smtplib en www.pythondiario.com'


# Datos
username = 'car.caceres.ochoa@gmail.com'
password = 'cjcaceres741852'

# Enviando el correo
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
