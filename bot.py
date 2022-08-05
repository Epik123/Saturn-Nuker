# IMPORTANT
token = "" # PUT YOUR BOT TOKEN INBETWEEN THE ""s

import disnake
from disnake.ext import commands

import os


bot = commands.Bot(perfix=".", intents=disnake.Intents.all(), sync_commands=True)
bot.remove_command("help")


# class Console:
#     def __init__(self):
#         self.maintext = "Discord Nuker || Version: 1.0.0 || "
#         self.update(update = "Initialized || ")
    
#     def update(self, update):
#         os.system(f"{self.maintext}+{update}")
#         self.maintext = f"{self.maintext}+{update}"


@bot.event
async def on_ready():
    print("Ready\nLogged in as {}".format(bot.user))


def loadCogs():
    """
    Load Extentions Of The Bot
    """
    try:
        bot.load_extension(f"cogs.nuker")
        print("Loaded Cogs ✅")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """
    Used too load the cogs of the bot
    """
    loadCogs()

Console()
bot.run(token)