from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['username']
    processed_text = text.upper()
    return render_template("bienvenue.html", message=processed_text)

@app.route('/test-formulaire')
def formulaire() :
    return render_template('formulaire.html')

@app.route('/test-formulaire', methods=['POST'])
def test_form() :
    prenom = request.form['prenom']
    nom = request.form['nom']
    sexe = request.form['sexe']
    pseudo = request.form['pseudo']
    return render_template("confirmation.html", prenom=prenom, nom=nom, sexe=sexe, pseudo=pseudo)

if __name__ == '__main__':
    app.run()