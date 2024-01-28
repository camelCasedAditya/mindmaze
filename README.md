
# mindmaze

MindMaze - Homework Helper

Local Setup
We highly recommend you run the app in a virtual environment

- Install Homebrew:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"`
- `brew update`
- Install Python: 
  - `brew install python@3.11`
- Switch to virtual env 
  - `python3.11 -m venv venv`
- Install django : 
  - `pip install django`
- Install the initial python packages:
  - `pip install python-chess`
  - `pip install plotly`
  - `pip install pandas`

Run the webiste

- `python manage.py runserver`