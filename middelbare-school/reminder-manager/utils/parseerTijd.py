from math import floor

tijdMethodes = [86400, 3600, 60, 1] # De verschillende tijdstukken - een dag, een uur, een minuut en een seconde

def pad (tijdstuk): # Met deze functie zetten we een tijdgetal zoals 5 om naar 05 (als een string)
  string = str(tijdstuk)
  if len(string) < 2:
    return '0' + string
  else:
    return string

def parseerTijd (tijdIn): # De functie die tijd in seconde omzet naar DD:HH:MM:SS
  tijd = [ pad(floor(tijdIn / tijdMethodes[0])) ] # Eerst vullen we de array met het aantal dagen, want de berekening daarvoor is anders
  for methode in range(3):
    tijd.append(pad(floor(tijdIn % tijdMethodes[methode] / tijdMethodes[methode + 1]))) # Telkens voegen we het volgende stuk aan de array toe
  
  return ':'.join(tijd) # We hebben er niet veel aan als het een array is, het moet in DD:HH:MM:SS