from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    first_name =  db.Column(db.String(), unique=False, nullable=False)
    last_name = db.Column(db.String(), unique=False, nullable=False)
    username = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name
            # do not serialize the password, its a security breach
        }

class CardSet(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 
    author = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "author": self.author
        }    

class CardTable(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    question = db.Column(db.String, unique=False, nullable=False)
    answer = db.Column(db.String, unique=False, nullable=False)
    incorrect_answer1 = db.Column(db.String, unique=False, nullable=False)
    incorrect_answer2 = db.Column(db.String, unique=False, nullable=False)
    Incorrect_answer3 = db.Column(db.String, unique=False, nullable=False)
    card_tableID = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return self.card_tableID

    def serialize(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "incorrect answer 1": self.incorrect_answer1,
            "incorrect answer 2": self.incorrect_answer2,
            "incorrect answer 3": self.Incorrect_answer3,
            "cardset Id": self.card_tableID
        }    

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, unique=False, nullable=False)
    deck = db.Column(db.String, unique=False, nullable=False)
    author = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return self.Card 

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "answer": self.answer,
            "deck": self.deck,
            "author": self.author
        }    
