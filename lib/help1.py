from random import shuffle, randint

#-----------------------------------------------------------------------------------------------------------#

def help_1():
    return """```[===============================================][Help Section][===============================================]

    -help <page> - Displays corresponding help page.

    -ping - Check your ping!

    -avatar <name> - Check out someone's profile picture without having to download it and zoom in.

    -roll <dice> - Roll a D4 / D6 / D8 / D10 / D100 / D12 / D20 / D∞ dice.

    -joke - Tell a joke!

    @random - Mention a random person.
    
    -google <something> - Get the first 5 google results!

[=================================================][Page 1/3][=================================================]```"""

#-----------------------------------------------------------------------------------------------------------#

def ping(message):
    return "Your ping is: " + str(randint(20,200))

#-----------------------------------------------------------------------------------------------------------#

def joke():
        rand = randint(0,9);
        
        jokes = {
            0:"Why did the chicken cross the road?\nTo get to the other side.",
            1:"Why do keyboards work 24/7?\nBecause they have two shifts.",
            2:"What days do fish dislike the most?\nFry-Days!.",
            3:"I don't know. You tell me.",
            4:"What kind of music is a balloon scared of?\nPop music.",
            5:"What do you call the security outside of a Samsung Store?\nGuardians of the Galaxy.",
            6:"Want a bad joke?\nLook in the mirror.",
            7:"What do you call a bee that was born is the United States?\nA USB.",
            8:"What do you call a cow in an earthquake?\nA milkshake.",
            9:"Where do animals go when their tails fall off?\nThe retail store.",
        }
        
        return str(rand) + jokes[rand]

#-----------------------------------------------------------------------------------------------------------#

def dice(message):
        if message.content.lower() == "-roll" or message.content.lower() == "-dice": return "no dice"
        else: dice = message.content.lower().split(' ')
        
        if dice[1] == "d4": roll = randint(1, 4)
        elif dice[1] == "d6": roll = randint(1, 6)
        elif dice[1] == "d8": roll = randint(1, 8)
        elif dice[1] == "d10": roll = randint(1, 10)
        elif dice[1] == "d100": roll = randint(1, 10) * 10
        elif dice[1] == "d12": roll = randint(1, 12)
        elif dice[1] == "d20": roll = randint(1, 20)
        elif dice[1] == "d∞": roll = "∞"
        else: return "wrong dice"
    
        #D4 / D6 / D8 / D10 / D00 / D12 / D20 / D∞
        
        return roll

#-----------------------------------------------------------------------------------------------------------#

def avatar(message):
    
    args = message.content.split(' ')
    
    if len(args) > 2: return "many args"
    elif len(args) == 1: return "no args"
    else:
        for member in message.mentions:
            return member         
        
#-----------------------------------------------------------------------------------------------------------#

def random(message):
    mem = [""]
        
    for i in message.channel.server.members:
        mem.append(i)
            
    shuffle(mem)
    
    return mem[1]
        
#-----------------------------------------------------------------------------------------------------------#

def google(message):
    url = message.content.lower()
    url = url[8:]
    
    k = 0

    msg = ""
    
    for j in search(url, tld="com", num=5, stop=1, pause=2):
        if k == 0:
            k += 1
            msg += "Here are your results:\n"
            
        msg += "<" + j + ">\n"
    
    if k == 0:
        msg = "No results found! :("
    
    return msg