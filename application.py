from flask import  Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db=SQLAlchemy(app)


class Beverages(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    description=db.Column(db.String(200))

    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')

def index():
    return '<h1>Hello World!</h1>'

@app.route('/beverages')

def get_beverages():
    beverages=Beverages.query.all()
    output=[]
    for beverage in beverages:
        beverage_data={'name':beverage.name,'description':beverage.description}
        output.append(beverage_data)
    return {"beverages": output}

@app.route('/beverages/<int:id>')
def get_beverage(id):
    beverage=Beverages.query.get_or_404(id)
    return {"name": beverage.name,"description": beverage.description}



@app.route('/beverages/<id>', methods=['DELETE'])
def delete_beverage(id):
    beverage = Beverages.query.get(id)
    if beverage is None:
        return {"error":"Not Found"}
    else:
        db.session.delete(beverage)
        db.session.commit()
        return {"Message":"Deleted Succesfully!"}


@app.route('/beverages', methods=['POST'])
def add_beverage():
    data=request.get_json(force=True)
    beverage = Beverages(name=data['name'],description=data['description'])
    db.session.add(beverage)
    db.session.commit()
    return{"id":beverage.id}

@app.route('/beverages', methods=['PUT'])
def adjust_beverage():
    data=request.get_json(force=True)
    beverage = Beverages.query.get(data['id'])
    
    if beverage is None:
        return {"error":"Not Found"}
    else:
        beverage.name=data['name']
        beverage.description=data['description']
        db.session.commit()
        return {"Message":"Adjusted Succesfully!"}
