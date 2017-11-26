from time import time as now
from pymongo import MongoClient # Onze database
import sys

from utils.alert import alert

client = MongoClient()
db = client.myDB
collection = db.reminders

def addReminder (reminderText, expiryDate):
  doc = { 'reminderText': reminderText, 'expiryDate': expiryDate + float(now()) }
  collection.posts.insert_one(doc)

def deleteReminderByID (id):
  collection.posts.delete_one({ '_id': id })

def deleteReminderByContent (content):
  collection.posts.delete_one({ 'reminderText': content })

def listReminders ():
  result = []
  cursor = collection.posts.find()
  for res in cursor:
    result.append(res)
  return result

def checkForExpired ():
  cursor = collection.posts.find({ 'expiryDate': { '$lt': int(now()) } })
  for reminder in cursor:
    alert('Uw Herrinering', reminder['reminderText'])
    deleteReminderByID(reminder['_id'])
