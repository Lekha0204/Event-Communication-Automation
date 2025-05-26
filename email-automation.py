"""
Event Follow-up Email Automation Script
---------------------------------------

This script reads personalized messages from a CSV file and sends tailored emails 
based on whether a user joined an event or not.

Features:
- Reads a CSV with email, message, and joined status
- Automatically assigns a subject line based on attendance
- Sends emails using Gmail's SMTP with a secure App Password

"""

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# === STEP 1: Load Data from CSV ===
try:
    df = pd.read_csv("personalized_messages.csv")
    print("✅ CSV loaded successfully.")
except FileNotFoundError:
    print("❌ Error: File 'personalized_messages.csv' not found.")
    exit()

# === STEP 2: Your Gmail Configuration ===
FROM_EMAIL = "your.email@gmail.com"                # Replace with your Gmail
APP_PASSWORD = "your_16_character_app_password"    # Replace with your Gmail App Password

# === STEP 3: Email Sending Function ===
def send_email(to_email, subject, body):
    """Composes and sends a single email via Gmail SMTP."""
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start encrypted connection
            server.login(FROM_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print(f"📤 Email sent to: {to_email}")
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")

# === STEP 4: Process Each Row and Send Emails ===
for index, row in df.iterrows():
    to_email = str(row.get('email', '')).strip()
    message = str(row.get('message', '')).strip()
    joined = str(row.get('joined', '')).strip().lower()

    # Skip if email is missing or malformed
    if not to_email or "@" not in to_email:
        print(f"⚠️ Skipping invalid email at row {index + 2}")
        continue

    # Customize subject line based on attendance
    if joined == 'yes':
        subject = "🎉 Thanks for joining the event!"
    else:
        subject = "👀 Sorry we missed you — here’s a quick follow-up!"

    # Send the email
    send_email(to_email, subject, message)

print("\n✅ All emails processed.")
