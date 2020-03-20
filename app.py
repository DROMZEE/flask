from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/confirmation')
def confirmation() :
    return render_template('confirmation.html')

@app.route('/test-formulaire')
def formulaire() :
    return render_template('formulaire.html')

@app.route('/test-formulaire', methods=['POST'])
def test_form():
    prenom = request.form['prenom']
    processed_text = prenom.upper()
    #nom = request.form['nom']
    #sexe = request.form['sexe']
    #pseudo = request.form['pseudo']
    #form_list = [['prenom',prenom],['nom',nom],['sexe',sexe], ['pseudo', pseudo]]
    #return render_template('confirmation.html', prenom=processed_text)
    return render_template("confirmation.html", message=processed_text)
    #return render_template("confirmation.html", form_list=form_list)
    #return render_template("confirmation.html", prenom=prenom, nom=nom, sexe=sexe, pseudo=pseudo)

if __name__ == '__main__':
    app.run(debug=True)