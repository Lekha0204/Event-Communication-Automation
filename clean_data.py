"""
Event Attendee Data Cleaning Script
-----------------------------------

This script performs data cleaning on event attendee information loaded from a CSV file.

Main functions:
- Removes duplicate entries based on email addresses
- Normalizes the 'has_joined_event' column to boolean values (Yes/No → True/False)
- Flags rows where LinkedIn profile is missing or incomplete
- Flags rows where the job title is blank or missing
- Saves the cleaned dataset as a new CSV file for further processing

"""

import pandas as pd

def is_linkedin_complete(link):
    if pd.isna(link) or not isinstance(link, str):
        return False
    return "linkedin.com/in/" in link.lower()

df= pd.read_csv("Data - Sheet1.csv")

# Remove duplicate email rows
df = df.drop_duplicates(subset=['email']).copy()

# Normalize has_joined_event values
df.loc[:, 'has_joined_event'] = df['has_joined_event'].map({'Yes': True, 'No': False})

# Identify and flag rows with missing/incomplete LinkedIn profile
df.loc[:, 'Flag_Missing_LinkedIn'] = df['What is your LinkedIn profile?'].isna() | (df['What is your LinkedIn profile?'] == '')

# Identify and flag rows with blank job title
df.loc[:, 'Flag_Blank_Job_Title'] = df['Job Title'].isna() | (df['Job Title'] == '')

# # Save the cleaned version as a new CSV
df.to_csv("cleaned_output.csv", index=False)

print("Cleaned data saved to cleaned_output.csv")

