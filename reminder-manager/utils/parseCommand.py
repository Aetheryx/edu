from utils.colors import colors
from commands.commands import commands

def parseCommand ():
  answer = input(colors['BLAUW'] +
    'Reminder Manager >>> ' +
    colors['CYAAN'])
  commando = answer.split(' ')[0]
  if commando in commands:
    commands[commando](answer.replace(commando, '').strip())
  else:
    print(colors['RESET'] + colors['BOLD'] + colors['ROOD'] +
      commando +
      colors['RESET'] + colors['ROOD'] +
      ' is niet herkend als een commando.')