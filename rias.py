#Libraries

import asyncio
import discord
import youtube_dl

from random import shuffle, randint

from lib import help1 as h1
from lib import help2 as h2
from lib import help3 as h3
from lib import dev

#-----------------------------------------------------------------------------------------------------------#

#Global Variables

client = discord.Client()

#-----------------------------------------------------------------------------------------------------------#

#Startup

@client.event
async def on_ready():
    
    print("[-------------------------------------]")
    
    print(" Hi, I'm @" + client.user.name + "#" + client.user.discriminator + " nice to meet you!")
    
    print("[-------------------------------------]")
    
    await client.change_presence(game = discord.Game(name = dev.status(client)))

#-----------------------------------------------------------------------------------------------------------#

#Master Function

@client.event
async def on_message(message):
    
#-----------------------------------------------------------------------------------------------------------#

#Variables

    userDisplayName = message.author.display_name
    userDiscrim = message.author.discriminator
    
#-----------------------------------------------------------------------------------------------------------#

#Help Section

    if message.content.lower().startswith("-help"):
        
        print("")
        print("----Start Command----")
        print("Function Code: help")
        
        args = message.content.lower().split(' ')
        
        if message.content.lower() != "-help": page = args[1]
        else: page = "1"

        if page == "dev": await client.send_message(message.channel, str(dev.help_dev()))
        elif page == "1": await client.send_message(message.channel, str(h1.help_1()))
        elif page == "2": await client.send_message(message.channel, str(h2.help_2()))
        elif page == "3": await client.send_message(message.channel, str(h3.help_3()))
        else:
            await client.send_message(message.channel, "Invalid Argument!")
            print("@" + userDisplayName + "#" + userDiscrim + " used an invalid argument!")
            
        print("@" + userDisplayName + "#" + userDiscrim + " executed '" + message.content + "'")
        print("-----End Command-----")
        print("")

#-----------------------------------------------------------------------------------------------------------#

#Help 1

    elif message.content.lower().startswith("-ping"):

        print("")
        print("----Start Command----")
        print("Function Code: ping")
        
        pong = str(h1.ping(message))
        
        await client.send_message(message.channel, pong)
        
        print("@" + userDisplayName + "#" + userDiscrim + " executed '" + message.content + "' and got " + pong[14:] + ".")
        
        print("-----End Command-----")
        print("")

                            #-------------------------------------------#
        
        
    elif message.content.lower().startswith("-joke"):
        
        print("")
        print("----Start Command----")
        print("Function Code: joke")
        
        joke = str(h1.joke())
        
        await client.send_message(message.channel, joke[1:])
        
        print("@" + userDisplayName + "#" + userDiscrim, "executed " + message.content + " and got joke '" + joke[0:1] + "'.")
        
        print("-----End Command-----")
        print("")
        
                            #-------------------------------------------#
        
    elif message.content.lower().startswith("-roll") or message.content.lower().startswith("-dice"):
        
        print("")
        print("----Start Command----")
        print("Function Code: dice")
        
        dice = str(h1.dice(message))
        
        if dice == "no dice":
            await client.send_message(message.channel, "You haven't specified a dice!")
            print("@" + userDisplayName + "#" + userDiscrim, " didn't specify a dice.")
            
        elif dice == "wrong dice":
            await client.send_message(message.channel, "That's not an available dice!")
            print("@" + userDisplayName + "#" + userDiscrim, " used an invalid dice.")
        else:
            if dice == "∞": await client.send_message(message.channel, "You've just rolled ∞. And got away with it.")
            else: await client.send_message(message.channel, "You've just rolled a " + str(dice) + "!")
        
            print("@" + userDisplayName + "#" + userDiscrim, "executed " + message.content + " and got '" + dice + "'.")
        
        print("-----End Command-----")
        print("")
        
                            #-------------------------------------------#

    elif message.content.lower().startswith("-avatar"):

        print("")
        print("----Start Command----")
        print("Function Code: avatar")
        
        usr = h1.avatar(message)
        
        if usr == "many args":
            await client.send_message(message.channel, "Too many arguments!")
            print("@" + userDisplayName + "#" + userDiscrim, "used too many arguments.")
        
        elif usr == "no args":
            print("@" + userDisplayName + "#" + userDiscrim, "didn't have enough arguments.")
            await client.send_message(message.channel, "Not enough arguments.")

        elif usr is None:
            print("@" + userDisplayName + "#" + userDiscrim, "didn't mention.")
            await client.send_message(message.channel, "You didn't @mention anyone.")
            
        else:
            await client.send_message(message.channel, usr.avatar_url)
            print("@" + userDisplayName + "#" + userDiscrim, "executed -avatar on @" + usr.display_name + "#" + usr.discriminator + ".")
            
        print("-----End Command-----")
        print("")
        
                            #-------------------------------------------#

    elif message.content.lower().startswith("@random"):
        
        print("")
        print("----Start Command----")
        print("Function Code: random")
        
        user = h1.random(message)
        
        await client.send_message(message.channel, "{}".format(user.mention))
        
        print("@" + userDisplayName + "#" + userDiscrim, " executed " + message.content + " and mentioned @" + str(user) + ".")
        
        print("-----End Command-----")
        print("")

                            #-------------------------------------------#

    elif message.content.lower().startswith("-google"):
        
        print("")
        print("----Start Command----")
        print("Function Code: google")
        
        await client.send_message(message.channel, h1.google(message))
        
        print("@" + userDisplayName + "#" + userDiscrim, " executed " + message.content + ".")
        
        print("-----End Command-----")
        print("")
        
#-----------------------------------------------------------------------------------------------------------#

#Help 2

    elif message.content.lower().startswith("-role") and "-roles" not in message.content.lower():
        
        print("")
        print("----Start Command----")
        
        print("@" + userDisplayName + "#" + userDiscrim + " executed " + message.content + ".")
        
        print("-----End Command-----")
        print("")
    
    #if message.content.lower().startswith("-lfg"):
        #h2.lfg(message)
        
#-----------------------------------------------------------------------------------------------------------#

#Help 3

    #if message.content.lower().startswith("-music"):
        #h3.music(message)

#-----------------------------------------------------------------------------------------------------------#
    
#Help Dev
    
    elif message.content.lower().startswith("-status"):
    
        print("")
        print("----Start Command----")
        print("Function Code: status")     
        
        await client.change_presence(game = discord.Game(name = dev.status(client)))
        
        print("@" + userDisplayName + "#" + userDiscrim, " executed " + message.content + ".")  
        print("-----End Command-----")
        print("")
        
#-----------------------------------------------------------------------------------------------------------#

#Client Run

client.run('secret token :p')

#-----------------------------------------------------------------------------------------------------------#