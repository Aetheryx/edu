import re # Hiermee kunnen we regexes uitvoeren - bepaalde patronen vinden in tekst.
from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal.
from utils.databaseFuncties import addReminder # De database functie waarmee we nieuwe herrineringen kunnen toevoegen.

omgerekend = { # De omgerekende nummers voor hoeveel secondes die notatie is
  's': 1, # een seconde is 1 seconde
  'm': 60, # een minuut is 60 secondes
  'h': 3600, # een uur is 3600 secondes
  'd': 86400 # een dag is 86400 secondes
}

def addCommando (input):
  regex = re.search('(.*) ([0-9.]*)(s|m|h|d)', input) # We kijken of de input voldoet aan het schema voor het commando.
  if regex: # Als dat zo is,
    addReminder(regex.group(1), float(regex.group(2)) * omgerekend[regex.group(3)]) # voegen we een herrinering toe.
    print(
      kleurtjes['GROEN'] +
      'Herrinering successvol toegevoegd.' +
      kleurtjes['RESET']
    )
  else: # Als dat niet zo is,
    print( # vertellen we de gebruiker hoe je het commando gebruikt.
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'Gebruik: ' +
      kleurtjes['RESET'] + kleurtjes['GRIJS'] +
      'add <herrinering_tekst> <tijdstip>\n' +
      kleurtjes['RESET'] +
      'waarbij' +
      kleurtjes['GRIJS'] +
      ' tijdstip ' +
      kleurtjes['RESET'] +
      'het volgende schema volgt:\n' + 
      kleurtjes['GROEN'] +
      '<' +
      kleurtjes['GRIJS'] +
      'getal' +
      kleurtjes['GROEN'] +
      '><' +
      kleurtjes['GRIJS'] +
      's|m|h|d' +
      kleurtjes['GROEN'] +
      '>' +
      kleurtjes['RESET']
    )