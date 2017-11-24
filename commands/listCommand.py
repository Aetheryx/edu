from utils.colors import colors
from utils.databaseFunctions import listReminders
import time


def listCommand (input = None):
  reminders = listReminders()
  if not reminders:
    return print(
      colors['RESET'] + colors['ROOD'] +
      'U heeft geen herrineringen!' + 
      colors ['RESET']
    )
  reminders = [
    '"' + reminder['reminderText'] + '"' + colors['RESET'] + colors['GRIJS'] +
    ' expiring at ' + colors['RESET'] + colors['CYAAN'] +
    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(reminder['expiryDate'])) +
    colors['RESET'] + colors['GRIJS'] +
    ' (in ' +
    colors ['RESET'] + colors['CYAAN'] +
    str(int(reminder['expiryDate'] - time.time())) +
    colors['RESET'] + colors['GRIJS'] +
    ' seconden)'
    for reminder in reminders]
  print('\n'.join(reminders) + colors['RESET'])