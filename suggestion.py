import discord
from discord.ext import commands
from discord_slash import cog_ext

class Suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "suggestion", description = "Suggère une idée au staff.")
    async def suggestion(self, ctx, *suggestion):
        suggestion = " ".join(suggestion)

        sugg = self.bot.get_channel(705378996195426315)

        embed = discord.Embed(title = "💡 ► SUGGESTION", description = f"> {suggestion}", color=0xFFA500)
        msg = embed.set_footer(text = f"Par {ctx.author.name}")
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")

        await sugg.send(embed = embed)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Suggestion(bot))