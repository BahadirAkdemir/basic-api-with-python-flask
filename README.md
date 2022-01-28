# basic-api-with-python-flask

This project contains a basic api which can do CRUD operations

To run, write "sh generate.sh" to the terminal

Or

Run those commands:


python3 -m venv .venv <br>
source .venv/bin/activate <br>
pip3 install flask   <br>
pip3 install flask-sqlalchemy<br> 
pip3 freeze > requirements.txt  <br>
export FLASK_APP=application.py<br>
export FLASK_ENV=development <br>
python3<br>
from application import db <br>
from application import Beverages<br>
db.create_all()<br>
exit()<br>
flask run<br>
