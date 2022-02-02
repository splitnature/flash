"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, CardSet, CardTable, Card
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from argon2 import PasswordHasher

ph = PasswordHasher()

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all() 
    response = []
    for user in users:
        response.append(user.serialize())

    return jsonify(response), 200  

@api.route('/CardSet', methods=['GET', 'POST'])
def get_CardSet():
    if request.method == "GET":

        card_sets = CardSet.query.all()
        response = []
        for card in card_sets:
            response.append(card.serialize())

        return jsonify(response), 200  
    else:     
        request_data = request.get_json()
        card = CardSet(
            name= request_data['name'], author= request_data["author"]
        )
        db.session.add(card)
        db.session.commit()
        return jsonify(card.serialize())


@api.route('/CardTable', methods=['GET', 'POST']) 
def get_CardTable():
    if request.method == 'GET':

        card_table = CardTable.query.all()
        response = []
        for table in card_table: 
            response.append(table.serialize())

        return jsonify(response), 200
    else: 
        request_data = request.get_json()
        table = CardTable(
            question = request_data['question'], 
            answer = request_data['answer'], 
            incorrect_answer1 = request_data['incorrect-answer1'],
            incorrect_answer2 = request_data['incorrect-answer2'],
            Incorrect_answer3 = request_data['incorrect-answer3'],
             card_tableID = request_data['CardTableID']
,
        )     
        db.session.add(table)
        db.session.commit()
        return jsonify(table.serialize())

@api.route('/card', methods=['POST', 'GET']) 
def get_card():
    if request.method == 'GET':

        card = Card.query.all()
        response = []
        for item in card:
            response.append(item.serialize())
        return jsonify(response), 200   
    else: 
        request_data = request.get_json()
        item = Card(
            description = request_data['description'],
            answer = request_data['answer'],
            deck = request_data['deck'],
            author = request_data['author']
        )    
        db.session.add(item)
        db.session.commit()
        return jsonify(Card.commit())

@api.route('/hello', methods=['POST', 'GET'])
@jwt_required()
def handle_hello():
    current_user_id = get_jwt_identity()

    user = User.query.filter(User.id == current_user_id).first()

    response_body = {
        "message": f"Hello I Am {user.email}"        
    }
    return jsonify(response_body), 200


@api.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()

    # Check if User exists
    if User.query.filter(User.email == data['email']).count() > 0:
        return 'user-exists', 400

    # Create the User
    user = User(
        email=data['email'], 
        password=ph.hash(data['password']), 
        is_active=True
    )
    db.session.add(user)
    db.session.commit()

    return '', 204


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter(User.email == data['email']).first()
    if user is None:
        return '', 404
    
    try:
        ph.verify(user.password, data['password'])
    except: 
        return 'wrong-password', 400

    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

