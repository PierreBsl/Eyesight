from flask import Flask, render_template, url_for, redirect, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import os
import psycopg2
import time

import frame
import coordonnees_rect
import On_off
import visage

ip1 = '10.30.50.174'  # Modifier ici l'adresse ip de la camera IP
ip2 = '10.30.50.180'  # Modifier ici l'adresse ip de la camera IP
app = Flask(__name__)
run=True
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')


# Configurtion for database

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_eyesight',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


def application():
    if ip1 != '' and ip2 != '':
        if visage.detection(frame.grab_frame2()) or visage.detection(
                frame.grab_frame('http://' + ip1 + '/axis-cgi/jpg/image.cgi')) or visage.detection(
            frame.grab_frame('http://' + ip2 + '/axis-cgi/jpg/image.cgi')):
            print('visage:ok')
            frame.photo()
            coordonnees_rect.coordonne()
            On_off.On_off()
            print('ok trame')
            return render_template('dashboard.html')
        else:
            print('pas de visage')
    else:
        if visage.detection(frame.grab_frame2()):
            print('visage: ok')
            frame.photo()
            coordonnees_rect.coordonne()
            On_off.On_off()
            return render_template('dashboard.html')
        else:
            print('pas de visage')
    return render_template('dashboard.html')

def chg_prise():
    file = open('etat.txt', 'r')
    char = file.read()
    if char[0] == '0':
        session['A1'] = '<i class="bi bi-plugin"></i>'
    else:
        session['A1'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[1] == '0':
        session['A2'] = '<i class="bi bi-plugin"></i>'
    else:
        session['A2'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[2] == '0':
        session['A3'] = '<i class="bi bi-plugin"></i>'
    else:
        session['A3'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[3] == '0':
        session['B1'] = '<i class="bi bi-plugin"></i>'
    else:
        session['B1'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[4] == '0':
        session['B2'] = '<i class="bi bi-plugin"></i>'
    else:
        session['B2'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[5] == '0':
        session['B3'] = '<i class="bi bi-plugin"></i>'
    else:
        session['B3'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[6] == '0':
        session['C1'] = '<i class="bi bi-plugin"></i>'
    else:
        session['C1'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[7] == '0':
        session['C2'] = '<i class="bi bi-plugin"></i>'
    else:
        session['C2'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[8] == '0':
        session['C3'] = '<i class="bi bi-plugin"></i>'
    else:
        session['C3'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[9] == '0':
        session['D1'] = '<i class="bi bi-plugin"></i>'
    else:
        session['D1'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[10] == '0':
        session['D2'] = '<i class="bi bi-plugin"></i>'
    else:
        session['D2'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    if char[11] == '0':
        session['D3'] = '<i class="bi bi-plugin"></i>'
    else:
        session['D3'] = '<i class="bi bi-plugin" style="color: green;"></i>'
    
    file.close()
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main():
    chg_prise()
    application()
    return render_template('dashboard.html')
        
    
        

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/stop')
def stop():
    global run
    run=False
    flash('Application Stopped', 'success')
    return render_template('dashboard.html')


@app.route('/select_objet', methods=['GET', 'POST'])
def select_objet():
    if request.method == 'POST':
        objet_1 = request.form['objet_1']
        objet_2 = request.form['objet_2']
        objet_3 = request.form['objet_3']
        objet_4 = request.form['objet_4']
        objet_5 = request.form['objet_5']
        objet_6 = request.form['objet_6']

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
        
        print('objet n°1:', objet_1)
        print('objet n°2:', objet_2)
        print('objet n°3:', objet_3)
        print('objet n°4:', objet_4)
        print('objet n°5:', objet_5)
        print('objet n°6:', objet_6)
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE objects	SET objet_1 = '" + objet_1 + "', objet_2 = '" + objet_2 + "', objet_3 = '" + objet_3 + "', objet_4 = '" + objet_4 + "', objet_5 = '" + objet_5 + "', objet_6 = '" + objet_6 + "' WHERE user_id = '" + str(
                session['user_id']) + "';")
                
        conn.commit()                
        
        session['objet_1'] = objet_1
        session['objet_2'] = objet_2
        session['objet_3'] = objet_3
        session['objet_4'] = objet_4
        session['objet_5'] = objet_5
        session['objet_6'] = objet_6

        return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')


@app.route('/dashboard')
def dashboard():
    chg_prise()
    return render_template('dashboard.html')
    
    
@app.route('/admin')
def admin():
    global run
    run=False
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ;")
    res = cur.fetchall()

    fichier = open("table.txt", "w")
    fichier.write('<table class="table"><thead><tr><th scope="col">#</th><th scope="col">Username</th></tr></thead><tbody>')

    for raw in res:
        fichier.write('<tr>')
        fichier.write('<th id="admin" scope="row">'+str(raw[0])+'</th>')
        fichier.write('<td>'+ raw[1]+'</td>')
        fichier.write('<td><form method="POST" action="/deleteUser"><button style="float: right" name="Delete" value="'+str(raw[0])+'" type="submit" class="btn btn-danger">Delete</button></form></td>')
        fichier.write('</tr>')

    fichier.write('</tbody>')
    fichier.write('</table>')
    fichier.close()

    file = open("table.txt", "r")
    table = file.read()
    print (table)
    return render_template('admin.html', table=table)

@app.route('/deleteUser', methods=['GET','POST'])
def deleteUser():
    if request.method == 'POST':
        value = request.form.get("Delete")
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM objects WHERE user_id = '"+str(value)+"';")
        cur.execute("DELETE FROM users WHERE userid = '"+str(value)+"';")
        conn.commit()
        cur.close()
        conn.close()
        
        return redirect(url_for('admin'))
    else:
        return render_template('admin.html')
        
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usname = request.form['username']
        paword = request.form['password']
        # pwhash = generate_password_hash(paword)
        pierre_pwhash = generate_password_hash('pierre')
        # print(pwhash)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = '" + usname + "';")
        val = cur.fetchone()[0]

        if check_password_hash(val, paword):
            cur.execute("SELECT userid FROM users WHERE username = '" + usname + "';")
            usid = cur.fetchone()[0]
            cur.execute("SELECT objet_1 FROM objects WHERE user_id = '" + str(usid) + "';")
            o1 = cur.fetchone()[0]
            cur.execute("SELECT objet_2 FROM objects WHERE user_id = '" + str(usid) + "';")
            o2 = cur.fetchone()[0]
            cur.execute("SELECT objet_3 FROM objects WHERE user_id = '" + str(usid) + "';")
            o3 = cur.fetchone()[0]
            cur.execute("SELECT objet_4 FROM objects WHERE user_id = '" + str(usid) + "';")
            o4 = cur.fetchone()[0]
            cur.execute("SELECT objet_5 FROM objects WHERE user_id = '" + str(usid) + "';")
            o5 = cur.fetchone()[0]
            cur.execute("SELECT objet_6 FROM objects WHERE user_id = '" + str(usid) + "';")
            o6 = cur.fetchone()[0]
            session['user_id'] = usid
            session['username'] = usname
            session['objet_1'] = o1
            session['objet_2'] = o2
            session['objet_3'] = o3
            session['objet_4'] = o4
            session['objet_5'] = o5
            session['objet_6'] = o6
            return render_template('profil.html')

        else:
            flash('Accès refusé', 'danger')
            return render_template('index.html')

    else:
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print('register')
    if request.method == 'POST':
        print('post')
        uname = request.form['reg_username1']
        pword = request.form['reg_password1']
        conf_password = request.form['reg_password_confirm1']

        if pword == conf_password:
            print('pword==conf_password')
            pwhash = generate_password_hash(pword)

            conn = get_db_connection()
            print('conn')
            cur = conn.cursor()
            print('cursor')
            cur.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (uname, pwhash))

            cur.execute("SELECT userid FROM users WHERE username = '" + uname + "';")
            uid = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO objects (objet_1, objet_2, objet_3, objet_4, objet_5, objet_6,	user_id) VALUES ('Aucun', 'Aucun', 'Aucun', 'Aucun', 'Aucun', 'Aucun', '" + str(
                    uid) + "');")

            cur.execute("SELECT objet_1 FROM objects WHERE user_id = '" + str(uid) + "';")
            o1 = cur.fetchone()[0]
            cur.execute("SELECT objet_2 FROM objects WHERE user_id = '" + str(uid) + "';")
            o2 = cur.fetchone()[0]
            cur.execute("SELECT objet_3 FROM objects WHERE user_id = '" + str(uid) + "';")
            o3 = cur.fetchone()[0]
            cur.execute("SELECT objet_4 FROM objects WHERE user_id = '" + str(uid) + "';")
            o4 = cur.fetchone()[0]
            cur.execute("SELECT objet_5 FROM objects WHERE user_id = '" + str(uid) + "';")
            o5 = cur.fetchone()[0]
            cur.execute("SELECT objet_6 FROM objects WHERE user_id = '" + str(uid) + "';")
            o6 = cur.fetchone()[0]

            conn.commit()
            cur.close()
            conn.close()
            print('close')
            session['username'] = uname
            session['objet_1'] = o1
            session['objet_2'] = o2
            session['objet_3'] = o3
            session['objet_4'] = o4
            session['objet_5'] = o5
            session['objet_6'] = o6

            flash('Votre compte a bien été crée', 'success')
            return redirect(url_for('index'))
        else:
            flash('Les mots de passes sont différents', 'danger')
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/contact')
def contact():
    global run
    run=False
    return render_template('contact.html')


@app.route('/calendar')
def calendar():
    global run
    run=False
    return render_template('calendar.html')


@app.route('/logout')
def logout():
    global run
    run=False
    session.clear()
    flash('Vous avez été correctement déconnecté', 'success')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0:5000", debug=True)
