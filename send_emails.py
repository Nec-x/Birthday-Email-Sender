import smtplib
import ssl
from email.message import EmailMessage
import own_variables as ov


def sender(name,email):
    """
    Sends a birthday email to a client. Variable user and password obtained from private file. Are strings.
    """

    user = ov.sender_email
    password = ov.pass_key
    reciever = email

    subject = f"Happy Birthday {name}!"

    em = EmailMessage()
    em['From'] = user
    em['To'] = reciever
    em['Subject'] = subject
    em.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style = "color:red;">Here at PlusUltra Reality, we want to wish you a happy birthday!</h1>
            <img src="https://static5.depositphotos.com/1006739/414/i/600/depositphotos_4141194-stock-photo-singing-saint-bernard-puppies-with.jpg">
            <h1 style = "color:red;">We appreciate your continued business with us, and hope for many more.</h1>

    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
        smtp.login(user, password)
        smtp.send_message(em)
