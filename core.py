import importlib.util
from time import sleep 
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from model import db, Zone

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    import FakeRPi.GPIO as GPIO


class OctoRelay():

    def __init__(self):
        print('OctoRelay Init')

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM) 

        zones = Zone.query.all()
        print(zones)

        for zone in zones:
            print('Zone Setup')
            GPIO.setup(zone.pinL, GPIO.OUT) 
            GPIO.setup(zone.pinR, GPIO.OUT) 
    
    def getLabel(self, zone):
        label = ''

        zoneR = Zone.query.filter_by(key=zone).first()
        if zoneR:
            label = zoneR.label

        return label

    def getToggle(self, zone):
        togg = False

        zoneR = Zone.query.filter_by(key=zone).first()
        if zoneR:
            togg = zoneR.toggle

        return togg

    def getVolume(self, zone):
        vol = 0

        zoneR = Zone.query.filter_by(key=zone).first()
        print(zoneR.format())
        if zoneR:
            vol = zoneR.volume

        return vol

    def setZoneToggle(self, zone, toggl):
        zoneR = Zone.query.filter_by(key=zone).first()
        if zoneR:
            zoneR.updateToggle(toggl)
            GPIO.output(zoneR.pinL,toggl)
            GPIO.output(zoneR.pinR,toggl)
            
    def setZoneLabel(self, zone, label):
        zoneR = Zone.query.filter_by(key=zone).first()
        if zoneR:
            zoneR.updateLabel(label)
        

    def setZoneVolume(self, zone, vol):
        zoneR = Zone.query.filter_by(key=zone).first()
        if zoneR:
            zoneR.updateVolume(int(vol))
