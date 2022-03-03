from discord.ext import commands
from discord_slash import cog_ext


class Latence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="latence", description="Affiche la latence du bot.")
    async def latence(self, ctx):
        await ctx.send(f"**La latence du *ScaryBot* est de `{round(self.bot.latency * 1000)}ms`.**")
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Latence(bot))
