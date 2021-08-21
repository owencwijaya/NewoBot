from stay import keep_alive
from replit import db
import discord
import os
import requests
import json
import random
import addfuncs
import arrays

client = discord.Client()
channel = client.get_channel(758682366264082487)
channel_id = 758682366264082487


#for motivation and such
def quoting():
  res = requests.get("https://zenquotes.io/api/random")
  jsondata = json.loads(res.text)
  quote = jsondata[0]['q'] + " -" + jsondata[0]['a']
  return quote

#main
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    options = arrays.sadge_words
    if "sadge_words" in db.keys():
      options = options + db["sadge_words"]


    suit = arrays.rps
    if "rps" in db.keys():
      suit = suit + db["rps"]


    cursedops = arrays.cursed_links
    if "cursed_links" in db.keys():
      cursedops = cursedops + db["cursed_links"]


    if message.content.lower().startswith('newo punch'):
      await message.channel.send('https://images-ext-2.discordapp.net/external/9Ge0Iho3C0aA6K4ocP2b8_gh6uvjwlhcRmzLNWSpvGA/https/media.discordapp.net/attachments/800041163238408253/814741330474303499/Screen_Recording_20210226-131004_YouTube_1.gif')


    if message.content.lower().startswith('newo wisdom'):
        await message.channel.send(random.choice(options))


    if message.content.lower().startswith('newo kerang ajaib'):
        await message.channel.send(random.choice(arrays.yes_or_no)
        )

    if message.content.lower().startswith('newo suit'):
        await message.channel.send("I choose {}".format(random.choice(suit)))


    if message.content.lower().startswith('newo cursed'):
      cursedQuery = random.choice(cursedops)
      while cursedQuery == " ":
        cursedQuery = random.choice(cursedops)
      if "stuff" in cursedQuery:
        cursedQuery = cursedQuery.split("stuff ", 1)[1]
      await message.channel.send(cursedQuery)


    if message.content.lower().startswith('newo motivate'):
        await message.channel.send(quoting())


    if message.content.lower().startswith("newo add wisdom"):
        wisdom1 = message.content.lower().split("newo add wisdom ", 1)[1]
        if wisdom1 == "":
          await message.channel.send("add what man")
        else:
          addfuncs.addwisdom(wisdom1)
          options = options + db["sadge_words"]
          await message.channel.send("wisdom added ezclap")


    if message.content.lower().startswith("newo add suit"):
        suit1 = message.content.lower().split("newo add suit ", 1)[1]
        if suit1 == "":
          await message.channel.send("add what man")
        else:
          print(suit1)
          addfuncs.addsuit(suit1)
          suit = suit + db["rps"]
          await message.channel.send("suit option added ezclap")


    if message.content.lower().startswith("newo add cursed"):
        cursed1 = message.content.lower().split("newo add cursed", 1)[1]
        if cursed1 == "":
          await message.channel.send("add what man")
        else:
          addfuncs.addcursed(cursed1)
          cursedops = cursedops + db["cursed_links"]
          print(cursedops)
          await message.channel.send("cursed stuffs added. no nsfw pls. pls.")


    if message.content.lower().startswith("ty newo") or message.content.startswith("thank you newo"):
        await message.channel.send(random.choice(arrays.noprobs) + "" + random.choice (arrays.motivate))


    if ("newo" in message.content.lower()) and ("unsee" in message.content.lower()):
        await message.channel.send("here you go")
        await message.channel.send(random.choice(arrays.unseeArray))


    if message.content.lower().startswith("newo choose"):
      condition = message.content.lower().split("newo choose", 1)[1]
      conditionArray = condition.split(", ")
      sentence = random.choice(arrays.chooseArray) + " "+ random.choice(conditionArray)
      await message.channel.send(sentence)


    if message.content.lower().startswith('newo ratecock'):
      ppsize = random.randint(1, 100)
      condition = message.content.lower().split("newo ratecock", 1)[1]
      cockrating = message.author.mention + "'s pp size" + addfuncs.conditioning(condition) + " = " + str(ppsize)  + "/100"
      await message.channel.send(cockrating)


    elif message.content.lower().startswith("newo rate "):
        size = random.randint(1, 100)
        condition = message.content.lower().split("newo rate", 1)[1]
        conditionArray = condition.split(" ")
        isRatingMyself = False
        youArray = ["your", "you", "yourself", "yourselves", "u", "ur", "urself", "urselves"]
        for i in range(len(conditionArray)):
          
          if conditionArray[i].lower() == "my":
            conditionArray[i] = "your"
          elif conditionArray[i].lower() == "i" or conditionArray[i].lower() == "me":
            conditionArray[i] = "you"
          elif conditionArray[i].lower() == "myself":
            conditionArray[i] = "yourselves"
          else:
            for j in range(len(youArray)):
              if conditionArray[i].lower() == youArray[j]:
                isRatingMyself = True

        restOfCondition = ' '.join([(str(x)) for x in conditionArray])
        
        if isRatingMyself == False:
          rating = random.choice(arrays.ratingArray) + restOfCondition + " is " + str(size) + "/100"
          await message.channel.send(rating) 
          if str(size) == "69":
            await message.channel.send("pretty  n i c e  if you ask me")
        else:
          await message.channel.send("how am i supposed to rate myself")


    if message.content.lower().startswith('newo google'):
      query = message.content.lower().split("newo google", 1)[1]
      queryList = query.split(" ")
      joinedQuery = "+".join([str(x) for x in queryList])[1:]
      results = "https://www.google.com/search?&q=" + joinedQuery
      embed = discord.Embed(title = "Here's your search regarding '{}'".format(query[1:]), url = results, description = "Hopefully this helps.", color = discord.Color.green())
      await message.channel.send(embed = embed)


    if message.content.lower().startswith('newo mock'):
      query = list(message.content.lower().split("newo mock ", 1)[1])
      for i in range(len(query)):
        if i % 2 != 0 and query[i] != " ":
          query[i] = chr(ord(query[i]) - 32)
      await message.channel.send("".join(query))


    if message.content.lower().startswith("newo help"):
      await message.channel.send(embed = addfuncs.help())



keep_alive()
client.run(os.getenv('TOKEN'))
