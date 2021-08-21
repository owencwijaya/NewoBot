#for motivation and such
from replit import db

import discord
import os
import requests
import json
import random

def quoting():
  res = requests.get("https://zenquotes.io/api/random")
  jsondata = json.loads(res.text)
  quote = jsondata[0]['q'] + " -" + jsondata[0]['a']
  return quote

#addWisdom
def addwisdom(mssg):
  if "sadge_words" in db.keys():
    wisdom = db["sadge_words"]
    wisdom.append(mssg)
    db["sadge_words"] = wisdom
  else:
    db["sadge_words"] = [mssg]
  
#add suit options
def addsuit(mssg):
  if "rps" in db.keys():
    suit_ops = db["rps"]
    suit_ops.append(mssg)
    db["rps"] = suit_ops
  else:
    db["rps"] = [mssg]

#add cursed messages
def addcursed(mssg):
  if "cursed_links" in db.keys():
      cursed_ops = db["cursed_links"]
      cursed_ops.append(mssg)
      db["cursed_links"] = cursed_ops
  else:
      db["cursed_links"] = [mssg]

def help():
  embed = discord.Embed(title = "Hi, I'm NewoBot.", description = "I'm a bot serving in this dumptruck fire of a server called STEI Empayer. I hold account of the history and the shitposts this place have seen. I honestly have no clue what I am, but I do these: \n\n\n\n - newo wisdom = I will send a wisdom for God knows why. These wisdoms are either from my father or from you guys. \n\n - newo kerang ajaib = I'm the magic shell. \n\n - newo suit = A simple rock-paper-scissors game but with a little twist to it. \n\n - newo cursed = I will send one of the cursed memes from my stash. \n\n - newo motivate = I will send a motivating message. So much for a weird bot. \n\n - newo ratecock <optional: condition> = I will, for God knows why, rate your cock. \n\n - newo rate <condition> = I will rate the condition you want me to rate. Probably. \n\n -newo choose <insert options with commas inbetween> = I'd choose something for your indecisive self. \n\n  - newo google <something> = for y'all who asks about something but don't bother to Google it first because your browser stopped working, now I can Google it for you. You'd still need your browser, though. \n\n\n\n You can also participate in the cursery by using these syntaxes: \n\n - newo add cursed <link>, newo add suit/newo add wisdom <message> will instantly add your item to my database.", color = discord.Color.green())
  return embed

def conditioning(condition):
  conditionArray = condition.split(" ")
  youArray = ["your", "you", "yourself", "yourselves", "u", "ur", "urself", "urselves"]
  for i in range(len(conditionArray)):
    if conditionArray[i].lower() == "my":
      conditionArray[i] = "their"
    elif conditionArray[i].lower() == "i":
      conditionArray[i] = "they"
    elif conditionArray[i].lower() == "me":
      conditionArray[i] = "them"
    elif conditionArray[i].lower() == "myself":
      conditionArray[i] = "themselves"
  newCondition = ' '.join([(str(x)) for x in conditionArray])
  return newCondition