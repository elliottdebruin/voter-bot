# Voter Bot

## Requirements

1. You need to have python3 installed. Version 3.3 or newer. To install on Mac run:

`brew install python`

## Step-by-Step

### 1. Download ChromeDriver

Search for “ChromeDriver Chromium” and download the latest version. Once it is downloaded, unzip the file.

Copy the file over from **Downloads**:

`mv ~/Downloads/chromedriver /usr/local/bin`

### 2. Set up Environment

In terminal run:

`python3 -m venv venv`

This will create a virtual environment for us to run the bot. Activate the
environment by running:

`source venv/bin/activate`

Then we need one package in the virtual environment. Execute:

`pip install selenium`

### 3. Sit back and watch the bot run

Run:

`python vote_bot.py`