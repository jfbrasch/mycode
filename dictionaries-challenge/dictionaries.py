#!/usr/bin/python3

##  Which character do you want to know about? (Starlord, Mystique, Hulk)

# Asks for user input1
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)")

# Asks for user input2
char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")

# assigns dictionary of marvel chars
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

# Assigns selected Hero name from char_name
selected_name = marvelchars[char_name]
# Assigns selected stat and selected Hero's name
selected_power = selected_name[char_stat]

# Prints out selected information.
print(char_name.title() + "'s " + char_stat.lower() + " is: " + selected_power)

# Second print using print f.
print(f"{char_name.title()}'s {char_stat.lower()} is: {selected_power}")


