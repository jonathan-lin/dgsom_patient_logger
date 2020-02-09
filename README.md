# dgsom_patient_logger
Patient logging script

This script automates the patient encounter logging process on Gryphon. Currently it only works for the surgical subspecialties that I rotated on but it can be easily extended to include any rotation/specialty.

The script requires python, selenium and a webdriver (I use geckodriver but chromedriver should work as well)

Enter your data into a dictionary as shown at the top of patientloggerconstant.py

When you initiate the script, there will be a 30 second pause for you to log into gryphon.
