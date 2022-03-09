from flask import Flask, render_template, url_for, redirect, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

import frame
import coordonnees_rect
import On_off

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')


# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    frame.photo()
    coordonnees_rect.coordonne()
    On_off.On_off()

    return render_template('dashboard.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')


@app.route('/select_objet', methods=['GET', 'POST'])
def select_objet():
    if request.method == 'POST':
        objet_1 = request.form['objet_1']
        objet_2 = request.form['objet_2']
        objet_3 = request.form['objet_3']
        objet_4 = request.form['objet_4']
        objet_5 = request.form['objet_5']
        objet_6 = request.form['objet_6']

        print('objet n°1:', objet_1)
        session['objet_1'] = objet_1
        print('objet n°2:', objet_2)
        session['objet_2'] = objet_2
        print('objet n°3:', objet_3)
        session['objet_3'] = objet_3
        print('objet n°4:', objet_4)
        session['objet_4'] = objet_4
        print('objet n°5:', objet_5)
        session['objet_5'] = objet_5
        print('objet n°6:', objet_6)
        session['objet_6'] = objet_6

        # Ecriture dans le fichier
        fichier_obj1 = open("objet_1.txt", "w")
        fichier_obj1.write(objet_1)
        fichier_obj1.close()

        fichier_obj2 = open("objet_2.txt", "w")
        fichier_obj2.write(objet_2)
        fichier_obj2.close()

        fichier_obj3 = open("objet_3.txt", "w")
        fichier_obj3.write(objet_3)
        fichier_obj3.close()

        fichier_obj4 = open("objet_4.txt", "w")
        fichier_obj4.write(objet_4)
        fichier_obj4.close()

        fichier_obj5 = open("objet_5.txt", "w")
        fichier_obj5.write(objet_5)
        fichier_obj5.close()

        fichier_obj6 = open("objet_6.txt", "w")
        fichier_obj6.write(objet_6)
        fichier_obj6.close()

        return render_template('dashboard.html', username=session['username'], objet_1=session['objet_1'],
                               objet_2=session['objet_2'], objet_3=session['objet_3'], objet_4=session['objet_4'],
                               objet_5=session['objet_5'], objet_6=session['objet_6'])
    else:
        return render_template('dashboard.html', username=session['username'], objet_1=session['objet_1'],
                               objet_2=session['objet_2'], objet_3=session['objet_3'], objet_4=session['objet_4'],
                               objet_5=session['objet_5'], objet_6=session['objet_6'])


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', objet_1=session['objet_1'], objet_2=session['objet_2'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('username:', username, 'password:', password)

        pwhash = generate_password_hash(password)
        pierre_pwhash = generate_password_hash('pierre')
        print('pwhash:', pwhash)
        if username == 'pierre' and check_password_hash(pierre_pwhash, password):
            session['username'] = username
            session['objet_1'] = 'Aucun'
            session['objet_2'] = 'Aucun'
            return render_template('profil.html', username=session['username'], objet_1=session['objet_1'],
                                   objet_2=session['objet_2'])

        else:
            flash('Accès refusé', 'danger')
            return render_template('index.html')

    else:
        return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Vous avez été correctement déconnecté', 'success')
    return redirect(url_for('index'))

# @app.route('/register/', methods=['POST'])
# def register():
#    result = request.form
#    username = result['reg_username1']
#    password = result['reg_password1']
#    pl = Prise_l['null']
#    pr = Prise_r['null']

#    return render_template('register.html', username=username, password=password, prise_l=pl, prise_r=pr)

#    app.run(debug=True)
