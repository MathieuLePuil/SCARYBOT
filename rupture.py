import discord
from discord.ext import commands
from discord_slash import cog_ext


class Rupture(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="rupture", description="Ajoute un item en rupture de stock.")
    async def rupture(self, ctx, categorie, item, prix, emoji):
        em = discord.Embed(description=f"> {emoji} **Catégorie:** {categorie} / **Item:** {item} / **Prix:** {prix}",
                           color=0xFFA500)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Rupture(bot))
