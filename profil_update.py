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
class Profil_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @cog_ext.cog_slash(name="profil_update", description="Mettre à jour le profil des commandes de l'utilisateur.")
    @commands.has_permissions(kick_members = True)
    async def profil_update(self, ctx, user: discord.User, objet, quantite):
        await when_nbrcommande(user)
        nbrcommande = await get_nbrcommande_data()
        if objet == "commande":
            if quantite.startswith("-"):
                quantite1 = quantite.replace("-", "")
                quantite_final = int(quantite1)
                try:
                    nbrcommande[str(user.id)]["nbrcommande"] = nbrcommande[str(user.id)]["nbrcommande"] - quantite_final
                    em = discord.Embed(description=f"`{quantite_final}` commande(s) a/ont été retirée(s) à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")
            elif quantite.startswith("+"):
                quantite1 = quantite.replace("+", "")
                quantite_final = int(quantite1)
                try:
                    nbrcommande[str(user.id)]["nbrcommande"] = nbrcommande[str(user.id)]["nbrcommande"] + quantite_final
                    em = discord.Embed(description=f"`{quantite_final}` commande(s) a/ont été ajoutée(s) à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")
            elif quantite.startswith("="):
                quantite = quantite.replace("=", "")
                quantite = int(quantite)
                try:
                    nbrcommande[str(user.id)]["nbrcommande"] = quantite
                    em = discord.Embed(description=f"`{quantite}` commande(s) a/ont été mise(s) à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")
        elif objet == "argent":
            if quantite.startswith("-"):
                quantite1 = quantite.replace("-", "")
                quantite_final = int(quantite1)
                try:
                    nbrcommande[str(user.id)]["argenttotal"] = nbrcommande[str(user.id)]["argenttotal"] - quantite_final
                    em = discord.Embed(description=f"`{quantite_final}$` ont été retirés à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")
            elif quantite.startswith("+"):
                quantite1 = quantite.replace("+", "")
                quantite_final = int(quantite1)
                try:
                    nbrcommande[str(user.id)]["argenttotal"] = nbrcommande[str(user.id)]["argenttotal"] + quantite_final
                    em = discord.Embed(description=f"`{quantite_final}$` ont été ajoutés à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")
            if quantite.startswith("="):
                quantite = quantite.replace("=", "")
                quantite = int(quantite)
                try:
                    nbrcommande[str(user.id)]["argenttotal"] = quantite
                    em = discord.Embed(description=f"`{quantite}$` ont été fixés à {user.mention} !",
                                       color=0xFFA500)
                except KeyError:
                    print(f"Il y a une erreur!")

        with open("/home/mmi21b12/DISCORD/SCARYBOT/nbrcommande-user.json", "w") as f:
            json.dump(nbrcommande, f, indent=2)

        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Profil_update(bot))
