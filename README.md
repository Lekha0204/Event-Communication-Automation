# Event Communication Automation

Automated data cleaning and personalized follow-up messaging for event attendees.

## Overview

This project automates two core tasks:
1. **Data Cleaning** – Prepares raw attendee data for outreach.
2. **Auto-Personalized Messaging** – Generates tailored messages based on user participation, job title, and LinkedIn status.

Optional features include generating `.txt` and `.json` files per user and automating message delivery using SMTP.

---

##  Step 1: Data Cleaning Script

**File:** `clean_data.py`

Cleans and prepares raw attendee data from a CSV file.

### ✨ Features:
- Removes duplicate email rows
- Normalizes `has_joined_event` values (`Yes/No` → `True/False`)
- Flags missing or incomplete LinkedIn profiles
- Flags rows with blank job titles
- Saves the cleaned version as `cleaned_output.csv`

### ✅ Output:
- `cleaned_output.csv`

---

##  Step 2: Auto-Personalized Messaging Script

**File:** `personalized_messaging.py`

Creates customized follow-up messages using cleaned attendee data.

### 📬 Message Logic:
- If **joined the event**:
  > _"Hey Venkatesh, thanks for joining our session! As a freelance developer, we think you’ll love our upcoming AI workflow tools. Want early access?"_

- If **didn’t join**:
  > _"Hi Arushi, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a Product Manager."_

- If **LinkedIn profile is missing**, an additional sentence is added:
  > _"Let us know if you’d like help building your online professional presence!"_

### ✅ Output:
- `personalized_messages.csv` — email + message
- `user_messages/*.txt` — plain-text messages per user
- `user_messages/*.json` — structured messages per user

---

## ⚙️ Step 3: Automation

**File:** `email-automation.py`

Send messages via:
-  ✅ **SMTP setup** (dummy Gmail) tested with personal email — working correctly.

> _This step is designed to demonstrate deployment readiness for messaging automation._

---
