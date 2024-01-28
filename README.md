
# mindMaze - Puddletown Homework Helper

## Local Setup
NOTE: We highly recommend you run the app in a virtual environment

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

- Run the webiste
  - `python manage.py runserver`