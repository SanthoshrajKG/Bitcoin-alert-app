#A Python-based backend price alert application that triggers an email when the user’s target price is achieved.






## Installation

Install Krypto-task with npm

```bash
  git clone https://github.com/SanthoshrajKG/Krypto-task.git
  cd Krypto-task
  docker compose up
```

    
## Usage

Docker runs the app.py which has the end points and runs job.py where I hard coded sender email id and password(google App password) for now, you can change it if required, it has the scheduler which continuosly check for the matching bitcoin price and triggers an email.

Navigate to http://127.0.0.1:5000/alerts/create and enter the user data and alert price in text box to create a new alert.

Navigate to http://127.0.0.1:5000/alerts/delete and enter an user name and alert price in text box to delete an alert.

Navigate to http://127.0.0.1:5000/alerts/triggered To view all the triggered alerts till now.

Navigate to http://127.0.0.1:5000/fetch_all/ To view the status of all the alerts till now.

## Screenshots
![image](https://user-images.githubusercontent.com/87854476/184536958-ea5eec13-aa9c-46d4-91fb-5be752a6727c.png)
![image](https://user-images.githubusercontent.com/87854476/184536966-f66fcf25-c9b8-4c43-847a-680a102af316.png)
![image](https://user-images.githubusercontent.com/87854476/184536998-691876d7-4973-4422-8e14-da57a4eae738.png)
![image](https://user-images.githubusercontent.com/87854476/184537052-d4022dc7-d1a8-487e-ab92-2e8ba1fbe1fb.png)
![image](https://user-images.githubusercontent.com/87854476/184537059-61a83d33-0232-497d-8015-8092f5dc793d.png)
![image](https://user-images.githubusercontent.com/87854476/184537097-f86215f2-da3f-498c-8f6d-9c3d5fa282d8.png)
![image](https://user-images.githubusercontent.com/87854476/184537117-89152322-22b7-42d3-b7c9-d4f5be0e7deb.png)
![image](https://user-images.githubusercontent.com/87854476/184537177-a9753044-f27c-4121-a21e-0faef4697afc.png)






