# Gmail-Python-Alarm

An alarm app that triggers when you receive an email from an email ending with ".edu"

To set up on your end:

1. Pre-Req:
   - Have Python 3 installed on your machine.
   - pip install playsound
     - If error occurs try pip install --upgrade wheel. Then re-attempt pip install playsound
2. Replace the gmail/password in the alerts.py file with your own, placeholder emails exist there for reference. Please follow the steps below.

   - Visit https://myaccount.google.com/security
   - Under "2-Step Verification," select App Passwords.
   - At the bottom, choose Select app and choose the app you’re using.
     - Select "Other", and then you'll be given an option to provide a custom name. You can name it something like "Python Email Alert" or anything that you would recognize.
   - Choose Generate.
   - Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
     - Do not add spaces.
   - Choose Done.

3. To Run App.
   - Use Terminal or Cmd line, cd into the directory, and run the following command:
     - python3 alerts.py
