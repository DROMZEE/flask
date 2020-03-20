from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  s = result['sexe']
  ps = result['pseudo']
  return render_template("resultat.html", nom=n, prenom=p, sexe=s, pseudo = ps)

app.run(debug=True)