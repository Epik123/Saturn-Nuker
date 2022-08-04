# MonkeySquad-Cog-Nuker

Nuker cog (Using disnake package)


Feel free too edit this

# Setup
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
