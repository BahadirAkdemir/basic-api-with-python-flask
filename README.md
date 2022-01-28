# basic-api-with-python-flask

This project contains a basic api which can do CRUD operations

To run, write "sh generate.sh" to the terminal

Or

Run those commands:


python3 -m venv .venv 
source .venv/bin/activate 
pip3 install flask   
pip3 install flask-sqlalchemy 
pip3 freeze > requirements.txt  
export FLASK_APP=application.py
export FLASK_ENV=development 
python3
from application import db
from application import Beverages
db.create_all()
exit()
flask run
