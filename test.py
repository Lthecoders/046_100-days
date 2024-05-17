import os
import random
import time

Mokedex = {}
# identifiner = 'classcification'
# name = 'name'
# type = 'type'
# special_move = 'special move'
# HP = 'HP'
# MP = 'MP'


# Mokedex[identifiner] = {
#     'name': name,
#     'type': type,
#     'special move': special_move,
#     'HP': HP,
#     'MP': MP
# }

# index = {
#     'name': 'name',
#     'type': 'type of moke',
#     'special move': 'special move',
#     'starting HP': 'starting HP',
#     'starting MP': 'starting MP'
# }


def prettyprint():
  for key, value in Mokedex.items():
    print(f"{key: ^20}", end='|')
    for subkey, subvalue in value.items():
      print(f"{subvalue: ^20} | ", end='')
    print()
  # for row, value in Mokedex.items():
  #     print(row + ': ')
  #     for key, val in value.items():
  #         print(f"{key}: {val}")
  #     print()


while True:
  print('\nadd your beast')
  moke_best='moke best data -->'
  name = input('\n\nenter the name -----> ')
  type_moke = input('\n\nenter the type -----> ')
  sepecialmove = input('\n\nenter the special move -----> ')
  starting_HP = input('\n\nenter the starting HP -----> ')
  starting_MP = input('\n\nenter the starting MP -----> ')

  Mokedex[moke_best] = {
          'name': name,
      'type of beast': type_moke,
      'special move': sepecialmove,
      'starting HP': starting_HP,
      'starting MP': starting_MP
  }
  # print("Name\t\t\tType\t\t\tHP\t\t\tMP\t\t\tSpecial Move")
  prettyprint()
