from flask import Flask, jsonify, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField, BooleanField
from wtforms.validators import DataRequired
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

API_KEY = "TopSecretAPIKey"

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)

class Form(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    map_url = StringField('map_url', validators=[DataRequired()])
    img_url = StringField('img_url', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    seats = StringField('seats', validators=[DataRequired()])
    has_toilet = BooleanField('has_toilet', validators=[DataRequired()])
    has_wifi = BooleanField('has_wifi', validators=[DataRequired()])
    has_sockets = BooleanField('has_sockets', validators=[DataRequired()])
    can_take_calls = BooleanField('can_take_calls', validators=[DataRequired()])
    coffee_price = BooleanField('coffee_price', validators=[DataRequired()])
    submit = SubmitField('submit')

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    


## HTTP GET - Read Record
@app.route('/all')
def get_all():
    with app.app_context():
        data = db.session.execute(db.select(Cafe)).scalars().all()
        new_data = [n.to_dict() for n in data]
        return jsonify(new_data)
    
@app.route('/search')
def search():
    location = request.args.get('loc')
    with app.app_context():
        data = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
        new_data = [n.to_dict() for n in data]
        if new_data:
            return jsonify(new_data)
        else:
            return jsonify({'error':{"Not Found": "sorry we dont have a cafe at that location"}})

@app.route('/random')
def get_random():
    with app.app_context():
        data = db.session.execute(db.select(Cafe)).scalars().all()
        item = random.choice(data).to_dict()
        # item = random.choice(data).__dict__
        # item.pop('_sa_instance_state', None)
    
    return jsonify(item)
    # return jsonify(cafe={
    #         "id": item.id,
    #         "name": item.name,
    #         "map_url": item.map_url,
    #         "img_url": item.img_url,
    #         "location": item.location,
    #         "seats": item.seats,
    #         "has_toilet": item.has_toilet,
    #         "has_wifi": item.has_wifi,
    #         "has_sockets": item.has_sockets,
    #         "can_take_calls": item.can_take_calls,
    #         "coffee_price": item.coffee_price,
    #         })


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({'success': "Successfully added new cafe"})
    
## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_price(id):
    new_price = request.args.get('new_price')
    with app.app_context():
        data = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
        if data is None:
            return jsonify({'error':{'Not Found': 'sorry a cafe with that id is not available in the database'}}), 404
        data.coffee_price = new_price
        db.session.commit()
    return jsonify({"success": 'price updated successfully'}), 200

## HTTP DELETE - Delete Record
@app.route('/report-closed/<int:id>', methods=['DELETE'])
def delete_cafe(id):
    new_price = request.args.get('api-key')
    if new_price != API_KEY:
        return jsonify({'error': 'that is not allowed. please provide a valid API key'}), 403
    with app.app_context():
        data = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
        if data is None:
            return jsonify({'error':{'Not Found': 'sorry a cafe with that id is not available in the database'}}), 404
        db.session.delete(data)
        db.session.commit()
    return jsonify({"success": 'cafe deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
