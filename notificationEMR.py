# This is just the template

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, smtp_server, port, login, password):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection with the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Upgrade to secure connection
        server.login(login, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Terminate the SMTP session and close the connection
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
if __name__ == "__main__":
    sender = "your_email@gmail.com"
    receiver = "recipient_email@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."
    smtp_server = "smtp.gmail.com"
    port = 587
    login = "your_email@gmail.com"
    password = "your_email_password"

    send_email(sender, receiver, subject, body, smtp_server, port, login, password)

    #test