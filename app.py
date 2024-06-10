from flask import Flask, jsonify, request, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

brugere = {
    "alice": "test",
    "Bob": "password2",
    "Charlie": "password3",
    "David": "password4",
    "Erika": "password5"
}

hvor_mange_rum = ["Køkken", "Stue", "Soveværelse", "Badeværelse", "Gang", "Kontor", "Børneværelse", "Kælder"]


def strøm_af_lamper(rum_info, hvor_mange_rum, brugere, watt, volt):
    return hvor_mange_rum, {room: watt * volt for room in hvor_mange_rum}

def check_temperature(manueltsat_temperatur):
    return 10, {room: manueltsat_temperatur for room in hvor_mange_rum}

@app.route('/lights', methods=['GET'])
def lights_status():
    _, forbrugs_info = strøm_af_lamper(None, hvor_mange_rum, brugere, 60, 230)
    return jsonify({"rooms": {room: {"power": power} for room, power in forbrugs_info.items()}})

@app.route('/temperature', methods=['GET'])
def get_temperature():
    selvvalgt_temperatur = int(request.args.get('manueltsat_temperatur', 15))
    udendørs_temperatur, rum_temperaturer = check_temperature(selvvalgt_temperatur)
    return jsonify({"udendørs_temperatur": udendørs_temperatur, "rum_temperatures": rum_temperaturer})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in brugere and brugere[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Brugernavn eller adgangskode er forkert.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
@app.route('/grundplan')
def grundplan():

        return render_template('index.html' )
    
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('hjem.html', username=username)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
