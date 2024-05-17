clue = {}

while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": location, "weapon":weapon} #line 7
# main key        subKEY     value      subKEY    value
  print(clue)
  break

# clue = {}

# def prettyPrint():
#   """
#   to create a 2D dictonery we have to create a mina key value which
#   are connected to another mini key value.
#   that mini key value stores the data
#   """
#   """
#   basically creating a main key pair which is connected to a sub key pair and
#   that sub key pair are contaning values. thus creating a 2D dictionary
#   """
#   print()

  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()

# while True:
#   name = input("Name: ")
#   location = input("Location: ")
#   weapon = input("Weapon: ")

#   clue[name] = {"location": location, "weapon": weapon}

#   prettyPrint()

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}
# #created 3 normal dictionaries

# courseProgress = {"John": john, "Janet": janet, "Erica": erica}
# #created a dictionary with 3 keys and 3 sub dictionaries. thus making it a 2D dictionary.

# print(courseProgress['John'])
# "this will print the hole data about john in the dict"
# # so we come to know from the above print function that
# """

# we can access the value of sub key by calling main key followed by sub key."""

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John": john, "Janet": janet, "Erica": erica}

# print(courseProgress["Erica"]["daysCompleted"])
# # The first bracket contains the key that references the sub dictionary. The second bracket contains the key that references the sub item. This will output '75'.

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John": john, "Janet": janet, "Erica": erica}

# print(courseProgress["Erica"]["daysCompleted"])
# for key, value in courseProgress.items():

#   for subKey, subValue in value.items():
#     print(subKey,subValue)

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John": john, "Janet": janet, "Erica": erica}

print(courseProgress["Erica"]["daysCompleted"])
print(courseProgress["Janet"]["streak"])

print()
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John": john, "Janet": janet, "Erica": erica}

print(courseProgress["Erica"]["daysCompleted"])
print(courseProgress["Janet"]["streak"])
