# Dit bestand bevat alle commandos.
from commandos.addCommando import addCommando
from commandos.listCommando import listCommando
from commandos.exitCommando import exitCommando
from commandos.deleteCommando import deleteCommando

commandos = {
  'add': addCommando,
  'new': addCommando,
  'ls': listCommando,
  'list': listCommando,
  'del': deleteCommando,
  'delete': deleteCommando,
  'exit': exitCommando
}