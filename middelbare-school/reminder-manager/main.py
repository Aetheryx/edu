from threading import Timer # Dit is een asynchrone timer die ervoor zorgt
                            # dat we tegelijkertijd twee threads kunnen draaien
                            # zonder dat de ene de ander blokeert

from utils.parseerCommando import parseerCommando # De functie die zal herkennen wanneer iets wel of niet een commando is
from utils.databaseFuncties import findExpiring # De functie die kijkt of er uitlopende herrinering zijn
from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal

def zetInterval (func, sec): # Dit een functie die (asynchroon, dus zonder het programma te stoppen) andere functies kan draaien
    def funcWrapper (): # Deze functie zal de gegeven functie oproepen en dan weer de vaderfunctie roepen
        zetInterval(func, sec)
        func()
    t = Timer(sec, funcWrapper) # Hier zorgen we ervoor dat de funcWrapper functie na
    t.start()                   # zoveel tijd pas gerund word, met een asynchrone timer
    return t

zetInterval(findExpiring, 1) # We starten hier het interval dat zoekt naar uitlopende herrineringen


print(
  kleurtjes['GROEN'] +
  'Welkom! Probeer het commando' + 
  kleurtjes['CYAAN'] +
  ' help ' +
  kleurtjes['RESET'] + kleurtjes['GROEN'] +
  'voor een lijst met commandos.\n' +
  kleurtjes['RESET']
)

while True: # Hier starten we de loop dat zorgt voor het simuleren van de terminal - 
            # We sturen een input(), en (synchroon) zal het programma wachten totdat de executie
            # van die input() (dus totdat we drukken op enter) afloopt. Wanneer dat gebeurd, beginnen we opnieuw.
  try:
    parseerCommando() # Probeer een commando te herkennen van de input.
  except KeyboardInterrupt: # Wanneer we tijdens dat process een KeyboardInterrupt opvangen (een Ctrl-C, bedoeld om het programma te stoppen)
    print( # vertellen we de gebruiker dat er een 'exit' commando is.
      kleurtjes['RESET'] + kleurtjes['GRIJS'] +
      '\nGebruik het' +
      kleurtjes['BOLD'] + kleurtjes['ROOD'] +
      ' exit ' +
      kleurtjes['RESET'] + kleurtjes['GRIJS'] +
      'commando om het programma te sluiten.' + 
      kleurtjes['RESET']
    )