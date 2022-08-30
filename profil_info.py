import discord
from discord.ext import commands
import asyncio
import datetime
import json
import random
from discord_components import *
from discord_slash import cog_ext


async def get_nbrcommande_data():
    with open("/home/mmi21b12/DISCORD/SCARYBOT/nbrcommande-user.json", "r") as f:
        nbrcommandeinfo = json.load(f)

    return nbrcommandeinfo


async def when_nbrcommande(user):
    nbrcommande = await get_nbrcommande_data()

    if str(user.id) in nbrcommande:
        return False
    else:

        nbrcommande[str(user.id)] = {}
        nbrcommande[str(user.id)]["user_id"] = user.id
        nbrcommande[str(user.id)]["nbrcommande"] = 0
        nbrcommande[str(user.id)]["argenttotal"] = 0

    with open("/home/mmi21b12/DISCORD/SCARYBOT/nbrcommande-user.json", "w") as f:
        json.dump(nbrcommande, f, indent=2)
    return True


# noinspection PyGlobalUndefined
class Profil_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @cog_ext.cog_slash(name="profil_info", description="Voir le profil des commandes de l'utilisateur.")
    @commands.has_permissions(kick_members = True)
    async def profil_info(self, ctx, user: discord.User):
        await when_nbrcommande(user)
        nbrcommande = await get_nbrcommande_data()

        nbrco = nbrcommande[str(user.id)]["nbrcommande"]
        argent = nbrcommande[str(user.id)]["argenttotal"]

        em = discord.Embed(title=f"Informations de {user}", description=f"> **Nombre de commande** <a:fl:802827880618000414> `{nbrco}` \n > **Argent total dépensé** <a:fl:802827880618000414> `{argent}$`", color=0xFFA500)

        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Profil_info(bot))
