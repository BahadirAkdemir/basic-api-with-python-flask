#!/bin/bash
python3 -m venv .venv 
source .venv/bin/activate 
pip3 install flask   
pip3 install flask-sqlalchemy 
pip3 freeze > requirements.txt  
export FLASK_APP=application.py
export FLASK_ENV=development 
python3 init.py
flask run
