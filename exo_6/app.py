from flask import Flask, render_template, request, redirect
# conda install -c conda-forge mysql-connector-python
import mysql.connector as mariadb

# Configuration pour la connection mysql
config = {
    'user': 'cedric',
    'password': 'root',
    'host': 'localhost',
    'database': 'flask_tuto'
}

# Instanciation Flask
app = Flask(__name__)
app.debug = True

# Routeur
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/alerte')
def refused():
    return render_template("erreur.html")

@app.route('/confirmation')
def accepted():
    return render_template("confirmation.html")

@app.route('/liste')
def liste():
    mariadb_connection = mariadb.connect(**config)
    cursor = mariadb_connection.cursor()
    query = "SELECT * FROM user"
    cursor.execute(query)
    list_user = []
    for registered_user in cursor:   
        list_user.append([registered_user[0],registered_user[1],registered_user[3]])
    return render_template("liste.html", liste = list_user)

@app.route('/formulaire')
def formulaire():
    return render_template("formulaire.html")

@app.route('/formulaire', methods=['POST'])
def text_box():
    lastname = request.form['lastname']
    firstname = request.form['firstname']
    sex = request.form['sex']
    pseudo = request.form['pseudo']

    mariadb_connection = mariadb.connect(**config)
    cursor = mariadb_connection.cursor()

    # Test si le pseudo existe déja
    query = "SELECT pseudo FROM user"
    cursor.execute(query)
    list_pseudo = []

    for registered_pseudo in cursor:   
        list_pseudo.append(registered_pseudo[0])

    if pseudo in list_pseudo:
        return redirect("/erreur")
    else:
        add_user = ("INSERT INTO user "
                    "(prenom,nom,sexe,pseudo) "
                    "VALUES (%s,%s,%s,%s)")
        data_user = (firstname,lastname,sex,pseudo)
        cursor.execute(add_user,data_user)
        mariadb_connection.commit()

        return redirect("/confirmation")

    # Fermeture de la connection
    mariadb_connection.close()

if __name__ == '__main__':
    app.run()