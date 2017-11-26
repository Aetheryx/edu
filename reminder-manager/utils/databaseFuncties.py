# Dit bestand bevat alle database-functies die we gebruiken voor herrineringen.

from time import time as now # Deze functie geeft het huidig tijdstip in UNIX-tijd.
from pymongo import MongoClient # De bibliotheek die we gebruiken om een connectie te maken met MongoDB.
from utils.notificatie import stuurNotificatie # De functie voor de notificaties.

client = MongoClient() # In deze regels maken we een connectie met MongoDB
db = client.myDB # en maken we de variabele die hoort bij de database-tabel die we willen gebruiken.
collection = db.reminders

def addReminder (reminderText, expiryDate):
  doc = {
    'reminderText': reminderText, # De tekst die hoort bij een herrinering.
    'expiryDate': expiryDate + float(now()) # Hier tellen we de relatieve tijd tot de herrinering op bij het huidige tijdstip,
  }                                         # dus hebben we het absolute tijdstip van de herrinering.
  collection.posts.insert_one(doc)

def deleteReminderByID (id):
  collection.posts.delete_one({ '_id': id }) 

def deleteReminderByContent (content):
  return collection.posts.delete_one({ 'reminderText': content })

def listReminders ():
  result = [] # Eerst maken we een lege array.
  cursor = collection.posts.find() # We krijgen van PyMongo een Cursor voorwerp als we meerdere items opzoeken.
  for res in cursor: # Voor elk van de items in de cursor,
    result.append(res) # voegen we dat item toe aan de output-array.
  return result

def findExpiring ():
  cursor = collection.posts.find({ # We zoeken herrineringen, waarvan
    'expiryDate': { # de uitloopdatum
      '$lt': int(now()) # lager is dan het huidige tijdstip in UNIX-tijd (dus, in het verleden).
    }
  })
  for reminder in cursor: # Voor elk van deze uitgelopen herrineringen,
    stuurNotificatie('Uw Herrinering', reminder['reminderText']) # sturen we een notificatie
    deleteReminderByID(reminder['_id']) # en verwijderen we de herrinering
