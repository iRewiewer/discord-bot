def help_3():
    return """```[===============================================][Help Section][===============================================]

    -music - Play music straight from YouTube.

    Subcommands of -music:
        -music add <link> - Add a youtube song link to the Queue.
        -music remove <link> - Remove a certain song from the Queue.
        -music list - View the current Queue.
        -music clear - Clear the current Queue.
        -music join - Tell the bot to join your channel in order to play music
        -music leave - Tell the bot to leave your channel.
        -music play - Play music from the current Queue.
        -music shuffle - Shuffle the current Queue.
        -music skip - Skip the current song.

[=================================================][Page 3/3][=================================================]```"""

#-----------------------------------------------------------------------------------------------------------#

#        global queue
        
#        args = message.content.lower().split(' ')
        
#        arg = args[1]
        
#        if arg == "add":
#            link = args[2]
#            queue.append(link)
        
#        elif arg == "remove":
#            link = args[2]
#            queue.remove(link)
        
#        elif arg == "list":
#            if not queue:
#                await client.send_message(message.channel, "- The Queue is empty -")
#            else:
#                await client.send_message(message.channel, queue)
        
#        elif arg == "clear":
#            queue = []
        
#        elif arg == "join":
#            await client.join_voice_channel(message.author.voice.voice_channel)
        
#        elif arg == "leave":
#            server = message.server
#            voice_client = client.voice_client_in(server)
#            await voice_client.disconnect()
            
#        elif arg == "play": #SOLO PLAYER - NO QUEUE FUNCTIONALITY ADDED - USE -music play <link>
#            link = args[2]
#            server = message.server
            
#            voice_client = client.voice_client_in(server)
#            player = await voice_client.create_ytdl_player(link)
            
#            player.start()
        
#        elif arg == "shuffle":
#            shuffle(queue)
        
#        elif arg == "skip":
#            pass  