
# Krypto Backend Task

A Python-based backend price alert application that triggers an email when the user’s target price is achieved.






## Installation

Install Krypto-task with npm

```bash
  git clone https://github.com/SanthoshrajKG/Krypto-task.git
  cd Krypto-task
  docker compose up
```

    
## Usage

Run the app.py which has the end points and job.py it has the scheduler which continuosly check for the matching bitcoin price and triggers an email.

Navigate to http://127.0.0.1:5000/alerts/create and enter the user data and alert price in text box to create a new alert.

Navigate to http://127.0.0.1:5000/alerts/delete and enter an user name and alert price in text box to delete an alert.

Navigate to http://127.0.0.1:5000/alerts/triggered To view all the triggered alerts till now.

Navigate to http://127.0.0.1:5000/fetch_all/ To view the status of all the alerts till now.

## Screenshots



