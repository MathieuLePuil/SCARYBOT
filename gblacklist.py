import discord
from discord.ext import commands
import asyncio
import datetime
from discord_slash import cog_ext

class Gblacklist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, time):

        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1

        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]


    @cog_ext.cog_slash(name = "gblacklist", description = "Blacklister un joueur qui n a pas respecte les conditions du giveaway.")
    @commands.has_permissions(kick_members = True)
    async def gblacklist(self, ctx, blacklist_user : discord.User, duree):

        guild = self.bot.get_guild(705089080693751850)
        roleBl = guild.get_role(819310756491296799)
        roleBarre1 = guild.get_role(769262346551689276)
        roleBarre2 = guild.get_role(838448008693153802)
        log_channel = guild.get_channel(853703546028818443)

        embed = discord.Embed(description = f"**{blacklist_user}** a été blacklist des **enchères**! \n \n Tu pourras de nouveau participer aux giveaways dans {duree}.", color = 0xFFA500)
        embed.set_thumbnail(url = blacklist_user.avatar_url)

        embed2 = discord.Embed(description = f"**{blacklist_user}** a été blacklist des **enchères**! \n \n Cette sanction est permanente.", color = 0xFFA500)
        embed2.set_thumbnail(url = blacklist_user.avatar_url)

        await blacklist_user.add_roles(roleBl)
        await blacklist_user.add_roles(roleBarre1)
        await blacklist_user.add_roles(roleBarre2)

        if duree == "permanent":
            await ctx.send(embed = embed2)
            await log_channel.send(embed = embed2)

        if duree == "perma":
            await ctx.send(embed = embed2)
            await log_channel.send(embed = embed2)

        if duree == "perm":
            await ctx.send(embed = embed2)
            await log_channel.send(embed = embed2)

        else:

            time = self.convert(duree)

            await ctx.send(embed = embed)
            await log_channel.send(embed = embed)

            await asyncio.sleep(time)

            await blacklist_user.remove_roles(roleBl)
            await blacklist_user.remove_roles(roleBarre1)
            await blacklist_user.remove_roles(roleBarre2)


    @cog_ext.cog_slash(name = "gunblacklist", description = "Unblacklister un joueur qui n a pas respecte les conditions du giveaway.")
    @commands.has_permissions(kick_members = True)
    async def gunblacklist(self, ctx, blacklist_user : discord.User):

        guild = self.bot.get_guild(705089080693751850)
        roleBl = guild.get_role(819310756491296799)
        roleBarre1 = guild.get_role(769262346551689276)
        roleBarre2 = guild.get_role(838448008693153802)
        log_channel = guild.get_channel(856523186480480256)

        await blacklist_user.remove_roles(roleBl)
        await blacklist_user.remove_roles(roleBarre1)
        await blacklist_user.remove_roles(roleBarre2)
        embed = discord.Embed(description = f"**{blacklist_user}** a été unblacklist des **enchères**! \n \n Tu peux de nouveau participer aux giveaways.", color = 0xFFA500)
        embed.set_thumbnail(url = blacklist_user.avatar_url)
        await ctx.send(embed = embed)
        await log_channel.send(embed = embed) 
        await ctx.message.delete()


def setup(bot):
     bot.add_cog(Gblacklist(bot))