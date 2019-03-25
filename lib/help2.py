def help_2():
    return """```[===============================================][Help Section][===============================================]

    -role <role> - Make your name colorful by self-assigning a role with the desired color's name.

    #Supported Colors: (dark_)green, (dark_)blue, (dark_)purple, (dark_)pink, (dark_)yellow, (dark_)orange, (dark_)red, 
    (dark_)gray, black, white

    -lfg - Looking for group feature.

    #Subcommands of -lfg:
        -lfg <game> - Find a party for <game>. When there are enough people to form a full party or the start command has been 
        issued, yourself and the party members will automatically join a temporary voice channel which will be deleted once the 
        party has been disbanded or once every member has left the channel.
    
        -lfg create <game> - Create a party for <game>
    
        -lfg start - Mark the party as ready and get right into it.
    
        -lfg disband - Disband the party immediately.
    
        -lfg list - List all active parties.
        
        -lfg leave - Leave the party.

    [=================================================][Page 2/3][=================================================]```"""

#-----------------------------------------------------------------------------------------------------------#

"""def role(message):        
        args = message.content.lower().split(' ')
        role = ""
        
        if len(args) > 1:
            
            role = args[1]

            matches = [x for x in message.server.roles if x.name.lower() == role.lower()] 
            
            if matches:
                if "Admin" not in matches[0].name:
                    
                    await client.add_roles(message.author, matches[0])
                    await client.send_message(message.channel, "Role '" + str(matches[0]) + "' assigned successfully.")
                    
                    print("Assigned " + str(matches[0]) + " to @" + userDisplayName + "#" + userDiscrim + ".")
                
                else:
                    await client.send_message(message.channel, "Nice try. Insufficient permissions tho.")
                    
                    print("@" + userDisplayName + "#" + userDisplayName + " has insufficient permissions for " + str(matches[0]))
                    
            else:
                await client.send_message(message.channel, "That role doesn't exist. Use \"-roles\" to see the available roles for you.")

                print("@" + userDisplayName + "#" + userDisplayName + " specified a non-existent role.")
        
        else:
            await client.send_message(message.channel, "You didn't specify a role. Use \"-roles\" to see the available roles for you.")
            
            print("@" + userDisplayName + "#" + userDiscrim + " didn't specify a role at all.")"""