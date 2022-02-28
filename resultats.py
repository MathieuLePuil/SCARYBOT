import discord
from discord.ext import commands
from discord_slash import cog_ext

class Resultats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "resultats", description = "Annoncer le resultats d'une enchere.")
    @commands.has_permissions(kick_members = True)
    async def resultats(self, ctx, mention_gagnant : discord.User, item, prix, mention_vendeur : discord.User):
        em = discord.Embed(description = f"**GG** à {mention_gagnant.mention}, tu remportes {item} au prix de ***{prix}*** vendu par {mention_vendeur.mention}. Je vous invite à vous MP pour faire le trade.", color=0xFFA500)
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Resultats(bot))