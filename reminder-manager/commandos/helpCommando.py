from utils.kleurtjes import kleurtjes
from commandos.helpStatussen import helpStatussen # Importeer een object van alle hulp statussen voor de commandos

def verkrijgObjectSleutels (object):
  output = []
  for item in object:
    output.append(item)

  return output

def helpCommando (input = None):
  if not input:
    commandoLijst = verkrijgObjectSleutels(helpStatussen) # We zetten het object van 'commandoNaam => commandoHulp' om naar een array van commando namen
    print(
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'Hier heb je een lijst van alle commandos:\n' +
      kleurtjes['CYAAN'] +
      (kleurtjes['RESET'] + ', ' + kleurtjes['CYAAN']).join(commandoLijst) + '\n' +
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'Je kunt ook ' +
      kleurtjes['CYAAN'] + 
      'help <commando> ' + 
      kleurtjes['RESET'] + kleurtjes['GROEN'] +
      'uitvoeren voor meer hulp bij een bepaald commando.' +
      kleurtjes['RESET']
    )
  else:
    if not input in helpStatussen:
      print( # vertellen we de gebruiker dat dat niet herkend is als een commando
        kleurtjes['RESET'] + kleurtjes['BOLD'] + kleurtjes['ROOD'] +
        input +
        kleurtjes['RESET'] + kleurtjes['ROOD'] +
        ' is niet herkend als een commando.' +
        kleurtjes['RESET']
      )
    else:
      print(helpStatussen[input]) # We pakken de juiste hulp status vanuit het object, en die geven we door
