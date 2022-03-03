import discord
from discord.ext import commands


class Msgsugg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def msgsugg(self, ctx):
        emp = discord.Embed(title="💡 ► SUGGESTION",
                            description="Pour proposer une suggestion, veuillez entrer la commande `/suggestion <SUGGESTION>` dans le chat ci-dessous.",
                            color=0xFFA500)
        await ctx.send(embed=emp)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Msgsugg(bot))
