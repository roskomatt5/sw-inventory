from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Drink, drink_schema, drinks_schema

api = Blueprint('api',__name__, url_prefix='/api')


@api.route('/drinks', methods = ['POST'])
@token_required
def create_drink(current_user_token):
    brand = request.json['brand']
    flavor = request.json['flavor']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    drink = Drink(brand,flavor,user_token=user_token) 
    
    db.session.add(drink)
    db.session.commit()

    response = drink_schema.dump(drink)
    return jsonify(response)


@api.route('/drinks', methods = ['GET'])
@token_required
def get_drink(current_user_token):
    a_user = current_user_token.token
    drink = Drink.query.filter_by(user_token = a_user).all()
    response = drinks_schema.dump(drink)
    return jsonify(response)

@api.route('/drinks/<id>', methods = ['GET'])
@token_required
def get_single_drink(current_user_token, id):
    owner = current_user_token.token
    drink = Drink.query.get(id)
    response = drink_schema.dump(drink)
    return jsonify(response)


@api.route('/drinks/<id>', methods = ['POST','PUT'])
@token_required
def update_drink(current_user_token, id):
    drink = Drink.query.get(id)
    drink.brand = request.json['brand']
    drink.flavor = request.json['flavor']
    drink.user_token = current_user_token.token

    db.session.commit()
    response = drink_schema.dump(drink)
    return jsonify(response)

@api.route('/drinks/<id>', methods = ['DELETE'])
@token_required
def drink(current_user_token, id):
    drink = Drink.query.get(id)
    db.session.delete(drink)
    db.session.commit()
    response = drink_schema.dump(drink)
    return jsonify(response)