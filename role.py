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
from discord_slash import cog_ext

class Role(commands.Cog):
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

    @cog_ext.cog_slash(name = "tempgrade", description = "Mettre temporairement un rôle payant à un joueur.")
    @commands.has_permissions(ban_members = True)
    async def tempgrade(self, ctx, user: discord.Member, duree, value):
        guild = self.bot.get_guild(705089080693751850)
        rolebarre1 = guild.get_role(733678143495208991)
        rolebarre2 = guild.get_role(838447916942229555)
        rolebarre3 = guild.get_role(838448157834346557)
        rolebarre4 = guild.get_role(819309540909776907)

        if value == "sorciere":
            em1 = discord.Embed(description = f"Le rôle <@&835561129186295858> a bien été ajouté à {user.mention} pour {duree} !", color = 0xFF7F00)
            em1.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            em2 = discord.Embed(description = f"Le rôle <@&835561129186295858> a été retiré à {user.mention} !", color = 0xFF7F00)
            em2.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            role = guild.get_role(835561129186295858)
            bon = guild.get_role(836949397089812511)
            await user.add_roles(role)
            await user.add_roles(bon)
            await user.add_roles(rolebarre1)
            await user.add_roles(rolebarre2)
            await user.add_roles(rolebarre3)
            await user.add_roles(rolebarre4)
            time = self.convert(duree)
            await ctx.send(embed = em1)
        
        if value == "faucheuse":
            em1 = discord.Embed(description = f"Le rôle <@&769261725421535244> a bien été ajouté à {user.mention} pour {duree} !", color = 0xFF7F00)
            em1.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            em2 = discord.Embed(description = f"Le rôle <@&769261725421535244> a été retiré à {user.mention} !", color = 0xFF7F00)
            em2.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            role = guild.get_role(769261725421535244)
            bon = guild.get_role(833274658467348480)
            await user.add_roles(role)
            await user.add_roles(bon)
            await user.add_roles(rolebarre1)
            await user.add_roles(rolebarre2)
            await user.add_roles(rolebarre3)
            await user.add_roles(rolebarre4)
            time = self.convert(duree)
            await ctx.send(embed = em1)

        if value == "fantome":
            em1 = discord.Embed(description = f"Le rôle <@&769261964311789588> a bien été ajouté à {user.mention} pour {duree} !", color = 0xFF7F00)
            em1.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            em2 = discord.Embed(description = f"Le rôle <@&769261964311789588> a été retiré à {user.mention} !", color = 0xFF7F00)
            em2.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            role = guild.get_role(769261964311789588)
            bon = guild.get_role(833274658467348480)
            await user.add_roles(role)
            await user.add_roles(bon)
            await user.add_roles(rolebarre1)
            await user.add_roles(rolebarre2)
            await user.add_roles(rolebarre3)
            await user.add_roles(rolebarre4)
            time = self.convert(duree)
            await ctx.send(embed = em1)

        if value == "assassin":
            em1 = discord.Embed(description = f"Le rôle <@&769262090308943935> a bien été ajouté à {user.mention} pour {duree} !", color = 0xFF7F00)
            em1.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            em2 = discord.Embed(description = f"Le rôle <@&769262090308943935> a été retiré à {user.mention} !", color = 0xFF7F00)
            em2.set_footer(text = "ScaryBot - Grades", icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            role = guild.get_role(769262090308943935)
            bon = guild.get_role(871680557602439189)
            await user.add_roles(role)
            await user.add_roles(bon)
            await user.add_roles(rolebarre1)
            await user.add_roles(rolebarre2)
            await user.add_roles(rolebarre3)
            await user.add_roles(rolebarre4)
            time = self.convert(duree)
            await ctx.send(embed = em1)

        await asyncio.sleep(time)

        await user.remove_roles(role)
        await user.remove_roles(bon)
        await user.remove_roles(rolebarre1)
        await user.remove_roles(rolebarre2)
        await user.remove_roles(rolebarre3)
        await user.remove_roles(rolebarre4)
        await ctx.send(f"{ctx.author.mention}", delete_after = 1)
        await ctx.send(embed = em2)

    @cog_ext.cog_slash(name = "cles", description = "Donner l'accès de son bureau à un utilisateur.")
    @commands.has_permissions(ban_members = True)
    async def cles(self, ctx, user: discord.Member):
        guild = self.bot.get_guild(705089080693751850)
        barre1 = guild.get_role(905388873947938836)
        barre2 = guild.get_role(838448157834346557)
        if ctx.author.id == 337971595928666113:
            print("1")
            role = guild.get_role(905389601332531200)
            await user.add_roles(role)
            await user.add_roles(barre1)
            await user.add_roles(barre2)

        elif ctx.author.id == "477556624467165185":
            role = guild.get_role(905389895143522305)
            await user.add_roles(role)
            await user.add_roles(barre1)
            await user.add_roles(barre2)

        elif ctx.author.id == "362602300704817153":
            role = guild.get_role(905390102799347712)
            await user.add_roles(role)
            await user.add_roles(barre1)
            await user.add_roles(barre2)

        elif ctx.author.id == "402525529653248035":
            role = guild.get_role(905390249918734386)
            await user.add_roles(role)
            await user.add_roles(barre1)
            await user.add_roles(barre2)

        elif ctx.author.id == "730110419280068681":
            role = guild.get_role(905390357959811084)
            await user.add_roles(role)
            await user.add_roles(barre1)
            await user.add_roles(barre2)

        em = discord.Embed(description = f"Vous venez d'ajouté la clé de votre bureau à {user.mention} !", color = 0xFFA500)
        await ctx.send(embed = em)

        



    @cog_ext.cog_slash(name = "addrole", description = "Ajouter un rôle à un joueur.")
    @commands.has_permissions(ban_members = True)
    async def addrole(self, ctx, member : discord.Member, role : discord.Role):
        await member.add_roles(role)
        em = discord.Embed(description = f"Le rôle {role.mention} a été ajouté à {member.mention} !", color = 0xFFA500)
        await ctx.send(embed = em)



def setup(bot):
    bot.add_cog(Role(bot))