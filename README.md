
# mindMaze - Puddletown Homework Helper

## Local Setup
NOTES: 

1. We highly recommend you run the app in a virtual environment

- Install Homebrew:
  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"`
  - `brew update`
- Install Python: 
  - `brew install python@3.11`
- Create virtual env (if not already done) 
  - `python3.11 -m venv venv`
- Switch to the virtual env
  - `source venv/bin/activate``
- Install django (if not already installed): 
  - `pip install django`
- Install the initial python packages:
  - `pip install python-chess`
  - `pip install plotly`
  - `pip install pandas`
  - `pip install whitenoise`

- Run any appropriate migrations (if prompted, when you run the site)
  - `python manage.py migrate`

- (First-time) Setup admin user in your local DB
  - `python manage.py createsuperuser` 

- Run the webiste
  - `python manage.py runserver`

- (First-time) Setup Training Terms and Levels
  - Login via django admin panel (http://127.0.0.1:8000/)
  - Create a Training Term
  - Create the appropriate Training Levels (the names should match exactly as below)
    - Level_1
    - Level_2
    - Level_3
    - Level_4
    - Elite_Level
  - Create 1 or more puzzles that you want to test with

- Now you can create a test training user and login with that user and play around