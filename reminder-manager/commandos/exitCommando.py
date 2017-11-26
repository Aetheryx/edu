from os import _exit # Dit is een functie die "schoon" alle execution threads en child processes van het programma afsluit - een "exit".
from utils.kleurtjes import kleurtjes # Het object wat alle ANSI-kleurcodes bevat voor de kleurtjes in de terminal

def exitCommando (input = None):
  print(kleurtjes['RESET'] + 'Doei!')
  _exit(0)