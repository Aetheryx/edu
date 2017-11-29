# Dit bestand bevat alle commandos.
from commandos.deleteCommando import *
from commandos.listCommando   import *
from commandos.exitCommando   import *
from commandos.helpCommando   import *
from commandos.addCommando    import *

commandos = {
  'help':   helpCommando,
  'add':    addCommando,
  'new':    addCommando,
  'ls':     listCommando, # Zoals je ziet kunnen we hier twee commando entries dezelfde functies geven,
  'list':   listCommando, # zodat zowel 'ls' als 'list' werken
  'del':    deleteCommando,
  'delete': deleteCommando,
  'exit':   exitCommando
}