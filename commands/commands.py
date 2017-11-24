from commands.add import add
from commands.listCommand import listCommand
from commands.exitApp import exitApp
from commands.delete import delete

commands = {
  'add': add,
  'new': add,
  'ls': listCommand,
  'list': listCommand,
  'del': delete,
  'delete': delete,
  'exit': exitApp
}