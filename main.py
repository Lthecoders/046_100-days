import os
import random
import time

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"

Mokedex = {}

working = 'classification'
name = 'name'
type = 'type'
special_move = 'special move'
HP = 'HP'
MP = 'MP'

work = 'making line'
line_for_name = '-------'
line_for_type = '-------'
line_for_special_move = '-------'
line_for_HP = '-------'
line_for_MP = '-------'

Mokedex[name] = {
    # 'name': name,
    'ty': type,
    'special move': special_move,
    'HP': HP,
    'MP': MP
}

Mokedex[line_for_name] = {
    # 'line name' : line_for_name,
    'line type': line_for_type,
    'line special move': line_for_special_move,
    'line HP': line_for_HP,
    'line MP': line_for_MP
}

green = '\033[32m'
normal = '\033[0m'


def prettyprint():

  for key, value in Mokedex.items():
    print(green)
    print(f"{key: ^15}", end='|')
    for subkey, subvalue in value.items():
      print(f"{subvalue: ^12} | ", end='')
    print()
  print(normal)
  leav_or_play = input(
      '\n\n\npress 1 for stop adding and 2 for continue adding --> ')
  if leav_or_play == '1':
    print('\n\n\n\nsaving data to our server....')
    print('\n\nPlease wait....')
    time.sleep(5)
    os.system('clear')
    print(purple, "\n\n\nthanks for playing 😀. your's Mokedex so far", normal)
    print('---------------------------------------------------\n\n\n')
    for key, value in Mokedex.items():
      print(green)
      print(f"{key: ^15}", end='|')
      for subkey, subvalue in value.items():
        print(f"{subvalue: ^12} | ", end='')
      print()

    exit()
  elif leav_or_play == '2':
    os.system('clear')
    print(green, '\n\n\n\nsaving....')
    time.sleep(4)
    os.system('clear')
    noChoise()
  else:
    print('invalid input')


def noChoise():
  while True:
    os.system('clear')
    print(
        yellow,
        '\n------>  👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾  <--------\n\n'
    )
    print(blue)
    print('\nadd your beast 👾')
    while True:
      print(blue)
      name = input('\n\nenter the name -----> ').strip().capitalize()
      if name == '' or name == ' ':
        print(red, '\ninvalid input try again ☹️', normal)
        continue
      else:
        break

    while True:
      print(blue)
      type_moke = input('\n\nenter the type -----> ').strip().capitalize()
      if type_moke == '' or type_moke == ' ':
        print(red, '\ninvalid input try again ☹️', normal)
        continue
      else:
        break

    while True:
      print(blue)
      sepecialmove = input(
          '\n\nenter the special move -----> ').strip().capitalize()
      if sepecialmove == '' or sepecialmove == ' ':
        print(red, '\ninvalid input try again ☹️', normal)
        continue
      else:
        break

    while True:
      print(blue)
      starting_HP = input(
          '\n\nenter the starting HP -----> ').strip().capitalize()
      if starting_HP == '' or starting_HP == ' ':
        print(red, '\ninvalid input try again ☹️', normal)
        continue
      else:
        break

    while True:
      print(blue)
      starting_MP = input(
          '\n\nenter the starting MP -----> ').strip().capitalize()
      if starting_MP == '' or starting_MP == ' ':
        print(red, '\ninvalid input try again ☹️', normal)
        continue
      else:
        break

    Mokedex[name] = {
        'type of beast': type_moke,
        'special move': sepecialmove,
        'starting HP': starting_HP,
        'starting MP': starting_MP
    }
    print()
    print()
    print()
    prettyprint()


print(
    yellow,
    '\n\n\n\n\n------>  👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾  <--------'
)

print('\n\n\nLoading....')
time.sleep(6)
os.system('clear')

noChoise()
