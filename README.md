# CMSC-495

UMGC Captsone project for software engineering degree, built by @jtkaufman737 @montyhack365 and @HAND0FCTHULU for the Fall 2021 semester 

# Project Description 

This project aims to provide a trello-like interface for [fault tree analysis](https://en.wikipedia.org/wiki/Fault_tree_analysis), a means of describing system behavior and failures for engineering teams. 

# Project Setup and Dependencies 

**Quick Note**: Unfortunately, I _do not have a Windows machine to practice on_ so these instructions are specific to flavors of Linux. I tried looking at how to do it with Docker, but even that runs into limitations without me giving someone a lot of complicated UI instructions since apparently windows cmd is not the normal way people interface with Docker on that OS. Long story short, I tried but for now *nix it is. 

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
export FLASK_APP=main       # tells Flask to use our app.py file 
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

Download a local version of MySQL for your system. Using `root` user set a password `mysqluser`. From the command line run `sudo mysql -p` and then enter first your **system** password and then the **db password**, `mysqluser`. From there you are in the SQL shell and can run `CREATE DATABASE fault_tree;`. You will need to do that BEFORE running `flask run` which will launch the db building script. 

*Note - this is a temporary local database setup until we get on AWS, to facilitate development of endpoints* 

# Future Improvements 

TBD 