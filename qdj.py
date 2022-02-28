import discord
from discord.ext import commands
from discord_slash import cog_ext

class Quete(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@cog_ext.cog_slash(name = "qdj", description = "Partager la quete du jour.")
	@commands.has_permissions(send_tts_messages = True)
	async def qdj(self, ctx, date, item, gain, prix):
		em = discord.Embed(title = "🛒 **► Quête du Jour**", description = f"Quête du {date} \n \n > *ITEM:* **{item}** \n > *GAIN:* **{gain}** \n > *PRIX:* **{prix}**", color=0xFFA500)
		em.set_footer(text = "⇾ Ouvrez un ticket de commande pour l'acquérir.")
		await ctx.send(embed = em)
		mention = await ctx.send("<@&706473637372231742>")
		await mention.delete()

def setup(bot):
	bot.add_cog(Quete(bot))