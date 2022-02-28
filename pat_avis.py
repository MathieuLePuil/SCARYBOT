import discord
from discord.ext import commands

class Patavis(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(send_tts_messages = True)
	async def pat_avis(self, ctx):
		em = discord.Embed(description = f"N'hésitez pas à laisser votre avis sur le vendeur (<#705434824323760209>) ainsi que sur les prix du catalogue (<#706532743705788558>) !", color=0xFFA500)
		await ctx.send(embed = em)
		await ctx.message.delete()

def setup(bot):
  	bot.add_cog(Patavis(bot))