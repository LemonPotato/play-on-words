"""
Main file - Play on Words

Licensed under MIT license
(c) Nathan Paul Peterson 2021

Adjective list created by hugsy
    https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913

Verbs list created by aaronbassett
    https://github.com/aaronbassett/Pass-phrase/blob/master/verbs.txt

Adverbs list created by janester
    https://github.com/janester/mad_libs/blob/master/List%20of%20Adverbs.txt

Nouns list from desiquintans.com
    http://www.desiquintans.com/downloads/nounlist/nounlist.txt
"""

import PySimpleGUI as sg
import random
import time
import sys
from PyDictionary import PyDictionary
import linecache


verbBank = ['Run','Walk','Swim','Write','Climb']
usedVerbs = ['Speak']
nounBank = ['Cat','Sock','Ship','Monkey','Cabbage']
usedNouns = ['Midnight']
adjBank = ['Bashful','Beautiful','Meaningless','Hungry','Pretty']
usedAdjs = ['Unhappy']
advBank = ['Securely','Sadly','Clumsily','Badly','Diligently']
usedAdvs = ['Angrily']

textSpeed = 0.03
coloredText = True

charType = None
noun1 = None
noun2 = None
noun3 = None
noun4 = None
noun5 = None
noun6 = None
noun7 = None
noun8 = None
noun9 = None
noun10 = None

verb1 = None
verb2 = None
verb3 = None
verb4 = None
verb5 = None
verb6 = None
verb7 = None
verb8 = None
verb9 = None
verb10 = None

adj1 = None
adj2 = None
adj3 = None
adj4 = None
adj5 = None
adj6 = None
adj7 = None
adj8 = None
adj9 = None
adj10 = None

adv1 = None
adv2 = None
adv3 = None
adv4 = None
adv5 = None
adv6 = None
adv7 = None
adv8 = None
adv9 = None
adv10 = None

gender = None
pronounHe = None
pronounHis = None
pronounHim = None

curStory = "none"

#bank reset if any of the banks are empty
def bankReset():
  global nounBank
  global verbBank
  global adjBank
  global advBank
  
  if not nounBank:
    nounBank = ['Cat','Sock','Ship','Monkey','Cabbage']
    usedNouns = ['Midnight']
  
  if not verbBank:
    verbBank = ['Run','Walk','Swim','Write','Climb']
    usedVerbs = ['Speak']
  
  if not adjBank:
    adjBank = ['Bashful','Beautiful','Meaningless','Hungry','Pretty']
    usedAdjs = ['Unhappy']
  
  if not advBank:
    advBank = ['Fastly','Sadly','Clumsily','Badly','Diligently']
    usedAdvs = ['Angrily']

def print_slowly(text):
  global textSpeed
  global coloredText
  
  for c in text:
    if c == ' ': #skips wait if it's a space
      sys.stdout.write(c)
    elif c == '.' or c == '?' or c == '!': #long pause after end of a sentence
      sys.stdout.write(c)
      time.sleep(0.5)
    elif c == ',': #short pause after commas
      sys.stdout.write(c)
      time.sleep(0.2)
    
    elif c == '[':
        time.sleep(0.2)
    
    else: #all other characters
      sys.stdout.write(c)
      time.sleep(textSpeed)

