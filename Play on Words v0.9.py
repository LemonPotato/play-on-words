"""
Adlib story generator

Licensed under MIT license
(c) Nathan Paul Peterson 2021
"""

import PySimpleGUI as sg
import random
import os
import time
import sys

verbBank = ['Run','Walk','Swim','Write','Climb']
usedVerbs = ['']
nounBank = ['Cat','Sock','Ship','Monkey','Cabbage']
usedNouns = ['']
adjBank = ['Bashful','Beautiful','Meaningless','Hungry','Pretty']
usedAdjs = ['']
advBank = ['Securely','Sadly','Clumsily','Badly','Diligently']
usedAdvs = ['']

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
    usedNouns = []
  
  if not verbBank:
    verbBank = ['Run','Walk','Swim','Write','Climb']
    usedVerbs = []
  
  if not adjBank:
    adjBank = ['Bashful','Beautiful','Meaningless','Hungry','Pretty']
    usedAdjs = []
  
  if not advBank:
    advBank = ['Fastly','Sadly','Clumsily','Badly','Diligently']
    usedAdvs = []

#class for colored text
class bcolors:
    RED = '\x1b[0;0;31m'
    BLUE = '\x1b[0;0;34m'
    GREEN = '\x1b[0;0;32m'
    END = '\x1b[0m'

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
    elif c == '/':

    elif c == '{':

    elif c == ']':
    
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
  window.Maximize()
  
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
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          window.Maximize()
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
                    window.Maximize()
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
                    window.Maximize()
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
                     window.Maximize()
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
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          window.Maximize()
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
                    window.Maximize()
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
                    window.Maximize()
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
                     window.Maximize()
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
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          window.Maximize()
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
                    window.Maximize()
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
                    window.Maximize()
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
                     window.Maximize()
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
                              [sg.Button("Remove words")],
                              [sg.Button("View words")],
                              [sg.Button("Return to bank edit")]]).Finalize()
          window.Maximize()
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
                    window.Maximize()
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
                    window.Maximize()
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
                     window.Maximize()
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
  print_slowly("Story: " + title)
  time.sleep(0.5)
  print_slowly("Character: " + char)
  time.sleep(0.5)
  print_slowly("Ending: " + "'" + ending + "'")
  time.sleep(3)
  print("")
  print("")
  print_slowly("Press enter to return to the main menu.")
  input()
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
    pronounHe = '{he]'
    pronounHis = '{his]'
    pronounHim = '{him]'
  else:
    pronounHe = '{she]'
    pronounHis = '{her]'
    pronounHim = '{her]'

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
  elif not nounBank:
    charType = random.choice(usedNouns)
  
  #nouns
  if nounBank:
    noun1 = random.choice(nounBank)
    nounBank.remove(noun1)
    usedNouns.append(noun1)
  elif not nounBank:
    noun1 = random.choice(usedNouns)
  
  if nounBank:
    noun2 = random.choice(nounBank)
    nounBank.remove(noun2)
    usedNouns.append(noun2)
  elif not nounBank:
    noun2 = random.choice(usedNouns)
    
  if nounBank:
    noun3 = random.choice(nounBank)
    nounBank.remove(noun3)
    usedNouns.append(noun3)
  elif not nounBank:
    noun3 = random.choice(usedNouns)
  
  if nounBank:
    noun4 = random.choice(nounBank)
    nounBank.remove(noun4)
    usedNouns.append(noun4)
  elif not nounBank:
    noun4 = random.choice(usedNouns)
  
  if nounBank:
    noun5 = random.choice(nounBank)
    nounBank.remove(noun5)
    usedNouns.append(noun5)
  elif not nounBank:
    noun5 = random.choice(usedNouns)
  
  if nounBank:
    noun6 = random.choice(nounBank)
    nounBank.remove(noun6)
    usedNouns.append(noun6)
  elif not nounBank:
    noun6 = random.choice(usedNouns)
  
  if nounBank:
    noun7 = random.choice(nounBank)
    nounBank.remove(noun7)
    usedNouns.append(noun7)
  elif not nounBank:
    noun7 = random.choice(usedNouns)
  
  if nounBank:
    noun8 = random.choice(nounBank)
    nounBank.remove(noun8)
    usedNouns.append(noun8)
  elif not nounBank:
    noun8 = random.choice(usedNouns)
  
  if nounBank:
    noun9 = random.choice(nounBank)
    nounBank.remove(noun9)
    usedNouns.append(noun9)
  elif not nounBank:
    noun9 = random.choice(usedNouns)
  
  if nounBank:
    noun10 = random.choice(nounBank)
    nounBank.remove(noun10)
    usedNouns.append(noun10)
  elif not nounBank:
    noun10 = random.choice(usedNouns)
  
  
  
  #verbs
  if verbBank:
    verb1 = random.choice(verbBank)
    verbBank.remove(verb1)
    usedVerbs.append(verb1)
  elif not verbBank:
    verb1 = random.choice(usedVerbs)
  
  if verbBank:
    verb2 = random.choice(verbBank)
    verbBank.remove(verb2)
    usedVerbs.append(verb2)
  elif not verbBank:
    verb2 = random.choice(usedVerbs)
    
  if verbBank:
    verb3 = random.choice(verbBank)
    verbBank.remove(verb3)
    usedVerbs.append(verb3)
  elif not verbBank:
    verb3 = random.choice(usedVerbs)
  
  if verbBank:
    verb4 = random.choice(verbBank)
    verbBank.remove(verb4)
    usedVerbs.append(verb4)
  elif not verbBank:
    verb4 = random.choice(usedVerbs)
  
  if verbBank:
    verb5 = random.choice(verbBank)
    verbBank.remove(verb5)
    usedVerbs.append(verb5)
  elif not verbBank:
    verb5 = random.choice(usedVerbs)
  
  if verbBank:
    verb6 = random.choice(verbBank)
    verbBank.remove(verb6)
    usedVerbs.append(verb6)
  elif not verbBank:
    verb6 = random.choice(usedVerbs)
  
  if verbBank:
    verb7 = random.choice(verbBank)
    verbBank.remove(verb7)
    usedVerbs.append(verb7)
  elif not verbBank:
    verb7 = random.choice(usedVerbs)
  
  if verbBank:
    verb8 = random.choice(verbBank)
    verbBank.remove(verb8)
    usedVerbs.append(verb8)
  elif not verbBank:
    verb8 = random.choice(usedVerbs)
  
  if verbBank:
    verb9 = random.choice(verbBank)
    verbBank.remove(verb9)
    usedVerbs.append(verb9)
  elif not verbBank:
    verb9 = random.choice(usedVerbs)
  
  if verbBank:
    verb10 = random.choice(verbBank)
    verbBank.remove(verb10)
    usedVerbs.append(verb10)
  elif not verbBank:
    verb10 = random.choice(usedVerbs)


  #adjectives
  if adjBank:
    adj1 = random.choice(adjBank)
    adjBank.remove(adj1)
    usedAdjs.append(adj1)
  elif not adjBank:
    adj1 = random.choice(usedAdjs)
  
  if adjBank:
    adj2 = random.choice(adjBank)
    adjBank.remove(adj2)
    usedAdjs.append(adj2)
  elif not adjBank:
    adj2 = random.choice(usedAdjs)
    
  if adjBank:
    adj3 = random.choice(adjBank)
    adjBank.remove(adj3)
    usedAdjs.append(adj3)
  elif not adjBank:
    adj3 = random.choice(usedAdjs)
  
  if adjBank:
    adj4 = random.choice(adjBank)
    adjBank.remove(adj4)
    usedAdjs.append(adj4)
  elif not adjBank:
    adj4 = random.choice(usedAdjs)
  
  if adjBank:
    adj5 = random.choice(adjBank)
    adjBank.remove(adj5)
    usedAdjs.append(adj5)
  elif not adjBank:
    adj5 = random.choice(usedAdjs)
  
  if adjBank:
    adj6 = random.choice(adjBank)
    adjBank.remove(adj6)
    usedAdjs.append(adj6)
  elif not adjBank:
    adj6 = random.choice(usedAdjs)
  
  if adjBank:
    adj7 = random.choice(adjBank)
    adjBank.remove(adj7)
    usedAdjs.append(adj7)
  elif not adjBank:
    adj7 = random.choice(usedAdjs)
  
  if adjBank:
    adj8 = random.choice(adjBank)
    adjBank.remove(adj8)
    usedAdjs.append(adj8)
  elif not adjBank:
    adj8 = random.choice(usedAdjs)
  
  if adjBank:
    adj9 = random.choice(adjBank)
    adjBank.remove(adj9)
    usedAdjs.append(adj9)
  elif not adjBank:
    adj9 = random.choice(usedAdjs)
  
  if adjBank:
    adj10 = random.choice(adjBank)
    adjBank.remove(adj10)
    usedAdjs.append(adj10)
  elif not adjBank:
    adj10 = random.choice(usedAdjs)


  #adverbs
  if advBank:
    adv1 = random.choice(advBank)
    advBank.remove(adv1)
    usedAdvs.append(adv1)
  elif not advBank:
    adv1 = random.choice(usedAdvs)
  
  if advBank:
    adv2 = random.choice(advBank)
    advBank.remove(adv2)
    usedAdvs.append(adv2)
  elif not advBank:
    adv2 = random.choice(usedAdvs)
    
  if advBank:
    adv3 = random.choice(advBank)
    advBank.remove(adv3)
    usedAdvs.append(adv3)
  elif not advBank:
    adv3 = random.choice(usedAdvs)
  
  if advBank:
    adv4 = random.choice(advBank)
    advBank.remove(adv4)
    usedAdvs.append(adv4)
  elif not advBank:
    adv4 = random.choice(usedAdvs)
  
  if advBank:
    adv5 = random.choice(advBank)
    advBank.remove(adv5)
    usedAdvs.append(adv5)
  elif not advBank:
    adv5 = random.choice(usedAdvs)
  
  if advBank:
    adv6 = random.choice(advBank)
    advBank.remove(adv6)
    usedAdvs.append(adv6)
  elif not advBank:
    adv6 = random.choice(usedAdvs)
  
  if advBank:
    adv7 = random.choice(advBank)
    advBank.remove(adv7)
    usedAdvs.append(adv7)
  elif not advBank:
    adv7 = random.choice(usedAdvs)
  
  if advBank:
    adv8 = random.choice(advBank)
    advBank.remove(adv8)
    usedAdvs.append(adv8)
  elif not advBank:
    adv8 = random.choice(usedAdvs)
  
  if advBank:
    adv9 = random.choice(advBank)
    advBank.remove(adv9)
    usedAdvs.append(adv9)
  elif not advBank:
    adv9 = random.choice(usedAdvs)
  
  if advBank:
    adv10 = random.choice(advBank)
    advBank.remove(adv10)
    usedAdvs.append(adv10)
  elif not advBank:
    adv10 = random.choice(usedAdvs)
  
  
  #convert all words to lowercase
  charType = '[' + charType.lower() + ']'
  
  
  noun1 = '[' + noun1.lower() + ']'
  noun2 = '[' + noun2.lower() + ']'
  noun3 = '[' + noun3.lower() + ']'
  noun4 = '[' + noun4.lower() + ']'
  noun5 = '[' + noun5.lower() + ']'
  noun6 = '[' + noun6.lower() + ']'
  noun7 = '[' + noun7.lower() + ']'
  noun8 = '[' + noun8.lower() + ']'
  noun9 = '[' + noun9.lower() + ']'
  noun10 = '[' + noun10.lower() + ']'
  
  verb1 = '[' + verb1.lower() + ']'
  verb2 = '[' + verb2.lower() + ']'
  verb3 = '[' + verb3.lower() + ']'
  verb4 = '[' + verb4.lower() + ']'
  verb5 = '[' + verb5.lower() + ']'
  verb6 = '[' + verb6.lower() + ']'
  verb7 = '[' + verb7.lower() + ']'
  verb8 = '[' + verb8.lower() + ']'
  verb9 = '[' + verb9.lower() + ']'
  verb10 = '[' + verb10.lower() + ']'
  
  adj1 = '[' + adj1.lower() + ']'
  adj2 = '[' + adj2.lower() + ']'
  adj3 = '[' + adj3.lower() + ']'
  adj4 = '[' + adj4.lower() + ']'
  adj5 = '[' + adj5.lower() + ']'
  adj6 = '[' + adj6.lower() + ']'
  adj7 = '[' + adj7.lower() + ']'
  adj8 = '[' + adj8.lower() + ']'
  adj9 = '[' + adj9.lower() + ']'
  adj10 = '[' + adj10.lower() + ']'
  
  adv1 = '[' + adv1.lower() + ']'
  adv2 = '[' + adv2.lower() + ']'
  adv3 = '[' + adv3.lower() + ']'
  adv4 = '[' + adv4.lower() + ']'
  adv5 = '[' + adv5.lower() + ']'
  adv6 = '[' + adv6.lower() + ']'
  adv7 = '[' + adv7.lower() + ']'
  adv8 = '[' + adv8.lower() + ']'
  adv9 = '[' + adv9.lower() + ']'
  adv10 = '[' + adv10.lower() + ']'

#story "The Bible as God Intended"
def story2():
    global textSpeed
    global charType
        
    window = sg.Window("The Bible as God Intended",[[sg.Output(size=(80,20),key='-story-')],
                                                    [sg.Button('Run', bind_return_key=True)]]).Finalize()
    window.Maximize()
    
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
            charType = charType[:1] + charType[1].swapcase() + charType[2:]
             
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
        
    
    

#chooses random story
def genStory():
  genWords()
  genGender()
  
  if curStory == "none":
    numStor = 5 #number of stories
    randStor = random.randint(1,numStor) #selects one from the options
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
  window.Maximize()
  
  while True:
      event, values = window.read()
      if event == "The Forest":
          window.close()
          curStory = 1
          window = sg.Window('Selection: The Forest',[[sg.Text("Your selected story is \"The Forest\".")],[sg.Button('Main menu')]]).Finalize()
          window.Maximize()
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
          window.Maximize()
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
          window.Maximize()
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
          window.Maximize()
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
          window.Maximize()
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
          window.Maximize()
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
    window.Maximize()
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