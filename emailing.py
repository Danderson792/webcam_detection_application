import smtplib
from email.message import EmailMessage
import imghdr


PASSWORD = 'ushhknokfgeahbvo'
SENDER = 'dave.and.792@gmail.com'
receiver = 'dave.and.792@gmail.com'

def send_email(image_path):
    print('send_email function started')
    email_message = EmailMessage()
    email_message['Subject'] = 'Movement detected.'
    email_message.set_content('There was movement detected on your webcam.')
    print('send_email function ended')

    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='Image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, receiver, email_message.as_string())

    gmail.quit()

if __name__ == '__main__':
    send_email(image_path='images/image33.png')