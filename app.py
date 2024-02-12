from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm  
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
load_dotenv()
import os


app = Flask(__name__)

# Définir une clé secrète pour la protection CSRF
app.config['SECRET_KEY'] = os.urandom(24)

# Initialiser la protection CSRF
csrf = CSRFProtect(app)

# Sécurisation des cookies de session
app.config['SESSION_COOKIE_SECURE'] = True

# Connexion à la bd
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifiant = db.Column(db.String(1000), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(1000), nullable=False)

with app.app_context():
    db.create_all()

# Définition du formulaire WTForms pour le login
class LoginForm(FlaskForm):
    identifiant = StringField('Identifiant', validators=[InputRequired(), Length(min=3, max=50)])
    mot_de_passe = PasswordField('Mot de passe', validators=[InputRequired(), Length(min=8)])
    submit = SubmitField('Connexion')

@app.route('/')
def accueil():
    form = LoginForm()  # Créer une instance du formulaire
    return render_template('formulaire.html', form=form)  # Passer le formulaire au template

@app.route('/traitement', methods=['POST'])
def traitement():
    identifiant_saisi = request.form['identifiant']
    mot_de_passe_saisi = request.form['mot_de_passe']

    # Validation des données saisies
    if len(identifiant_saisi) < 3 or len(identifiant_saisi) > 50:
        return "Identifiant invalide. Veuillez saisir un identifiant entre 3 et 50 caractères."

    if len(mot_de_passe_saisi) < 8:
        return "Mot de passe invalide. Veuillez saisir un mot de passe d'au moins 8 caractères."

    # requête paramétrée
    utilisateur = Utilisateur.query.filter_by(identifiant=identifiant_saisi).first()

    if utilisateur and check_password_hash(utilisateur.mot_de_passe, mot_de_passe_saisi):
        return "Connexion réussie!"
    else:
        return "Identifiant ou mot de passe incorrect."

@app.route('/ajouter_compte', methods=['POST'])
def ajouter_compte():
    if request.method == 'POST':
        nouvel_identifiant = request.form['nouvel_identifiant']
        nouveau_mot_de_passe = request.form['nouveau_mot_de_passe']

        # Validation des données saisies
        if len(nouvel_identifiant) < 3 or len(nouvel_identifiant) > 50:
            return "Identifiant invalide. Veuillez saisir un identifiant entre 3 et 50 caractères."

        if len(nouveau_mot_de_passe) < 8:
            return "Mot de passe invalide. Veuillez saisir un mot de passe d'au moins 8 caractères."

        # Vérifier si l'identifiant existe déjà
        if Utilisateur.query.filter_by(identifiant=nouvel_identifiant).first():
            return "Cet identifiant existe déjà."

        # Créer un nouvel utilisateur
        nouvel_utilisateur = Utilisateur(identifiant=nouvel_identifiant, mot_de_passe=generate_password_hash(nouveau_mot_de_passe))
        db.session.add(nouvel_utilisateur)
        db.session.commit()

        return "Compte ajouté avec succès!"
    else:
        return "Erreur"

if __name__ == '__main__':
    # certificat SSL (pour test local uniquement)
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=False)

