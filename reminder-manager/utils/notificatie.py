from subprocess import call as exec # Dit is een functie die we kunnen gebruiken om commando's uit te voeren op het systeem.
from platform import system # Een functie die ons verteld welk operatiesysteem wordt gebruikt...
operatieSysteem = system() # ...dit slaan we op in een variabele, zodat we niet steeds de functie oproepen
import os


if operatieSysteem == 'Windows': # Omdat Windows een buitenbeentje is en niet via de terminal een commando heeft voor notificaties,
  from win10toast import ToastNotifier # gebruiken we een externe bibliotheek voor notificaties op Windows.
  notify = ToastNotifier().show_toast

extensies = {
  'Darwin': 'png',
  'Linux': 'png',
  'Windows': 'ico' # Hier is Windows weer een buitenbeentje, voor het notificatieicoontje moet een .ico bestand gebruikt worden.
}
afbeeldingPath = os.path.join(os.getcwd(), 'assets', 'clock.' + extensies[operatieSysteem])

def stuurNotificatie (title, desc):
  if operatieSysteem == 'Linux':
    exec(['notify-send', '-i', afbeeldingPath, title, desc]) # Als het operatiesysteem Linux is, gebruiken we notify-send.
  elif operatieSysteem == 'Darwin':
    exec(['osascript', '-e', 'display notification ' + desc + ' with title ' + title]) # Als het operatiesysteem macOS is, gebruiken we een AppleScript/OSA-script.
  elif operatieSysteem == 'Windows':
    notify( # Als het operatiesysteem Windows is, gebruiken we de bibliotheek.
      title,
      desc,
      icon_path=afbeeldingPath,
      duration=10
    )