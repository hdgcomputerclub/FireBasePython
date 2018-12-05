# FireBasePython
Hello Club,

I found the problem we had on Wednesday.

The issue was I had stored the credentials
Use this command to undo the store:
sudo git config credential.helper cache

We need to remove the git stored file then make sure it doesnt come back!!

sudo nano /root/.gitconfig, get rid of username stuff.!


December 6th, 2018 Goals:

Team "Breadboard" [Project "FireBasePython"]
    - Develop a method for the Python code to receive it's configuration from a webservice call.
    - pass in the wlan0 mac address "Finding the MAC of a Raspberry Pi" in google
    - develop the function in the Utilities folder as a new file "RaspberryPi.py"
    - follow method on "Time and Read Mr. Scott" to import the function.
    - Call the endpoint (request.get) "http://climaedu.com/api/getRoomId"

Team "Web Application" [Project "climaedu"]
    - Develop api signatures for saving sensor data (already stubbed out in /server/controllers/api.js) with MYSQL
    - Work on getRoomID & getCurrentTemperature

Team "UI" [Project TBD] -using the Mac
    - Develop github repository to save work.
    - Get the latest Temperature and display on the screen:
        - For this week, we will have the temperature appear on a button click.
        - use the endpoint "http://climaedu.com/api/getCurrentTemperature"
        - understand "state" and how react handles state + rendering.
    - Develop a method for logging into the application. Follow: "React Native & Firebase: Authentication by Faraz Amiruddin Ahmad"
         - must build a Firebase DB with the club's google account.

