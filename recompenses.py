import discord
from discord.ext import commands
from discord_slash import cog_ext

class Recompenses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name = "recompenses", description = "Demander les recompenses d events.")
    async def recompenses(self, ctx, pseudoig, nombre_invite, prix_total):
        em = discord.Embed(description = f"🎁 **► Récompenses** \n \n > *Pseudo IG:* **{pseudoig}** \n > *Nombre d'invitation:* **{nombre_invite}** \n > *Prix total:* **{prix_total}**", color=0xFFA500)
        em.set_thumbnail(url = "https://cdn.discordapp.com/emojis/834364622555054080.png?v=1")
        em.set_footer(text = f"Demande de {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Recompenses(bot))