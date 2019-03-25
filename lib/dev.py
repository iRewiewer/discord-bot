from random import shuffle, randint

#-----------------------------------------------------------------------------------------------------------#

def help_dev():
    return """```[===============================================][Dev Section][===============================================]

    -say <msg> - Make the bot say <msg> while deleting your message

    -del <number> - delete <number> messages

    -status - change the bot's status

    

[=================================================][Page DEV][=================================================]```"""

#-----------------------------------------------------------------------------------------------------------#

def status(client):
    #Mandatory Variables
    guilds = len(list(client.servers))
    
    #Status Section
    statuses = [
        " for " + str(guilds) + " Guilds!",
        " with your feelings",
        " ASYNC",
        " PEP8 Formatting",
        " with time and space",
        " Blackjack",
        " with services",
        " Playing",
        " spoopy music",
        " death metal"
    ]
    
    var = randint(0, len(statuses) - 1 )
    
    return statuses[var]

#-----------------------------------------------------------------------------------------------------------#

#elif message.content.lower().startswith("-del"):
#        nr = message.content.lower().split(' ')
        
#        async for msg in client.logs_from(message.channel, limit = int(nr[1]) + 1):
#            await client.delete_message(msg)
#            await asyncio.sleep(0.4)

#-----------------------------------------------------------------------------------------------------------#

#elif message.content.lower().startswith("-say"):
        
#        userMention = message.content.split(' ')
#        msg = ""
        
#        await client.delete_message(message)
        
#        for c in range(1, len(userMention)):
#            msg += userMention[c]
#            msg += " "
                
#        await client.send_message(message.channel, msg)