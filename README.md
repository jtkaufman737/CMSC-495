# CMSC-495

UMGC Captsone project for software engineering degree, built by @jtkaufman737 @montyhack365 and @HAND0FCTHULU for the Fall 2021 semester 

# Project Description 

This project aims to provide a trello-like interface for [fault tree analysis](https://en.wikipedia.org/wiki/Fault_tree_analysis), a means of describing system behavior and failures for engineering teams. 

# Project Setup and Dependencies 

## Backend 

For *nix systems you should already have python installed. You can confirm by running `python3 --version`. If you do not have python3 you will need to [install it](https://www.python.org/downloads/).

You will also need the Python package manager, pip. You can run `pip --version` from the command line, and if needed install it [here](https://pip.pypa.io/en/stable/installation/).

Once you have python installed, from the project directory run the following steps.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
The lines above takes care of installing all the python libraries needed to run our web server. "venv" is a virtual environment for those dependencies to be installed so that they won't conflict with anything else on your system. 

Next, we are going to follow the Flask quickstart guide to run a minimal web server.
```
export FLASK_APP=app       # tells Flask to use our app.py file 
python -m flask            
flask run                  # will run a local server at localhost:5000 
```

From there, you can see the local code by directing a browser to localhost:5000. This is what you will use to locally develop endpoint logic. 

## Frontend 

To install node dependencies and run the user interface dev server, enter the ui folder and run the following commands. 
```
cd ui
npm install 
npm run serve
```

## Test db 

Download a local version of MySQL for your system. Using `root` user set a password `mysqluser`. From the command line as root user, run `CREATE DATABASE fault_tree;`

# Future Improvements 

TBD 