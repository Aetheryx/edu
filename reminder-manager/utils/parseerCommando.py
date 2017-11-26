from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal
from commandos.commandos import commandos # Importeer een object van alle commandos.

def parseerCommando ():
  antwoord = input(
    kleurtjes['BLAUW'] + # Dit is het prompt zelf.
    'Reminder Manager >>> ' +
    kleurtjes['CYAAN'] # Door voor het eind van de output een ANSI-kleurcode te printen, 
  )                 # zal de input van de gebruiker met die kleur gekleurd zijn.
  commando = antwoord.split(' ')[0] # Het commando is aller eerste "woord" (het stukje van de string voor de eerste spatie).
  if commando in commandos: # Als het herkende commando bestaat,
    commandos[commando](antwoord.replace(commando, '').strip()) # roepen we de functie die bij dat commando hoort.
  else: # Als dat niet zo is,
    print( # vertellen we de gebruiker dat dat niet herkend is als een commando
      kleurtjes['RESET'] + kleurtjes['BOLD'] + kleurtjes['ROOD'] +
      commando +
      kleurtjes['RESET'] + kleurtjes['ROOD'] +
      ' is niet herkend als een commando.'
    )