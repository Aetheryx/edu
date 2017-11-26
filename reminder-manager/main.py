from threading import Timer # Wat we gebruiken voor de interval functie die checkt voor herrineringen die geleverd moeten worden

from utils.parseCommand import parseCommand
from utils.databaseFunctions import checkForExpired
from utils.colors import colors

def setInterval (func, sec):
    def funcWrapper ():
        setInterval(func, sec)
        func()
    t = Timer(sec, funcWrapper)
    t.start()
    return t

setInterval(checkForExpired, 1)

while True:
  try:
    parseCommand()
  except KeyboardInterrupt:
    print(colors['RESET'] + colors['GRIJS'] +
      '\nGebruik het' +
      colors['BOLD'] + colors['ROOD'] +
      ' exit ' +
      colors['RESET'] + colors['GRIJS'] +
      'commando om het programma te sluiten.' + 
      colors['RESET'])