#program to edit word banks
def bankEdit():
  global nounBank
  global verbBank
  global adjBank
  global advBank
  
  window = sg.Window("Edit banks",[[sg.Text('Select a word bank to edit')],[sg.Button('Adjective Bank')],[sg.Button('Verb Bank')],[sg.Button('Noun Bank')],[sg.Button('Adverb Bank')],[sg.Button('Main Menu')]]).Finalize()
  
  
  while True:
      event, values = window.read()
      if event == "Main Menu":
          window.close()
          mainMenu()
          
      elif event == "Adjective Bank":
          window.close()
          window = sg.Window("Edit adjective bank",
                             [[sg.Text("How would you like to edit the adjective bank?")],
                              [sg.Button("Add words")],
                              [sg.Button("Add random word")],
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          
          while True:
                event, values = window.read()
                if event == "Return to bank edit":
                    window.close()
                    bankEdit()
                    
                elif event == sg.WIN_CLOSED:
                    window.close()
                    break
                elif event == "Add words":
                    window.close()
                    window = sg.Window("Adjective Bank: Add",
                                       [[sg.Text("Input a word to add to the Adjective Bank")],
                                        [sg.InputText()],
                                        [sg.Button("Submit")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Submit":
                            window.close()
                            adjBank.append(values[0].capitalize())
                            bankEdit()
                            
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                            
                elif event == "Add random word":
                    window.close()
                    
                    dictionary = PyDictionary()

                    adjfile = open("adjectives.txt","r")

                    #finds the number of lines in the file
                    adjcount = 0
                    for x in adjfile:
                        adjcount += 1

                    #finds a random number between 1 and the number of lines
                    randlinenum = random.randint(1,adjcount)

                    #finds the random line generated
                    randline = linecache.getline('adjectives.txt',randlinenum)

                    #finds the definition for the random word
                    randdef = str(dictionary.meaning(randline))

                    #finds the points to cut in the definition
                    cutpoint1 = randdef.find('[')+1
                    cutpoint2 = randdef.find(']')

                    #assembles definition without extra characters
                    randdef = randdef[cutpoint1:cutpoint2]
                    
                    popup = sg.popup_yes_no(randline + randdef, title = "Random adjective")
                    
                    if popup == "Yes":
                        randline = randline.capitalize()
                        adjBank.append(randline)
                        window.close()
                        bankEdit()
                    elif popup == "No":
                        window.close()
                        bankEdit()
                    
                elif event == "Remove words":
                    window.close()
                    listAdj = '\n'
                    for i in range(len(adjBank)):
                        listAdj += str(i+1) + '. '
                        listAdj += adjBank[i]
                        listAdj += '\n'
                    window = sg.Window("Adjective Bank: Remove",
                                       [[sg.Text("Adjective Bank:\n" + listAdj)],
                                        [sg.Input(key = 'intLock', enable_events = True)],
                                        [sg.Button("Remove")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                        elif event == "intLock" and values['intLock'] and values['intLock'][-1] not in ('0123456789'):
                            window['intLock'].update(values['intLock'][:-1])
                        elif event == "Remove":
                            print(int(values['intLock']))
                            removeElm = int(values['intLock']) - 1
                            adjBank.pop(removeElm)
                            window.close()
                            bankEdit()
                            
                elif event == "View words":
                     window.close()
                     listAdj = '\n'
                     for i in range(len(adjBank)):
                        listAdj += str(i+1) + '. '
                        listAdj += adjBank[i]
                        listAdj += '\n'
                     window = sg.Window("Adjective List: View",
                                        [[sg.Text("Adjective Bank:\n" + listAdj)],
                                         [sg.Button("Return to bank edit")]]).Finalize()
                     
                     while True:
                         event, values = window.read()
                         if event == "Return to bank edit":
                             window.close()
                             bankEdit()
                         elif event == sg.WIN_CLOSED:
                             window.close()
                             break
      
      elif event == "Verb Bank":
          window.close()
          window = sg.Window("Edit verb bank",
                             [[sg.Text("How would you like to edit the verb bank?")],
                              [sg.Button("Add words")],
                              [sg.Button("Add random word")],
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          
          while True:
                event, values = window.read()
                if event == "Return to bank edit":
                    window.close()
                    bankEdit()
                    
                elif event == sg.WIN_CLOSED:
                    window.close()
                    break
                elif event == "Add words":
                    window.close()
                    window = sg.Window("Verb Bank: Add",
                                       [[sg.Text("Input a word to add to the Verb Bank")],
                                        [sg.InputText()],
                                        [sg.Button("Submit")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Submit":
                            window.close()
                            verbBank.append(values[0].capitalize())
                            bankEdit()
                            
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                
                elif event == "Add random word":
                    window.close()
                    
                    dictionary = PyDictionary()

                    verbfile = open("verbs.txt","r")

                    #finds the number of lines in the file
                    verbcount = 0
                    for x in verbfile:
                        verbcount += 1

                    #finds a random number between 1 and the number of lines
                    randlinenum = random.randint(1,verbcount)

                    #finds the random line generated
                    randline = linecache.getline('verbs.txt',randlinenum)

                    #finds the definition for the random word
                    randdef = str(dictionary.meaning(randline))

                    #finds the points to cut in the definition
                    cutpoint1 = randdef.find('[')+1
                    cutpoint2 = randdef.find(']')

                    #assembles definition without extra characters
                    randdef = randdef[cutpoint1:cutpoint2]
                    
                    popup = sg.popup_yes_no(randline + randdef, title = "Random verb")
                    
                    if popup == "Yes":
                        randline = randline.capitalize()
                        verbBank.append(randline)
                        window.close()
                        bankEdit()
                    elif popup == "No":
                        window.close()
                        bankEdit()
                
                elif event == "Remove words":
                    window.close()
                    listVerb = '\n'
                    for i in range(len(verbBank)):
                        listVerb += str(i+1) + '. '
                        listVerb += verbBank[i]
                        listVerb += '\n'
                    window = sg.Window("Verb Bank: Remove",
                                       [[sg.Text("Verb Bank:\n" + listVerb)],
                                        [sg.Input(key = 'intLock', enable_events = True)],
                                        [sg.Button("Remove")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                        elif event == "intLock" and values['intLock'] and values['intLock'][-1] not in ('0123456789'):
                            window['intLock'].update(values['intLock'][:-1])
                        elif event == "Remove":
                            print(int(values['intLock']))
                            removeElm = int(values['intLock']) - 1
                            verbBank.pop(removeElm)
                            window.close()
                            bankEdit()
                            
                elif event == "View words":
                     window.close()
                     listVerb = '\n'
                     for i in range(len(verbBank)):
                        listVerb += str(i+1) + '. '
                        listVerb += verbBank[i]
                        listVerb += '\n'
                     window = sg.Window("Verb List: View",
                                        [[sg.Text("Verb Bank:\n" + listVerb)],
                                         [sg.Button("Return to bank edit")]]).Finalize()
                     
                     while True:
                         event, values = window.read()
                         if event == "Return to bank edit":
                             window.close()
                             bankEdit()
                         elif event == sg.WIN_CLOSED:
                             window.close()
                             break
      
      
      elif event == "Adverb Bank":
          window.close()
          window = sg.Window("Edit adverb bank",
                             [[sg.Text("How would you like to edit the adverb bank?")],
                              [sg.Button("Add words")],
                              [sg.Button("Add random word")],
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          
          while True:
                event, values = window.read()
                if event == "Return to bank edit":
                    window.close()
                    bankEdit()
                    
                elif event == sg.WIN_CLOSED:
                    window.close()
                    break
                elif event == "Add words":
                    window.close()
                    window = sg.Window("Adverb Bank: Add",
                                       [[sg.Text("Input a word to add to the Adverb Bank")],
                                        [sg.InputText()],
                                        [sg.Button("Submit")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Submit":
                            window.close()
                            advBank.append(values[0].capitalize())
                            bankEdit()
                            
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                            
                elif event == "Remove words":
                    window.close()
                    listAdv = '\n'
                    for i in range(len(advBank)):
                        listAdv += str(i+1) + '. '
                        listAdv += advBank[i]
                        listAdv += '\n'
                    window = sg.Window("Adverb Bank: Remove",
                                       [[sg.Text("Adverb Bank:\n" + listAdv)],
                                        [sg.Input(key = 'intLock', enable_events = True)],
                                        [sg.Button("Remove")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                        elif event == "intLock" and values['intLock'] and values['intLock'][-1] not in ('0123456789'):
                            window['intLock'].update(values['intLock'][:-1])
                        elif event == "Remove":
                            print(int(values['intLock']))
                            removeElm = int(values['intLock']) - 1
                            advBank.pop(removeElm)
                            window.close()
                            bankEdit()
                            
                elif event == "Add random word":
                    window.close()
                    
                    dictionary = PyDictionary()

                    advfile = open("adverbs.txt","r")

                    #finds the number of lines in the file
                    advcount = 0
                    for x in advfile:
                        advcount += 1

                    #finds a random number between 1 and the number of lines
                    randlinenum = random.randint(1,advcount)

                    #finds the random line generated
                    randline = linecache.getline('adverbs.txt',randlinenum)

                    #finds the definition for the random word
                    randdef = str(dictionary.meaning(randline))

                    #finds the points to cut in the definition
                    cutpoint1 = randdef.find('[')+1
                    cutpoint2 = randdef.find(']')

                    #assembles definition without extra characters
                    randdef = randdef[cutpoint1:cutpoint2]
                    
                    popup = sg.popup_yes_no(randline + randdef, title = "Random adverb")
                    
                    if popup == "Yes":
                        randline = randline.capitalize()
                        advBank.append(randline)
                        window.close()
                        bankEdit()
                    elif popup == "No":
                        window.close()
                        bankEdit()
                
                elif event == "View words":
                     window.close()
                     listAdv = '\n'
                     for i in range(len(verbBank)):
                        listAdv += str(i+1) + '. '
                        listAdv += advBank[i]
                        listAdv += '\n'
                     window = sg.Window("Adverb List: View",
                                        [[sg.Text("Adverb Bank:\n" + listAdv)],
                                         [sg.Button("Return to bank edit")]]).Finalize()
                     
                     while True:
                         event, values = window.read()
                         if event == "Return to bank edit":
                             window.close()
                             bankEdit()
                         elif event == sg.WIN_CLOSED:
                             window.close()
                             break
      
      elif event == "Noun Bank":
          window.close()
          window = sg.Window("Edit noun bank",
                             [[sg.Text("How would you like to edit the noun bank?")],
                              [sg.Button("Add words")],
                              [sg.Button("Add random word")],
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          
          while True:
                event, values = window.read()
                if event == "Return to bank edit":
                    window.close()
                    bankEdit()
                    
                elif event == sg.WIN_CLOSED:
                    window.close()
                    break
                elif event == "Add words":
                    window.close()
                    window = sg.Window("Verb Bank: Add",
                                       [[sg.Text("Input a word to add to the Noun Bank")],
                                        [sg.InputText()],
                                        [sg.Button("Submit")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Submit":
                            window.close()
                            verbBank.append(values[0].capitalize())
                            bankEdit()
                            
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                
                elif event == "Add random word":
                    window.close()
                    
                    dictionary = PyDictionary()

                    nounfile = open("nouns.txt","r")

                    #finds the number of lines in the file
                    nouncount = 0
                    for x in nounfile:
                        nouncount += 1

                    #finds a random number between 1 and the number of lines
                    randlinenum = random.randint(1,nouncount)

                    #finds the random line generated
                    randline = linecache.getline('nouns.txt',randlinenum)

                    #finds the definition for the random word
                    randdef = str(dictionary.meaning(randline))

                    #finds the points to cut in the definition
                    cutpoint1 = randdef.find('[')+1
                    cutpoint2 = randdef.find(']')

                    #assembles definition without extra characters
                    randdef = randdef[cutpoint1:cutpoint2]
                    
                    popup = sg.popup_yes_no(randline + randdef, title = "Random noun")
                    
                    if popup == "Yes":
                        randline = randline.capitalize()
                        nounBank.append(randline)
                        window.close()
                        bankEdit()
                    elif popup == "No":
                        window.close()
                        bankEdit()
                
                elif event == "Remove words":
                    window.close()
                    listNoun = '\n'
                    for i in range(len(nounBank)):
                        listNoun += str(i+1) + '. '
                        listNoun += nounBank[i]
                        listNoun += '\n'
                    window = sg.Window("Noun Bank: Remove",
                                       [[sg.Text("Noun Bank:\n" + listNoun)],
                                        [sg.Input(key = 'intLock', enable_events = True)],
                                        [sg.Button("Remove")],
                                        [sg.Button("Return to bank edit")]]).Finalize()
                    
                    while True:
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            window.close()
                            break
                        elif event == "Return to bank edit":
                            window.close()
                            bankEdit()
                        elif event == "intLock" and values['intLock'] and values['intLock'][-1] not in ('0123456789'):
                            window['intLock'].update(values['intLock'][:-1])
                        elif event == "Remove":
                            print(int(values['intLock']))
                            removeElm = int(values['intLock']) - 1
                            nounBank.pop(removeElm)
                            window.close()
                            bankEdit()
                            
                elif event == "View words":
                     window.close()
                     listNoun = '\n'
                     for i in range(len(nounBank)):
                        listNoun += str(i+1) + '. '
                        listNoun += nounBank[i]
                        listNoun += '\n'
                     window = sg.Window("Noun List: View",
                                        [[sg.Text("Noun Bank:\n" + listNoun)],
                                         [sg.Button("Return to bank edit")]]).Finalize()
                     
                     while True:
                         event, values = window.read()
                         if event == "Return to bank edit":
                             window.close()
                             bankEdit()
                         elif event == sg.WIN_CLOSED:
                             window.close()
                             break
      
      elif event == sg.WIN_CLOSED:
          window.close()
          break

#program to end the story and return to main menu
def storyEnd(title,char,ending):
  end = sg.popup("Story: " + title,"Character: " + char,"Ending: " + "'" + ending + "'")
  mainMenu()

#program to select gender
def genGender():
  global gender
  global pronounHe
  global pronounHis
  global pronounHim
  
  #selects gender
  gender = random.randint(1,2)
  if gender == 1:
    gender = 'male'
  elif gender == 2:
    gender = 'female'
  else:
    gender = 'male'
  
  if gender == 'male':
    pronounHe = 'he'
    pronounHis = 'his'
    pronounHim = 'him'
  else:
    pronounHe = 'she'
    pronounHis = 'her'
    pronounHim = 'her'

#generate unique words
def genWords():
  global nounBank
  global usedNouns
  global verbBank
  global usedVerbs
  global adjBank
  global usedAdjs
  global advBank
  global usedAdvs
  
  #resets used word lists
  for i in range(len(usedNouns)):
    nounBank.append(usedNouns[i])
  usedNouns *= 0
    
  for i in range(len(usedVerbs)):
    verbBank.append(usedVerbs[i])
  verbBank *= 0
    
  for i in range(len(usedAdjs)):
    adjBank.append(usedAdjs[i])
  adjBank *= 0
    
  for i in range(len(usedAdvs)):
    advBank.append(usedAdvs[i])
  advBank *= 0
  
  global charType
  
  global noun1
  global noun2
  global noun3
  global noun4
  global noun5
  global noun6
  global noun7
  global noun8
  global noun9
  global noun10
  
  global verb1
  global verb2
  global verb3
  global verb4
  global verb5
  global verb6
  global verb7
  global verb8
  global verb9
  global verb10
  
  global adj1
  global adj2
  global adj3
  global adj4
  global adj5
  global adj6
  global adj7
  global adj8
  global adj9
  global adj10
  
  global adv1
  global adv2
  global adv3
  global adv4
  global adv5
  global adv6
  global adv7
  global adv8
  global adv9
  global adv10
  
  #random, unique word generation
  
  #chooses character species
  if nounBank:
    charType = random.choice(nounBank)
    nounBank.remove(charType)
    usedNouns.append(charType)
  else:
    charType = random.choice(usedNouns)
  
  #nouns
  if nounBank:
    noun1 = random.choice(nounBank)
    nounBank.remove(noun1)
    usedNouns.append(noun1)
  else:
    noun1 = random.choice(usedNouns)
  
  if nounBank:
    noun2 = random.choice(nounBank)
    nounBank.remove(noun2)
    usedNouns.append(noun2)
  else:
    noun2 = random.choice(usedNouns)
    
  if nounBank:
    noun3 = random.choice(nounBank)
    nounBank.remove(noun3)
    usedNouns.append(noun3)
  else:
    noun3 = random.choice(usedNouns)
  
  if nounBank:
    noun4 = random.choice(nounBank)
    nounBank.remove(noun4)
    usedNouns.append(noun4)
  else:
    noun4 = random.choice(usedNouns)
  
  if nounBank:
    noun5 = random.choice(nounBank)
    nounBank.remove(noun5)
    usedNouns.append(noun5)
  else:
    noun5 = random.choice(usedNouns)
  
  if nounBank:
    noun6 = random.choice(nounBank)
    nounBank.remove(noun6)
    usedNouns.append(noun6)
  else:
    noun6 = random.choice(usedNouns)
  
  if nounBank:
    noun7 = random.choice(nounBank)
    nounBank.remove(noun7)
    usedNouns.append(noun7)
  else:
    noun7 = random.choice(usedNouns)
  
  if nounBank:
    noun8 = random.choice(nounBank)
    nounBank.remove(noun8)
    usedNouns.append(noun8)
  else:
    noun8 = random.choice(usedNouns)
  
  if nounBank:
    noun9 = random.choice(nounBank)
    nounBank.remove(noun9)
    usedNouns.append(noun9)
  else:
    noun9 = random.choice(usedNouns)
  
  if nounBank:
    noun10 = random.choice(nounBank)
    nounBank.remove(noun10)
    usedNouns.append(noun10)
  else:
    noun10 = random.choice(usedNouns)
  
  
  
  #verbs
  if verbBank:
    verb1 = random.choice(verbBank)
    verbBank.remove(verb1)
    usedVerbs.append(verb1)
  else:
    verb1 = random.choice(usedVerbs)
  
  if verbBank:
    verb2 = random.choice(verbBank)
    verbBank.remove(verb2)
    usedVerbs.append(verb2)
  else:
    verb2 = random.choice(usedVerbs)
    
  if verbBank:
    verb3 = random.choice(verbBank)
    verbBank.remove(verb3)
    usedVerbs.append(verb3)
  else:
    verb3 = random.choice(usedVerbs)
  
  if verbBank:
    verb4 = random.choice(verbBank)
    verbBank.remove(verb4)
    usedVerbs.append(verb4)
  else:
    verb4 = random.choice(usedVerbs)
  
  if verbBank:
    verb5 = random.choice(verbBank)
    verbBank.remove(verb5)
    usedVerbs.append(verb5)
  else:
    verb5 = random.choice(usedVerbs)
  
  if verbBank:
    verb6 = random.choice(verbBank)
    verbBank.remove(verb6)
    usedVerbs.append(verb6)
  else:
    verb6 = random.choice(usedVerbs)
  
  if verbBank:
    verb7 = random.choice(verbBank)
    verbBank.remove(verb7)
    usedVerbs.append(verb7)
  else:
    verb7 = random.choice(usedVerbs)
  
  if verbBank:
    verb8 = random.choice(verbBank)
    verbBank.remove(verb8)
    usedVerbs.append(verb8)
  else:
    verb8 = random.choice(usedVerbs)
  
  if verbBank:
    verb9 = random.choice(verbBank)
    verbBank.remove(verb9)
    usedVerbs.append(verb9)
  else:
    verb9 = random.choice(usedVerbs)
  
  if verbBank:
    verb10 = random.choice(verbBank)
    verbBank.remove(verb10)
    usedVerbs.append(verb10)
  else:
    verb10 = random.choice(usedVerbs)


  #adjectives
  if adjBank:
    adj1 = random.choice(adjBank)
    adjBank.remove(adj1)
    usedAdjs.append(adj1)
  else:
    adj1 = random.choice(usedAdjs)
  
  if adjBank:
    adj2 = random.choice(adjBank)
    adjBank.remove(adj2)
    usedAdjs.append(adj2)
  else:
    adj2 = random.choice(usedAdjs)
    
  if adjBank:
    adj3 = random.choice(adjBank)
    adjBank.remove(adj3)
    usedAdjs.append(adj3)
  else:
    adj3 = random.choice(usedAdjs)
  
  if adjBank:
    adj4 = random.choice(adjBank)
    adjBank.remove(adj4)
    usedAdjs.append(adj4)
  else:
    adj4 = random.choice(usedAdjs)
  
  if adjBank:
    adj5 = random.choice(adjBank)
    adjBank.remove(adj5)
    usedAdjs.append(adj5)
  else:
    adj5 = random.choice(usedAdjs)
  
  if adjBank:
    adj6 = random.choice(adjBank)
    adjBank.remove(adj6)
    usedAdjs.append(adj6)
  else:
    adj6 = random.choice(usedAdjs)
  
  if adjBank:
    adj7 = random.choice(adjBank)
    adjBank.remove(adj7)
    usedAdjs.append(adj7)
  else:
    adj7 = random.choice(usedAdjs)
  
  if adjBank:
    adj8 = random.choice(adjBank)
    adjBank.remove(adj8)
    usedAdjs.append(adj8)
  else:
    adj8 = random.choice(usedAdjs)
  
  if adjBank:
    adj9 = random.choice(adjBank)
    adjBank.remove(adj9)
    usedAdjs.append(adj9)
  else:
    adj9 = random.choice(usedAdjs)
  
  if adjBank:
    adj10 = random.choice(adjBank)
    adjBank.remove(adj10)
    usedAdjs.append(adj10)
  else:
    adj10 = random.choice(usedAdjs)


  #adverbs
  if advBank:
    adv1 = random.choice(advBank)
    advBank.remove(adv1)
    usedAdvs.append(adv1)
  else:
    adv1 = random.choice(usedAdvs)
  
  if advBank:
    adv2 = random.choice(advBank)
    advBank.remove(adv2)
    usedAdvs.append(adv2)
  else:
    adv2 = random.choice(usedAdvs)
    
  if advBank:
    adv3 = random.choice(advBank)
    advBank.remove(adv3)
    usedAdvs.append(adv3)
  else:
    adv3 = random.choice(usedAdvs)
  
  if advBank:
    adv4 = random.choice(advBank)
    advBank.remove(adv4)
    usedAdvs.append(adv4)
  else:
    adv4 = random.choice(usedAdvs)
  
  if advBank:
    adv5 = random.choice(advBank)
    advBank.remove(adv5)
    usedAdvs.append(adv5)
  else:
    adv5 = random.choice(usedAdvs)
  
  if advBank:
    adv6 = random.choice(advBank)
    advBank.remove(adv6)
    usedAdvs.append(adv6)
  else:
    adv6 = random.choice(usedAdvs)
  
  if advBank:
    adv7 = random.choice(advBank)
    advBank.remove(adv7)
    usedAdvs.append(adv7)
  else:
    adv7 = random.choice(usedAdvs)
  
  if advBank:
    adv8 = random.choice(advBank)
    advBank.remove(adv8)
    usedAdvs.append(adv8)
  else:
    adv8 = random.choice(usedAdvs)
  
  if advBank:
    adv9 = random.choice(advBank)
    advBank.remove(adv9)
    usedAdvs.append(adv9)
  else:
    adv9 = random.choice(usedAdvs)
  
  if advBank:
    adv10 = random.choice(advBank)
    advBank.remove(adv10)
    usedAdvs.append(adv10)
  else:
    adv10 = random.choice(usedAdvs)
  
  
  #convert all words to lowercase
  charType = charType.lower()
  
  
  noun1 = noun1.lower()
  noun2 = noun2.lower()
  noun3 = noun3.lower()
  noun4 = noun4.lower()
  noun5 = noun5.lower()
  noun6 = noun6.lower()
  noun7 = noun7.lower()
  noun8 = noun8.lower()
  noun9 = noun9.lower()
  noun10 = noun10.lower()
  
  verb1 = verb1.lower()
  verb2 = verb2.lower()
  verb3 = verb3.lower()
  verb4 = verb4.lower()
  verb5 = verb5.lower()
  verb6 = verb6.lower()
  verb7 = verb7.lower()
  verb8 = verb8.lower()
  verb9 = verb9.lower()
  verb10 = verb10.lower()
  
  adj1 = adj1.lower()
  adj2 = adj2.lower()
  adj3 = adj3.lower()
  adj4 = adj4.lower()
  adj5 = adj5.lower()
  adj6 = adj6.lower()
  adj7 = adj7.lower()
  adj8 = adj8.lower()
  adj9 = adj9.lower()
  adj10 = adj10.lower()
  
  adv1 = adv1.lower()
  adv2 = adv2.lower()
  adv3 = adv3.lower()
  adv4 = adv4.lower()
  adv5 = adv5.lower()
  adv6 = adv6.lower()
  adv7 = adv7.lower()
  adv8 = adv8.lower()
  adv9 = adv9.lower()
  adv10 = adv10.lower()

#story "The Forest:
def story1():
    global textSpeed
    global charType
    window = sg.Window("The Forest",[[sg.Output(size=(80,20),key='-story-')],
                                                    [sg.Button('Run', bind_return_key=True)]])
    
    begin = 1
    while True:
        event, value = window.Read()
        if event == 'EXIT'  or event == sg.WIN_CLOSED:
            window.close()
            break # exit button clicked      
        if event == 'Run' and begin == 1:
            begin = 0
            title = "The Forest"
            
            #story
            print_slowly("A long time ago, there was a " + adj1 + " " + charType + " who lived in a far away land. What was " +pronounHis+ " name?")
            time.sleep(1)
            print("")
            
            charName = sg.popup_get_text('What was the ' + charType + '\'s name?','Please input a name.').capitalize()
            time.sleep(1)
            
            char = charName + " the " + charType
            
            print_slowly("Ah! Our " + adj1 + " " + charType + " was named " + charName + "! What a " + adj2 + " name! It should be; it was passed down to " + pronounHim + " from " + pronounHis + " " + adj3 + " Aunt Margerie. Never mind the fact that she's a " + noun1 + " and " + pronounHe +"'s a " + charType + ", it's a family name.")
            print("")
            print("")
            time.sleep(1)
            print_slowly("It was a dark and " + adj4 + " night. Our " + charName + " the " + charType + " is " + verb1  + "ing through a thicket of " + adj5 + " bushes. As "+pronounHe+" " + verb2 + "s back to the outside world, "+ pronounHe + " hears a loud crash, as if an overweight " + noun2 + " had just come crashing through " + pronounHis + " " + noun3 + ".")
            print("")
            print("")
            time.sleep(1)
            
            choice = None
            while choice != 'yes' and choice != 'no' and choice != 'Yes' and choice != 'No' and choice != 'y' and choice != 'n' and choice != 'Y' and choice != 'N':
                choice = sg.popup_get_text('Does ' + charName + ' want to examine the noise?','Please input yes or no.')
            
            if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
                print_slowly(charName + " " + verb3 + "s forward " + adv1 + ". " + pronounHe.capitalize() + " looks around, trying to identify the source of the noise that sounded as if an overweight " + noun2 + " had just come crashing through " + pronounHis + " " + noun3 + ".")
                print("")
                time.sleep(1)
                split = random.randint(1,3)
                
                if split == 1:
                  print_slowly(charName + " couldn't find anything. Confused as a " + adj6 + " " + noun4 + ", " + pronounHe + " decides to turn back the way he came.")
                  print("")
                  time.sleep(1)
                  randsize1 = str(random.randint(20,2000))
                  randsize2 = str(random.randint(20,2000))
                  randsize3 = str(random.randint(20,2000))
                  print_slowly("After several minutes of traveling, " + charName + " comes across a ditch. Well, more of a ravine. About " + randsize1 +" feet across and at least a " + randsize2 + " feet down, this scar on the land stretched for " + randsize3 + " feet in either direction.")
                  print("")
                  time.sleep(1)
                  
                  choice = None
                  while choice != 'yes' and choice != 'no' and choice != 'Yes' and choice != 'No' and choice != 'y' and choice != 'n' and choice != 'Y' and choice != 'N':
                      choice = sg.popup_get_text('Should ' + charName + ' attempt to cross the ravine?','Please input yes or no.')
                  
                  if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
                      print_slowly(charName + " tries to cross the ravine by jumping over it. Alas, one should be more careful, especially after such a close call with whatever produced that " + noun2 + "like noise. Like an overly " + adj7 + " " + noun4 + ", " + charName + " plummeted down the ravine to " + pronounHis + " death.")
                      print("")
                      time.sleep(1)
                      print_slowly("If I said that " + charName + " was remebered for " + pronounHis + " " + adj8 + ", I'd be lying. " + charName + " would only be remembered for how " + pronounHe +" went splat like a " + adj8 + " " + noun5 + ". So for all of the " + noun6 + "s out there, remember; watch your step.")
                      print("")
                      time.sleep(3)
                      ending = "Splat goes the weasel"
                      storyEnd(title,char,ending)
                      
                  elif choice == 'no' or choice == 'No' or choice == 'n' or choice == 'N':
                      print_slowly(charName + " decides to walk along the ravine for a time, until " + pronounHe +" finds something better to do.")
                      print("")
                      time.sleep(1)
                      print_slowly(charName + " is still walking.")
                      print("")
                      time.sleep(2)
                      print_slowly(charName + " is still walking.")
                      print("")
                      time.sleep(4)
                      print_slowly(charName + " is STILL walking.")
                      print("")
                      time.sleep(1)
                      print_slowly("It seems as if " + charName + "'s estimate that the ravine stretched on for " + randsize3 + " feet was much too short. It still stretched on beyond " + pronounHis + " sight.")
                      print("")
                      time.sleep(2)
                      print_slowly("Still, " + charName + " walked along it's edge. Compelled to do this by the command of some force " + charName + " was unaware of, "+ pronounHe +" would walk the edge of this ravine until the day "+ pronounHe + " died, alone and forgotten like a " + adj7 + " " + noun3 + " who didn't know the difference between a " + noun4 + " and a " + noun5 + ".")
                      print("")
                      time.sleep(3)
                      ending = "As God as my witness"
                      storyEnd(title,char,ending)
                
                elif split == 2 or split == 3:
                  print_slowly("Suddenly, a massive, " + adj6 + " " + noun4 + " jumped on top of " + charName + "! In a moment of panic, our hero flails "+ pronounHis +" arms " + adv2 + " around and grabs a nearby " + noun5 + ". Still suffocated by the thrashing " + noun4 + ", " + charName + " whacks the " + noun4 + ", which proceeds to drop dead on top of "+ pronounHim +".")
                  print("")
                  time.sleep(1)
                  print_slowly("Now, this appears like a good thing; the massive, " + adj6 + " " + noun4 + " was no longer " + verb3 + "ing our poor hero. However, this is NOT a good thing. While the massive, "  + adj6 + " " + noun4 + " was no longer " + verb3 + "ing our charming " + charType + ", there was now a DEAD massive, " + adj6 + " " + noun4 + " on top of our charming " + charType + ".")
                  print("")
                  time.sleep(1)
                  print_slowly("On any other day, I'm sure that " + charName + " would be quick to tell you how easily "+ pronounHe +" would've been able to heave a massive, " + adj6 + " " + noun4 + " off of "+ pronounHis +" chest, but on this particular day "+ pronounHe +" simply wasn't feeling it. Probably something " +  adj8 + " in the air. So it took several minutes for our champion to roll aside the glistening " + noun4 + " that lay on top of "+ pronounHim +" and stand up.")
                  print("")
                  time.sleep(1)
                  print_slowly("Our hero brushed "+ pronounHim +"self off in the most heroic manner possible for a " + charType + " who was just abused by a " + noun4 + ", and dove, just as heroicly, back into the bush to hide.")
                  print("")
                  time.sleep(1)
                  daysPassed = str(random.randint(10,100))
                  print_slowly("It was " + daysPassed + " days later that our hero arose. Bleary eyed and ready to " + verb4 +  " " + adv3 + ", " + charName + " had never felt better. A little hungry, maybe, but never better.")
                  print("")
                  time.sleep(1)
                  print_slowly("VERY hungry, it seems. In fact, " + charName + " could barely stand. A mix of fatigue, hunger, and missing "+ pronounHis +" Aunt Margerie caused " + charName + " to collapse to the ground, forced to crawl by "+ pronounHis +" hands like an untrained " + noun6 + ".")
                  print("")
                  time.sleep(1)
                  strengthOf = str(random.randint(0,1000))
                  print_slowly("Through sheer willpower, with the strength of " + strengthOf + " " + noun7 + "s, " + charName + " crawled " + adv4 + " through the bushes, hoping, " + verb5 + "ing to find a way out. It was several minutes later that "+ pronounHe +" emerged, whining like an abandoned " + noun8 + ", and saw "+ pronounHis +" salvation: a river, filled with a variety of red fishes. "+ pronounHe.capitalize() +" also noticed some enticing berries bushes several yards away.")
                  print("")
                  
                  choice = None
                  while choice != '1' and choice != '2':
                      choice = sg.popup_get_text('Should ' + charName + ' (1) eat the berries or (2) drink the water?','Please input 1 or 2.')
                  
                  if choice == '1':
                      print_slowly(charName + " moves towards the berries, the dirt sticking under "+ pronounHis +" fingernails like wet " + noun9 + ". With each " + adj9 + " movment, "+ pronounHe +" felt his strength returning, hope filling "+ pronounHim +" with the " + adj10 + " feeling "+ pronounHe +" got whenever "+ pronounHe +" was around Aunt Margerie. Before "+ pronounHe +" knew it, "+ pronounHe +" was upon them. Almost " + verb6 + "ing, " + charName + " reaches for the berries and greedily stuffs them in "+ pronounHis +" mouth. Never before had "+ pronounHe +" fed himself so " + adv5 + ".")
                      print("")
                      time.sleep(1)
                      print_slowly("It was at the climax of this enjoyment that " + charName + " saw something out of the corner of "+ pronounHis +" eye. Something large, and " + noun4 + "like. Through "+ pronounHis +" gluttony and fear," + charName + " had failed to acknowledge the possibility that there could've been more than one " + noun4 + " in this forest. It was as "+ pronounHe +" was stuffing "+ pronounHis +" mouth full with another handfull of berries that the massive, " + adj6 + " " + noun4 + " made it's move. A simple hop and it was in motion.")
                      print("")
                      time.sleep(1)
                      print_slowly("But before the " + noun4 + " could devour it's target, " + charName + " seized up. "+ pronounHis.capitalize() +" eyes bulged, seeming almost to pop out of his face. With a last exhalation and final thoughts of "+ pronounHis +" Auntie, " + charName + " died.")
                      print("")
                      time.sleep(1)
                      print_slowly("The massive, " + adj6 + " " + noun4 + " was left with several minutes to enjoy it's free meal before other massive, " + adj6 + " " + noun4 + "s came along to take some for themselves. Alas, this is the fate of adventurers who step foot in the Forest of the " + noun4.capitalize() + ". And of course, never eat the berries.")
                      print("")
                      time.sleep(3)
                      ending = "Death by berries"
                      storyEnd(title,char,ending)
                  elif choice == '2':
                      print_slowly(charName + " stumbles towards the stream. Thirsty from "+ pronounHis +" " + adj9 + " adventure, " + charName + " " + adv5 + " gulps down the contents of the stream. Minutes pass, and soon, our hero's thirst is satiated. Satisfied, " + charName + " crawls out of the stream and lies down, sopping wet, on the grass.")
                      print("")
                      time.sleep(1)
                      print_slowly("There is silence. Nothing moves around " + charName + ".")
                      print("")
                      time.sleep(2.5)
                      print_slowly("Hmmm. Odd. " + charName + " feels slightly queasy. Probably just gas. It'll pass.")
                      print("")
                      time.sleep(2.5)
                      print_slowly("AUUGH. It has not passed. " + charName + " holds "+ pronounHis +" stomach, wheezing and begging " + adv6 + " like a " + adj10 + " " + noun9 + ".")
                      print("")
                      time.sleep(1)
                      print_slowly(charName + " opened "+ pronounHis +" mouth only to expel the water "+ pronounHe +" had just consumed. Gallons spewed out of "+ pronounHim +", like an uneasy " + noun10 + ". The one difference is that the water did not stop. Out of " + charName + "'s mouth it kept coming. Sometimes the vomitting was interrupted with brief respits, but not enough for " + charName + " to breathe.")
                      print("")
                      time.sleep(1)
                      print_slowly("Even after it seemed like too much fluid had been regurgitated, it still kept coming. And coming. And coming. And still it was coming.")
                      print("")
                      time.sleep(1)
                      print_slowly("It was several minutes later that the water finally ceased it's hazardous flow. The water had stopped. " + charName + ", it seems, had too.")
                      print("")
                      time.sleep(1)
                      print_slowly("A warning as old as literature itself, it seems; beware the red herrings.")
                      time.sleep(3)
                      ending = "Fish-filled fallacy"
                      storyEnd(title,char,ending)
            
            elif choice == 'no' or choice == 'No' or choice == 'n' or choice == 'N':
                print_slowly(charName + " decides to head back the way "+ pronounHe +" came.")
                print("")
                time.sleep(1)
                randsize1 = str(random.randint(20,2000))
                randsize2 = str(random.randint(20,2000))
                randsize3 = str(random.randint(20,2000))
                print_slowly("After several minutes of traveling, " + charName + " comes across a ditch. Well, more of a ravine. About " + randsize1 +" feet across and at least a " + randsize2 + " feet down, this scar on the land stretched for " + randsize3 + " feet in either direction.")
                print("")
                time.sleep(1)
                  
                choice = None
                while choice != 'yes' and choice != 'no' and choice != 'Yes' and choice != 'No' and choice != 'y' and choice != 'n' and choice != 'Y' and choice != 'N':
                    choice = sg.popup_get_text('Should ' + charName + ' attempt to cross the ravine?','Please input yes or no.')
                  
                if choice == 'yes' or choice == 'Yes' or choice == 'y' or choice == 'Y':
                    print_slowly(charName + " tries to cross the ravine by jumping over it. Alas, one should be more careful, especially after such a close call with whatever produced that " + noun2 + "like noise. Like an overly " + adj7 + " " + noun4 + ", " + charName + " plummeted down the ravine to " + pronounHis + " death.")
                    print("")
                    time.sleep(1)
                    print_slowly("If I said that " + charName + " was remebered for " + pronounHis + " " + adj8 + ", I'd be lying. " + charName + " would only be remembered for how " + pronounHe +" went splat like a " + adj8 + " " + noun5 + ". So for all of the " + noun6 + "s out there, remember; watch your step.")
                    print("")
                    time.sleep(3)
                    ending = "Splat goes the weasel"
                    storyEnd(title,char,ending)
                    
                elif choice == 'no' or choice == 'No' or choice == 'n' or choice == 'N':
                    print_slowly(charName + " decides to walk along the ravine for a time, until " + pronounHe +" finds something better to do.")
                    print("")
                    time.sleep(1)
                    print_slowly(charName + " is still walking.")
                    print("")
                    time.sleep(2)
                    print_slowly(charName + " is still walking.")
                    print("")
                    time.sleep(4)
                    print_slowly(charName + " is STILL walking.")
                    print("")
                    time.sleep(1)
                    print_slowly("It seems as if " + charName + "'s estimate that the ravine stretched on for " + randsize3 + " feet was much too short. It still stretched on beyond " + pronounHis + " sight.")
                    print("")
                    time.sleep(2)
                    print_slowly("Still, " + charName + " walked along it's edge. Compelled to do this by the command of some force " + charName + " was unaware of, "+ pronounHe +" would walk the edge of this ravine until the day "+ pronounHe + " died, alone and forgotten like a " + adj7 + " " + noun3 + " who didn't know the difference between a " + noun4 + " and a " + noun5 + ".")
                    print("")
                    time.sleep(3)
                    ending = "As God as my witness"
                    storyEnd(title,char,ending)
                  
#story "The Bible as God Intended"
def story2():
    global textSpeed
    global charType
        
    window = sg.Window("The Bible as God Intended",[[sg.Output(size=(80,20),key='-story-')],
                                                    [sg.Button('Run', bind_return_key=True)]])
    
    
    begin = 1
    while True:
        event, value = window.Read()
        if event == 'EXIT'  or event == sg.WIN_CLOSED:
            window.close()
            break # exit button clicked      
        if event == 'Run' and begin == 1:
            begin = 0
            
            window.Element('-story-')._TKOut.output.bind("<Key>", lambda e: "break")
            
            title = "The Bible as God Intended"
  
            #story
            saveSpeed = textSpeed
            
            #skips color indicator to capitalize charType for title
            charType = charType.capitalize()
             
            #slows text speed for printing the title
            textSpeed = 2 * textSpeed
            print_slowly("The Book of "+charType+"")
            print("")
            textSpeed = saveSpeed
            
            time.sleep(2)
            print_slowly("1. In the beginning God "+verb2+"ed the "+noun1+" and the "+noun2+".")
            print("")
            time.sleep(1)
            print_slowly("2. And the "+noun2+" was without form, and void; and darkness was upon the face of the deep. And the "+noun4+" of God "+verb1+"ed upon the face of the "+noun3+"s.")
            print("")
            time.sleep(1)
            print_slowly("3. And God said, Let there be "+noun5+": and there was "+noun5+".")
            print("")
            time.sleep(1)
            print_slowly("4. And God saw the "+noun5+", that it was "+adj1+": and God "+verb3+"ed the "+noun5+" from the "+noun6+".")
            print("")
            time.sleep(1)
            
            light = sg.popup_get_text('What should God call the '+noun5+"?",'Please input a name.').capitalize()
            time.sleep(1)
            
            darkness = sg.popup_get_text('What should God call the '+noun6+"?",'Please input a name.').capitalize()
            time.sleep(1)
            
            print_slowly("5. And God called the "+noun5+" " + light + ", and the "+noun6+" "+pronounHe+" called " + darkness + ". And the evening and the morning were the first "+noun7+".")
            print("")
            time.sleep(1)
            print_slowly("6. And God said, Let there be a "+noun9+" in the midst of the "+noun3+"s, and let it "+verb4+" the "+noun3+"s from the "+noun3+"s.")
            print("")
            time.sleep(1)
            print_slowly("7. And God made the "+noun8+", and "+verb4+" the "+noun3+"s which were under the "+noun8+" of the "+noun3+"s which were above the "+noun8+": and it was so.")
            print("")
            time.sleep(1)
            
            heaven = sg.popup_get_text('What should God call the '+noun8+"?",'Please input a name.').capitalize()
            time.sleep(1)
            
            randomInterval = random.randint(1,30)
            intervals = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth','twenty-first','twenty-second','twenty-third','twenty-fourth','twenty-fifth','twenty-sixth','twenty-seventh','twenty-eighth','twenty-ninth','thirtieth']
            intervalWord = intervals[randomInterval - 1]
            print_slowly("8. And God called the "+noun8+" "+heaven+". And the evening and the morning were the "+intervalWord+" day.")
            print("")
            time.sleep(1)
            print_slowly("9. And God created existence. It kinda sucked. Not to worry. Soon, everything was gone. And so it was. Amen.")
            print("")
            time.sleep(10)
            
            window.close()
            
            char = "God"
            ending = "Existence"
            storyEnd(title,char,ending)

#chooses random story
def genStory():
  genWords()
  genGender()
  
  
  numStor = 5 #number of stories
  randStor = random.randint(1,numStor) #selects one from the options
  if curStory == "none":
    if randStor == 1:
      story1()
    elif randStor == 2:
      story2()
    elif randStor == 3:
      print("Story 3 - random")
      input()
      mainMenu()
    elif randStor == 4:
      print("Story 4 - random")
      input()
      mainMenu()
    elif randStor == 5:
      print("Story 5 - random")
      input()
      mainMenu()
  elif curStory == 1:
    story1()
  elif curStory == 2:
    story2()
  elif curStory == 3:
    print("Story 3 - selected")
    input()
    mainMenu()
  elif curStory == 4:
    print("Story 4 - selected")
    input()
    mainMenu()
  elif curStory == 5:
    print("Story 5 - selected")
    input()
    mainMenu()

#selects story instead of choosing random one
def storySelect():
  global curStory
  window = sg.Window('Select your story',[[sg.Text("Select a story to experience.")],[sg.Button('The Forest')],[sg.Button('The Bible as God Intended')],[sg.Button('Story 3')],[sg.Button('Story 4')],[sg.Button('Story 5')],[sg.Button('Random')]]).Finalize()
  
  
  while True:
      event, values = window.read()
      if event == "The Forest":
          window.close()
          curStory = 1
          window = sg.Window('Selection: The Forest',[[sg.Text("Your selected story is \"The Forest\".")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == "The Bible as God Intended":
          window.close()
          curStory = 2
          window = sg.Window('Selection: The Bible as God Intended',[[sg.Text("Your selected story is \"The Bible as God Intended\".")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == "Story 3":
          window.close()
          curStory = 3
          window = sg.Window('Selection: Story 3',[[sg.Text("Your selected story is \"Story 3\".")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == "Story 4":
          window.close()
          curStory = 4
          window = sg.Window('Selection: Story 4',[[sg.Text("Your selected story is \"Story 4\".")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == "Story 5":
          window.close()
          curStory = 5
          window = sg.Window('Selection: Story 5',[[sg.Text("Your selected story is \"Story 5\".")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == "Random":
          window.close()
          curStory = None
          window = sg.Window('Selection: Random',[[sg.Text("Your story selection will be random.")],[sg.Button('Main menu')]]).Finalize()
          
          while True:
              event, values = window.read()
              if event == "Main menu":
                  window.close()
                  mainMenu()
              elif event == sg.WIN_CLOSED:
                  window.close()
                  break
      elif event == sg.WIN_CLOSED:
          window.close()
          break

def mainMenu():
    sg.theme('DarkAmber')
    layout = [  [sg.Text('Welcome to Play on Words')],
                [sg.Button('Embark!')],
                [sg.Button('Edit vocab lists')],
                [sg.Button('Select adventure')],
                [sg.Button('Quit')]]

    window = sg.Window('Play on Words', layout).Finalize()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()
            break
        elif event == 'Embark!':
            window.close()
            genStory()
        elif event == 'Edit vocab lists':
            window.close()
            bankEdit()
        elif event == 'Select adventure':
            window.close()
            storySelect()

mainMenu()
