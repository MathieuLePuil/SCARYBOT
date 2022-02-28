import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
from discord_slash import SlashCommand, ButtonStyle
import datetime
import json
import random
from discord import Permissions
from colorama import Fore, Style
from discord_slash.utils.manage_components import *
from discord_components import *
from discord_slash import *

class Rappel(commands.Cog):
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

    @cog_ext.cog_slash(name = "rappel", description = "Met un rappel dans un certain temps dans un channel spécifique.")
    @commands.has_permissions(kick_members = True)
    async def rappel(self, ctx, channel : discord.TextChannel, duree, reason = "Aucune raison n'a été renseignée"):
        time = self.convert(duree)
        fin = datetime.datetime.now() + datetime.timedelta(seconds = time)

        if fin.month == 1:
            month == "Janvier"
        elif fin.month == 2:
            month = "Février"
        elif fin.month == 3:
            month = "Mars"
        elif fin.month == 4:
            month = "Avril"
        elif fin.month == 5:
            month = "Mai"
        elif fin.month == 6:
            month = "Juin"
        elif fin.month == 7:
            month = "Juillet"
        elif fin.month == 8:
            month = "Août"
        elif fin.month == 9:
            month = "Septembre"
        elif fin.month == 10:
            month = "Octobre"
        elif fin.month == 11:
            month = "Novembre"
        elif fin.month == 12:
            month = "Décembre"

        if fin.minute < 10:
            minute = f"0{fin.minute}"
        else:
            minute = fin.minute

        em1 = discord.Embed(description = f"Vous avez mis un rappel pour le **{fin.day} {month} {fin.year} à {fin.hour}h{minute}** dans {channel.mention}.", color = 0xFFA500)
        em1.set_footer(text="ScaryBot",
                             icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed = em1)

        await asyncio.sleep(time)

        em2 = discord.Embed(description = f"**⏰ ► RAPPEL** \n \n > **Raison :** *{reason}* \n > **Rappel de** {ctx.author.mention}", color = 0xFFA500)
        em2.set_footer(text="ScaryBot", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await channel.send(embed = em2)
        await channel.send(ctx.author.mention, delete_after = 1)
        


def setup(bot):
    bot.add_cog(Rappel(bot))