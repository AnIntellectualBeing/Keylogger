from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

def send_email(server, sender_email, recipient_email, subject, email_message, attachment_data, attachment_filename):
    # Create a multipart message
    message = MIMEMultipart()

    # Set email headers
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add the email message as plain text
    message.attach(MIMEText(email_message, 'plain'))

    # Add the attachment
    attachment = MIMEApplication(attachment_data)
    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_filename)
    message.attach(attachment)

    # Convert the message to a string
    message_string = message.as_string()

    # Send the email
    server.sendmail(sender_email, recipient_email, message_string)
