from commandos.deleteCommando import *
from commandos.listCommando   import *
from commandos.exitCommando   import *
from commandos.addCommando    import *

helpStatussen = {
  'add':    addHelp,
  'new':    addHelp,
  'ls':     listHelp, # Zoals je ziet kunnen we hier twee commando entries dezelfde functies geven,
  'list':   listHelp, # zodat zowel 'ls' als 'list' werken
  'del':    deleteHelp,
  'delete': deleteHelp,
  'exit':   exitHelp
}