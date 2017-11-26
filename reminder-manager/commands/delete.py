from utils.colors import colors
from utils.databaseFunctions import deleteReminderByContent

def delete (input):
  if not input:
    return print(colors['RESET'] + colors['GROEN'] +
      'Gebruik: ' +
      colors['RESET'] + colors['GRIJS'] +
      'delete herrinering_text' +
      colors['RESET'])

  deleteReminderByContent(input)
  print(
    colors['RESET'] + colors['GROEN'] +
    'Reminder successvol gewist.' +
    colors['RESET']
  )