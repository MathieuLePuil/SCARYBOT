import discord
from discord.ext import commands
from discord_slash import cog_ext
import asyncio


class Close(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="close", description="Ferme le channel.")
    @commands.has_permissions(kick_members=True)
    async def close(self, ctx):

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        try:

            em = discord.Embed(title="Fermeture du Ticket",
                               description="Pour valider la fermeture, entrez `close` dans le chat. Si vous souhaitez annulé, faites `cancel`",
                               color=0xFFA500)
            em1 = discord.Embed(title="Fermeture du Ticket", description="Vous avez annulé la fermeture du channel !",
                                color=0xFFA500)

            await ctx.send(embed=em)
            msg = await self.bot.wait_for('message', check=check, timeout=60)

            if msg.content == "close":
                await ctx.channel.delete()
                return
            elif msg.content == "Close":
                await ctx.channel.delete()
                return
            else:
                await ctx.send(embed=em1)
                return

        except asyncio.TimeoutError:
            em = discord.Embed(title="Fermeture",
                               description="Vous avez mis trop de temps à répondre, veuillez refaire !close.",
                               color=0xFFA500)
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Close(bot))
