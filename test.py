from multiprocessing import Process
from time import sleep

p = 'asdf'

def f(name):
    print('hoi!')
    sleep(1)
    f('hoi')

def ipa():
  res = input('hoi?')
  if res == 'hallo':
    p.terminate()

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()

while True:
  ipa()