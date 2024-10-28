# This is just the template

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_email, subject, body, smtp_server, port):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = "EMRnotifyDemo@outlook.com"
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection with the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()  # Upgrade to secure connection
        server.login("EMRnotifyDemo@outlook.com", "loopsolutions1122")

        # Send the email
        server.sendmail("EMRnotifyDemo@outlook.com", receiver_email, msg.as_string())

        # Terminate the SMTP session and close the connection
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example email
receiver = "jonathan.manda11@gmail.com"
subject1 = "Test Email"
body1 = "This is a test email sent using Python."
emailServer = "smtp-mail.outlook.com"
port1 = 587



send_email("jonathan.manda11@gmail.com", subject1, body1, emailServer, port1)