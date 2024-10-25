from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    current_time = datetime.now()
    greeting = "Good Morning!" if current_time.hour < 12 else "Good Afternoon!" if current_time.hour < 18 else "Good Evening!"
    
    sellers = [
        {"name": "Seller 1", "image": "BUYERS/IMAGE 1.jpeg"},
        {"name": "Seller 2", "image": "BUYERS/IMAGE 2.jpeg"},
        {"name": "Seller 3", "image": "BUYERS/IMAGE 3.jpeg"},
        {"name": "Seller 4", "image": "BUYERS/IMAGE4.webp"},
    ]
    
    buyers = [
        {"name": "Buyer 1", "image": "SELLERS/IMAGE1.jpeg"},
        {"name": "Buyer 1", "image": "SELLERS/IMAGE2.webp"},
        {"name": "Buyer 2", "image": "SELLERS/IMAGE3.jpeg"},
        {"name": "Buyer 3", "image": "SELLERS/IMAGE4.webp"},
    ]

    return render_template('index.html', greeting=greeting, sellers=sellers, buyers=buyers, user = current_user)




    # if request.method == 'POST': 
    #     note = request.form.get('note')#Gets the note from the HTML 

    #     if len(note) < 1:
    #         flash('Note is too short!', category='error') 
    #     else:
    #         new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
    #         db.session.add(new_note) #adding the note to the database 
    #         db.session.commit()
    #         flash('Note added!', category='success')

    # return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/')
def index():
    current_time = datetime.now()
    greeting = "Good Morning!" if current_time.hour < 12 else "Good Afternoon!" if current_time.hour < 18 else "Good Evening!"
    
    sellers = [
        {"name": "Seller 1", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/BUYERS/IMAGE 1.jpeg"},
        {"name": "Seller 2", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/BUYERS/IMAGE 2.jpeg"},
        {"name": "Seller 3", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/BUYERS/IMAGE 3.jpeg"},
    ]
    
    buyers = [
        {"name": "Buyer 1", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/SELLERS/ACHERON.jpg"},
        {"name": "Buyer 2", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/SELLERS/JINGLIU.jpg"},
        {"name": "Buyer 3", "image": "C:/Users/bhara/Desktop/Flask-Web-App-Tutorial-main/website/templates/SELLERS/TINGYUN 2.jpg"},
    ]

    return render_template('index.html', greeting=greeting, sellers=sellers, buyers=buyers)


