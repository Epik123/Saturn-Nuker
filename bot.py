# IMPORTANT
token = "" # PUT YOUR BOT TOKEN INBETWEEN THE ""s

import disnake
from disnake.ext import commands


bot = commands.Bot(perfix="!", intents=disnake.intents.all(), case_insensitive=True, sync_commands=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Ready\nLogged in as {}".format(bot.user))


def loadCogs():
    """
    Load Extentions Of The Bot
    """
    if os.path.isfile("./cogs/__init__.py"):
        try:
            bot.load_extension(f"cogs.__init__")
            print("Loaded Cogs ✅")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    """
    Used too load the cogs of the bot
    """
    loadCogs()


bot.run(token)