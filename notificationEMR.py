
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def pullClickUp():
    api_key = 'pk_81318893_U3BKRQVH2XL48GARBM10W8SYG7RJ6MCU'
    listID = '901100495428'

    apiURL = f'https://api.clickup.com/api/v2/list/{listID}/task'
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(apiURL, headers=headers)
    if response.status_code == 200:
        tasks = response.json().get('tasks', [])
        for task in tasks:
            print(f"Task ID: {task['id']}")
            print(f"Task Name: {task['name']}")
            print(f"Status: {task['status']['status']}")
            print("=" * 30)
    else:
        print(f"Failed to retrieve tasks: {response.status_code} - {response.text}")


def createLink(user, hospital, hlink):
    apiURL = "https://app.linklyhq.com/api/v1/link"

    headers = {
        "Content-Type": "application/json"
    }

    # Link data to be created
    data = {
        "api_key" : "yxKzDSVmCaU/TRZMCaFdjw==",
        "workspace_id": 244134,
        "enabled": True,
        "block_bots": False,
        "public_analytics": False,
        "url": f"{hlink}",
        "name": user + " at " + hospital,
        "og_description": f"This is a link for {user} at {hospital}."
    }

    # Make the POST request to create the link
    try:
        response = requests.post(apiURL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        link_data = response.json()  # The created link's data in JSON format
        print("Link created successfully:", link_data)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


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

#createLink('Jonathan', 'GitHub', 'https://github.com/')
#pullClickUp()
#send_email(receiver, emailSubject, emailBody, emailServer, emailPort)