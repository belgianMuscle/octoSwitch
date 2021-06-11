import os
import babel
from flask import Flask, request, Response, abort, jsonify, render_template, flash, redirect
from core import OctoRelay
from model import setup_db, isInitial, initializeZones

app = Flask(__name__)
'''app.config.from.object('config')'''
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/data/octo.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '645aswe98asd65'
octorelay = None

@app.route('/')
def index():

    pageData = {
        'zoneALabel':octorelay.getLabel('A'),
        'zoneBLabel':octorelay.getLabel('B'),
        'zoneAToggle':octorelay.getToggle('A'),
        'zoneBToggle':octorelay.getToggle('B'),
        'zoneAVolume':octorelay.getVolume('A'),
        'zoneBVolume':octorelay.getVolume('B')
    }

    print(pageData)

    return render_template('pages/index.html',data=pageData)

@app.route('/toggle',methods=['POST'])
def updateToggle():
    data = request.get_json()

    print(data)

    octorelay.setZoneToggle('A',data['zoneAToggle'])
    octorelay.setZoneToggle('B',data['zoneBToggle'])

    response = {
        'zoneALabel':octorelay.getLabel('A'),
        'zoneBLabel':octorelay.getLabel('B'),
        'zoneAToggle':octorelay.getToggle('A'),
        'zoneBToggle':octorelay.getToggle('B'),
        'zoneAVolume':octorelay.getVolume('A'),
        'zoneBVolume':octorelay.getVolume('B')
    }
    print(response)
    return render_template('pages/index.html',data=response)

@app.route('/volume',methods=['POST'])
def updateVolume():
    data = request.get_json()

    print(data)

    octorelay.setZoneVolume('A',data['zoneAVolume'])
    octorelay.setZoneVolume('B',data['zoneBVolume'])

    response = {
        'zoneALabel':octorelay.getLabel('A'),
        'zoneBLabel':octorelay.getLabel('B'),
        'zoneAToggle':octorelay.getToggle('A'),
        'zoneBToggle':octorelay.getToggle('B'),
        'zoneAVolume':octorelay.getVolume('A'),
        'zoneBVolume':octorelay.getVolume('B')
    }
    print(response)
    return render_template('pages/index.html',data=response)

@app.route('/label',methods=['POST'])
def updateLabel():
    data = request.get_json()
    print("Receiving data")
    print(data)

    octorelay.setZoneLabel('A',data['zoneALabel'])
    octorelay.setZoneLabel('B',data['zoneBLabel'])

    response = {
        'zoneALabel':octorelay.getLabel('A'),
        'zoneBLabel':octorelay.getLabel('B'),
        'zoneAToggle':octorelay.getToggle('A'),
        'zoneBToggle':octorelay.getToggle('B'),
        'zoneAVolume':octorelay.getVolume('A'),
        'zoneBVolume':octorelay.getVolume('B')
    }
    print("Response data")
    print(response)
    return render_template('pages/index.html',data=response)

@app.route('/how')
def about():
    return render_template('pages/how.html')

# Default port:
'''
if __name__ == '__main__':
    app.run()
'''

# Or specify port manually:
if __name__ == '__main__':

    setup_db(app)
    if isInitial():
        initializeZones(2)
    
    octorelay = OctoRelay()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)