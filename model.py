from flask import Flask
from flask_sqlalchemy import SQLAlchemy

zoneHeaders = [ (17,27),
                (22,23)]

db = SQLAlchemy()

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)
    label = db.Column(db.String(120), unique=False, nullable=False)
    toggle = db.Column(db.Boolean, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    pinL = db.Column(db.Integer, nullable=False)
    pinR = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Zone %r>' % self.key

    def insert(self):
        print("Inserting new Zone")
        print(self)
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def updateToggle(self,toggle):
        self.toggle = toggle
        db.session.commit()

    def updateLabel(self,label):
        if not label == '':
            self.label = label
            db.session.commit()

    def updateVolume(self,vol):
        if vol > -1 and vol < 101:
            self.volume = vol
            db.session.commit()    

    def format(self):
        return {
            'id': self.id,
            'key': self.key,
            'label': self.label,
            'toggle': self.toggle,
            'volume': self.volume,
            'pinL': self.pinL,
            'pinR': self.pinR
        }

def setup_db(app):
    print("Doing initial setup")
    db.app = app
    db.init_app(app)
    db.create_all()

def isInitial():
    rows = db.session.query(Zone).count()
    if rows > 0:
        print("DB is not initial")
        return False
    else:
        print("DB is initial")
        return True

def initializeZones(zoneCount):
    print("Initializing DB")
    print(zoneCount)
    if zoneCount > 0 and zoneCount < 3:
        print("zone creation")
        for i in range(zoneCount):
            print("creating another zone")
            #ASCII alphabet starts at 65 for A
            zoneCharI = i + 65
            zoneChar = chr(zoneCharI)
            zoneL = "Zone " + zoneChar
            zonePins = zoneHeaders[i]
            zone = Zone(key=zoneChar, label=zoneL, toggle=False, volume=0, pinL=zonePins[0], pinR=zonePins[1])
            zone.insert()