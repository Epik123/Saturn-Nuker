# IMPORTANT
token = "MTAwNDgxNjQ5MDczNTg4MjI3MA.GO14xd.i-lmpgEuaF58d18eBJ0vBT_feu0pdPdO5ky0I4" # PUT YOUR BOT TOKEN INBETWEEN THE ""s

import disnake
from disnake.ext import commands

import os
import traceback
import ctypes


from cogs.nuker import Console


bot = commands.Bot(perfix=".", intents=disnake.Intents.all(), sync_commands=True)
bot.remove_command("help")


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
        print("\n")
        traceback.print_exc()


if __name__ == "__main__":
    """
    Used too load the cogs of the bot
    """
    loadCogs()

Console()
bot.run(token)