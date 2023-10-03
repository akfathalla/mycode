#!/usr/bin/env python3
"""Understanding dictionaries """

def main():
    char_name = input.title("Which character do you want to know about? (Starlord, Mystique, Hulk)")
    char_stat = input.lower(" What statistic do you want to know about? (real name, powers, archenemy)")

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
#print ("Character Name: " + marvelchars[char_name[char_stat]])
print (marvelchars.keys()[char_name] + " 's " + marvelchars([char_name.keys()[char_stat]] + " is ") 

        main()

