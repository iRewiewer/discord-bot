## Introduction
This is my discord chatbot project written in Python3 as part of the year 1 tasks using [Discord.py](https://github.com/Rapptz/discord.py). If you'd like to check out the code, please click on the "View on Github" button above.


## Features
* Roll a dice! Dices available: D4 / D6 / D8 / D10 / D100 / D12 / D20 / D∞
* Have the bot tell a joke. It's funny, I promise!
* Image manipulation! Crop out a friend's profile picture over a chicken body!
* Music player. It's kind of mandatory in 2018, so here you go.
* Looking for Group feature. Automagically create temporary parties & voice channels for your favorite games.
* Ultra super secret dev commands! For admins with a good sense of humor.
* Natural Language interpreter! Talk casually with the bot and have it say totally unrelated things.
* Ever changing 'Playing..' status.
* And more!

### Dice Example
![Dice](https://i.imgur.com/dRtn0ok.png "Dice")
### Joke Example
![Joke](https://i.imgur.com/fmkBFyI.png "Joke")
  
  
## The Journey
"What started out as a simple university year 1 chatbot project turned out to be one of the most popular discord bots out there". 
That would the opening line if it were true. While it is true that this discord bot started as a chatbot project, right from the beginning I wanted to have a long lasting piece of software, not just get marked, get a grade and completely forget about it. I wanted to make a bot that would have a bunch of functionalities that would prove to be both useful and entertaining for its users. To be honest, I think I’m on the right path, having designed the bot with the discord community in mind while still bearing the marking criteria in mind, I am confident that with a little bit more polish I could very well get the bot running and publish it to the people. 
  
  
## Design
Having worked on the bot for about 4 weeks, I have already went through 1 complete rewrite of the code, a total restructure of the filesystem and successfully implemented 26 working commands with a variety of functions. From simply rolling a dice to organising parties with temporary voice & text channels to playing music YouTube to just having the bot tell a lame joke, or as the project “chatbot” theme suggests, natural language interpretation. For features like the YouTube integration where I’m using the [youtube_dl](https://rg3.github.io/youtube-dl/) solution to get the videos from YouTube and [FFMPEG](https://www.ffmpeg.org/) to stream the audio to voice channel the bot is connected to, I’m only going to need to polish them so that they have a good scalability in case the bot actually gets popular and will have to handle big amounts of data at a time.  
  
  
## Past
For the past 4 years I’ve mainly programmed in C++ without the use of any libraries so I could say I have some considerable algorithmic knowledge by having to learn all sorts of stuff and rewriting, adapting and optimising them each time I needed them. A few examples would probably be the classic sorting algorithms (Bubble, Insertion, Merge, Quicksort), Greedy, Divide Et Impera, BFS, DFS, Lee, Dijkstra, Floyd Warshall, Euclid Extended, and many unnamed others. I’ve also dabbled a bit into language learning and tried getting into Lua, C#, Java, JavaScript & Ruby, so when it came down to learning Python, it was a piece of cake.
  
  
## The Teamwork Experience
At the end of the day, this was a team project, and as such we have set up a few ways of working and communicating together – a discord server for the team where we discuss, ask for help from fellow team mates and test out our bots and an azure dev ops team where we managed our work with weekly sprints.  

![Image](https://i.imgur.com/XiQDUyx.png "img")  

We’ve also estimated the time & effort for each task using the [Planning Poker](https://www.planningpoker.com/) technique. The only issue that we’ve encountered was that we weren’t exactly a real team. We did set up ways to communicate & work together, but nobody was really using them and everybody was just doing their own thing. Half the team didn’t even join the dev ops team, so in order to work like this, we’ve agreed we’ll just talk what we want to work on and have separate bots doing their own thing and then, at the end, we’d do a big merge of all our code and just have a big bot with every functionality we’ve come up with. However, fast-forward 4 weeks later and people didn’t really want to do that anymore because it’d just be bother and since for this whole time we’ve been graded individually there wasn’t really any point to merge our code so we just focused on our own presentations and here we are.
  
  
## Sources
- [Getting Started Obligatory Youtube Video](https://www.youtube.com/watch?v=_0LXIvLDhBM)
- [Discord.py Official Documentation](https://discordpy.readthedocs.io/en/latest/)
- [Python Docs](https://docs.python.org/3/)
- [FFmpeg Audio Streaming Solution](https://www.ffmpeg.org/)
- [Web Scraper](https://pypi.org/project/beautifulsoup4/)
- [Performing Google Searches](https://www.geeksforgeeks.org/performing-google-search-using-python-code/)
