# RUN AT YOUR OWN RISK

# Nuker cog (Using disnake package)


Feel free too edit the code 

# Setup 
First go to https://discord.com/developers/applications
in the top left hit the button "New Application" - Name Your Application Anything, then hit create

on the left there will be a sidebar with the name settings - hit Bot, on that page create "Add Bot", Hit the button "Yes, do it"

first scroll down too where it says "Privileged Gateway Intents", there should be 3 options unchecked labeled "PRESENCE INTENT"
"SERVER MEMBERS INTENT", and "MESSAGE CONTENT INTENT", check all of these and the scroll up

there should be a button labeled "Reset Token", reset your bot's token, (DO NOT GIVE THIS AWAY) then copy it and head over too bot.py

when you are there at the very top of the file it should be labeled "token = "" # PUT YOUR BOT TOKEN INBETWEEN THE ""s"
paste your token inbetween the ""s as stated and then you are free too run the bot


# Setup - ONLY IF YOU WANT TOO ADD THE COG TOO A PRE EXISTING BOT
too add this too you bot create a folder named cogs
create the file with any name that you want

in the main file add a definition or add it too the if __name__ == "__main__": statement
add the code below
bot.load_extention("cogs.FILENAMEHERE")

or you can get too something more advanced (seen below)
```py
def loadCogs():
    """
    Load Extentions Of The Bot
    """
    if os.path.isfile("./cogs/nuker.py"):
        try:
            bot.load_extension(f"cogs.nuker")
            print("Loaded Cogs ✅")
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
  loadCogs()
```
# Notes:
in bot.load_extention you may have too change "bot" too something different it depeneds on how you initalize your bot

# Issues/Support 
feel free too contact collin#8694 on discord

# Commands
There are multiple nuke commands

!banall - Bans all of the members in a guild
!kickall - Kicks all of the members in a guild
!nukeserver - Edits all of the guild information too make it hard too recover from the nuke, then bans all of the members
!nickall (nick) - Edits all of the nicknames of members in a guild
!messageall (message) - Sends a message too all of the members in a guild
!clearroles - Deletes all of the roles in a guild
!clearemojis - Deletes all of the emojis in a guild
!clearchannels - Deletes all of the channels in a guild