# Quintype Assignment
This is the assignment done for Quintype interview. This project is done using python3 and uses the python 
framework django (version 2). There is no communication with database for this project so some dummy data 
was created and stored in the file "data.json" which is present in the folder taxi. This file can be 
modified to change the data of the project.
 
Assumption made by me for the project:
 
1. Python3, PIP3 and virtualenv is already installed. 

## Installation Guide
You should follow the installation instructions to make this project working

1. Change to the directory where you cloned/downloaded the app 
2. Setup a virtual env for our project. This can be done using the command virtualenv

        virtualenv -p python3 env
3. Activate the virtual env using the following command (In the below command you can avoid the path to 
directory part if you are already in that directory else replace it with the actual path):

        source /path/to/directory/env/bin/activate
4. Install the requirements for the project using the command

        pip install -r requirements.txt
5. Start the application using the command
        
        python manage.py runserver