
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

def pullClickUp():
    apiToken = 'pk_81318893_U3BKRQVH2XL48GARBM10W8SYG7RJ6MCU'
    listID = '901100495428'

    api_url = f'https://api.clickup.com/api/v2/list/{listID}/task'
    headers = {
        'Authorization': apiToken,
        'Content-Type': 'application/json'
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        tasks = response.json().get('tasks', [])
        for task in tasks:
            print(f"Task ID: {task['id']}")
            print(f"Task Name: {task['name']}")
            print(f"Status: {task['status']['status']}")
            print("=" * 30)
    else:
        print(f"Failed to retrieve tasks: {response.status_code} - {response.text}")

def send_email(receiver_email, subject, body, smtp_server, port):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = "emrnotifydemo@gmail.com"
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body text to the email
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection with the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()  # Upgrade to secure connection
        server.login("emrnotifydemo@gmail.com", "lrqj dlpz luub sots")

        # Send the email
        server.sendmail("emrnotifydemo@gmail.com", receiver_email, msg.as_string())

        # Terminate the SMTP session and close the connection
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example email
receiver = "jonathan.manda11@gmail.com"
emailSubject = "Test Email"
emailBody = "This is a test email sent using Python."
emailServer = "smtp.gmail.com"
emailPort = 587


pullClickUp()
#send_email(receiver, emailSubject, emailBody, emailServer, emailPort)