# IMPORTANT
import disnake
from disnake.ext import commands

import json
import os


if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        json.dump(
            {"token": "",
             "webraidadvanced": False,
             "webraidmessages": 20
             }, f, indent=4)
        exit()
else:
    with open("config.json") as f:
        config = json.load(f)


bot = commands.Bot(perfix=".", intents=disnake.Intents.all(), sync_commands=True)
bot.remove_command("help")


def loadCogs():
    """
    Load Extentions Of The Bot
    """
    bot.load_extension(f"cogs.nuker")


if __name__ == "__main__":
    """
    Used too load the cogs of the bot
    """
    loadCogs()


bot.run(config.get("token"))