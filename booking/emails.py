import smtplib


def send_email(recipient_email):
    # SMTP server settings for Outlook
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    # Email login credentials
    sender_email = "samplemail@gmail.com"
    password = "sample_pass"

    # Email content
    subject = "Confirmation Mail JatraMitra"
    message = "Your account is successfully created. Enjoy!"

    # Construct the email message
    email_message = f"From: {sender_email}\r\nTo: {recipient_email}\r\nSubject: {subject}\r\n\r\n{message}"

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, password)  # Login to the email account
            server.sendmail(
                sender_email, recipient_email, email_message
            )  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print("Error occurred while sending email:", e)


