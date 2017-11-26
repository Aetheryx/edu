from subprocess import call as exec # Wat we gebruiken voor desktop notificaties

def alert (title, desc):
  exec(['notify-send', '-i', '/home/aether/Documents/clock.png', title, desc])