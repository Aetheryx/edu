from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal
from utils.databaseFuncties import deleteReminderByContent # De database functie die we gebruiken om herrineringen te verwijderen, via hun bericht.

def deleteCommando (input):
  if not input: # Als er geen input is vertellen we de gebruiker hoe je het commando gebruikt.
    return print(
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'Gebruik: ' +
      kleurtjes['RESET'] + kleurtjes['GRIJS'] +
      'delete herrinering_text' +
      kleurtjes['RESET']
    )

  res = deleteReminderByContent(input) # Voer de database functie uit om de (potentiele) herrinering te verwijderen.
  if res.deleted_count == 0: # Als er geen herrineringen zijn verwijderd, dus als er geen herrineringen zijn verwijderd,
    print( # vertellen we de gebruiker dat er geen herrinering gevonden was.
      kleurtjes['RESET'] + kleurtjes['ROOD'] +
      'Ik heb geen herrinering met de naam ' +
      kleurtjes['GRIJS'] + kleurtjes['BOLD'] +
      input +
      kleurtjes['RESET'] + kleurtjes['ROOD'] +
      ' gevonden. Zie het commando ' +
      kleurtjes['RESET'] + kleurtjes['GRIJS'] + 
      'list' +
      kleurtjes['RESET'] + kleurtjes['ROOD'] +
      ' voor een lijst met commandos.' +
      kleurtjes['RESET']
    )
  else: # Als er wel een herrinering gevonden was,
    print( # vertellen we de gebruiker dat de herrinering gewist is.
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'Reminder successvol gewist.' +
      kleurtjes['RESET']
    )