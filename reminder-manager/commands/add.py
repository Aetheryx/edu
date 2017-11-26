import re
from utils.colors import colors
from utils.databaseFunctions import addReminder

convertedTimes = {
  's': 1,
  'm': 60,
  'h': 3600,
  'd': 86400
}

def add (input):
  regex = re.search('(.*) ([0-9]*)(s|m|h|d)', input)
  if regex:
    print(colors['RESET'] + 'goedzo')
    addReminder(regex.group(1), int(regex.group(2)) * convertedTimes[regex.group(3)])
  else:
    print(colors['RESET'] + colors['GROEN'] +
      'Gebruik: ' +
      colors['RESET'] + colors['GRIJS'] +
      'add herrinering_text tijdstip' +
      colors['RESET'])