"""
Event Follow-up Personalized Messaging Script
---------------------------------------------

This script reads cleaned event attendee data from a CSV file, then generates 
customized messages for each attendee based on their event attendance, job title, 
and LinkedIn profile presence.

Features:
- Reads cleaned data CSV with attendee information
- Generates personalized messages tailored to each attendee's event participation status
- Flags missing LinkedIn profiles with an additional prompt
- Saves all messages in a combined CSV file (email + message)
- Exports individual user messages in both .txt and .json formats for easy access or integration

"""

import pandas as pd
import os
import json

# Load the cleaned data CSV into a pandas DataFrame
df = pd.read_csv("cleaned_output.csv")

def generate_message(row):
    # Extract the first name
    name = row['first_name']
    
    # Get the job title if available and non-empty, else use a default phrase
    job = row['Job Title'] if pd.notna(row['Job Title']) and row['Job Title'].strip() != "" else "a professional like you"
    
    # Normalize 'has_joined_event' to a boolean value
    joined = str(row['has_joined_event']).strip().lower() == 'true'
    
    # Check if LinkedIn profile is present and non-empty
    has_linkedin = pd.notna(row['What is your LinkedIn profile?']) and row['What is your LinkedIn profile?'].strip() != ""

    # Generate message based on event attendance
    if joined:
        message = f"Hey {name}, thanks for joining our session! As {job}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        message = f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as {job}."

    # Add additional note if LinkedIn profile is missing
    if not has_linkedin:
        message += " Let us know if you’d like help building your online professional presence!"

    return message

# Apply the message generation function to each row and create a new 'message' column
df['message'] = df.apply(generate_message, axis=1)

# Save the resulting DataFrame with only 'email' and 'message' columns to a CSV file
df[['email', 'message']].to_csv("personalized_messages.csv", index=False)

# Create a directory to save individual user message files (txt and json)
os.makedirs("user_messages", exist_ok=True)

# Loop through each row to save messages in separate files
for _, row in df.iterrows():
    # Create a safe filename by replacing '@' and '.' in the email
    filename = row['email'].replace("@", "_at_").replace(".", "_dot_")
    
    # Save message as a .txt file
    with open(f"user_messages/{filename}.txt", "w") as f:
        f.write(row['message'])

    # Save message and email as a .json file for structured storage
    with open(f"user_messages/{filename}.json", "w") as f:
        json.dump({"email": row['email'], "message": row['message']}, f, indent=2)

print("Messages generated and saved to personalized_messages.csv and user_messages/ folder.")
