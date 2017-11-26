from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal
from utils.parseerTijd import parseerTijd # Dit gebruiken we om secondes om te zetten in DD:HH:MM:SS
from utils.databaseFuncties import listReminders # De database functie die alle herrineringen opvangt.
import time # Een pakket waarmee we o.a. de huidige tijd in UNIX-tijd krijgen, en UNIX-tijd naar human-readable tijd kunnen omzetten.

def listCommando (input = None):
  reminders = listReminders()
  if not reminders: # Als er geen herrineringen zijn,
    return print( # vertellen we de gebruiker dat.
      kleurtjes['RESET'] + kleurtjes['ROOD'] +
      'U heeft geen herrineringen!' + 
      kleurtjes ['RESET']
    )
  reminders = [ # Hier construeren we een array wat uiteindelijk een array van strings wordt, die de reminders geformatteerd bevat.
    kleurtjes['CYAAN'] + 
    '"' + reminder['reminderText'] + '"'
    + kleurtjes['RESET'] + kleurtjes['GRIJS'] +
    ' loopt af op ' +
    kleurtjes['RESET'] + kleurtjes['CYAAN'] +
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reminder['expiryDate'])) + # We zetten de UNIX-tijd van de herrinering om tot human-readable tijd.
    kleurtjes['RESET'] + kleurtjes['GRIJS'] +
    ' (in ' +
    kleurtjes ['RESET'] + kleurtjes['CYAAN'] +
    parseerTijd(int(reminder['expiryDate'] - time.time())) +
    kleurtjes['RESET'] + kleurtjes['GRIJS'] +
    ')'
    for reminder in reminders]
  print('\n'.join(reminders) + kleurtjes['RESET'])