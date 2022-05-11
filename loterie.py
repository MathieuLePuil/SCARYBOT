import discord
from discord.ext import commands
from discord.ext.commands import cooldown
from discord_slash import cog_ext
import datetime
import random


class Loterie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="loterie",
                       description="Permet aux joueurs de tenter de gagner un lot toutes les 24h.", aliases=['loterie', 'lotos'])
    @cooldown(1, 86400, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def loto(self, ctx):
        gain = ["PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU", "PERDU",
                "PERDU", "PERDU", "PERDU", "PERDU", "1.000$ sur Paladium", "1.000$ sur Paladium", "2 Blocs de Paladium",
                "2 Findiums", "2.000$ sur Paladium"]
        lot = random.choice(gain)
        if lot == "PERDU":
            em = discord.Embed(
                description="Désolé, vous n'avez rien gagné aujourd'hui. Revenez dans 24h pour retenter votre chance !",
                color=0xFFA500, timestamp=datetime.datetime.utcnow())
        else:
            em = discord.Embed(
                description=f"GG, vous remportez **{lot}**. Rendez-vous dans le <#765633542658195456> pour récuperer votre récompense !",
                color=0xFFA500, timestamp=datetime.datetime.utcnow())

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Loterie(bot))
