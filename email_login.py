import smtplib

def login_email(username, password):
    # SMTP server settings for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS encryption
    server.starttls()

    try:
        # Log in to the email account
        server.login(username, password)
        print("Login successful!")

        return server
    except smtplib.SMTPAuthenticationError:
        print("Failed to log in. Please check your email credentials.")
        return None
