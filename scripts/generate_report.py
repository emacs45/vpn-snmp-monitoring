import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body):
    from_email = 'your_email@example.com'
    to_email = 'recipient@example.com'
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, 'your_password')
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def generate_report():
    # Generieren Sie hier Ihren Bericht
    report = "Dieser Bericht enthält die neuesten SNMP-Daten."
    send_email("SNMP Report", report)

if __name__ == "__main__":
    generate_report()
