from . import app
from flask import request, session, redirect, url_for, abort, render_template
from .models import db, Talk, User, Person
import hashlib

# Questa piccola funzione cripta le password.
def hash_password(password):
   hash_object = hashlib.sha256(password.encode('utf-8'))
   return hash_object.hexdigest()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/contributions')
def contributions():
    return render_template('contributions.html')

@app.route('/talks')
def talks():
    talks = Talk.query.all()
    return render_template('talks.html', talks=talks)

@app.route('/talks/<int:talk_id>')
def talkdetails(talk_id):
    talk = Talk.query.get(talk_id)
    return render_template('talkdetails.html', talk=talk)

@app.route('/conferencephoto')
def photo():
    return render_template('conferencephoto.html')

@app.route('/listofparticipants')
def list():
    person = Person.query.all()
    return render_template('listofparticipants.html', person=person)

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Dovrei controllare che l'utente esista.
    utente = User.query.filter_by(username=request.form['username']).first()
    # Controllo la password.
    if request.form['password'] == utente.password:
      session['username'] = request.form['username']
    else:
      abort(403)
    return redirect(url_for('index'))
  return render_template('login.html')

  
@app.route('/logout')
def logout():
  # Tolgo "username" dalla sessione.
  session.pop('username', None)
  return redirect(url_for('index'))

@app.route('/crea-utente', methods=['GET', 'POST'])
def crea_utente():
    # Se non sono loggato come 'admin' esco con codice 401.
    if 'username' not in session or session['username'] != 'Admin':
      abort(401)
    if request.method == 'POST':
      u = request.form['username']
      p = request.form['password']
      utente = User(username=u, password=p)
      # Qui potrei controllare se l'utente già esiste.
      db.session.add(utente)
      db.session.commit()
      return redirect(url_for('index'))
    return render_template('crea.html')


# disponibili = {
#   'A111': 100,
# }

@app.route('/trip')
def trip():
  max_participants = 25
  participants = User.query.filter_by(trip = 1).all()
  return render_template('trip.html', participants=participants, max_participants = max_participants)

@app.route('/jointrip')
def jointrip():
    if 'username' not in session:
       abort(403) 
    participant = User.query.filter_by(username=session['username']).first()
    participant.trip = 1
    #added = User.query.filter_by(trip = 0).all()
    db.session.add(participant)
    db.session.commit()
    return redirect('/trip')

