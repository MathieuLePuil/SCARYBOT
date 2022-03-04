from discord.ext import commands
import asyncio
import datetime
from discord_slash.utils.manage_components import *
from discord_components import *


def convert(time):

    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1

    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


class Enchere(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def enchere(self, ctx):
        embed = discord.Embed(title="**Lancer une enchère**",
                              description="Pour lancer une enchère, veuillez cliquer sur le bouton sous ce message.",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/808290709404516402.gif?size=128")
        embed.set_footer(text="ScaryBot - Enchère",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.green, label="⚖️ Enchère", custom_id="enchere")])
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interactions: Interaction):
        channel = interactions.channel
        if interactions.custom_id == "enchere":
            await interactions.respond(type=7)

            em1 = discord.Embed(description="Dans quel channel souhaitez-vous lancer l'enchère?",
                                color=0xFFA500)
            em2 = discord.Embed(description="Quel est l'objet et la quantité de l'enchère?", color=0xFFA500)
            em3 = discord.Embed(description="Quel est le prix de départ de l'enchère? (sans le $)",
                                color=0xFFA500)
            em4 = discord.Embed(description="Quelle est la durée de l'enchère? `(s|m|h|d)`", color=0xFFA500)
            em5 = discord.Embed(
                description="Quel est le pas de l'enchère? `(1 pour 1.000$ en 1.000$, 2 pour 2.000$ en 2.000$...)`",
                color=0xFFA500)
            em6 = discord.Embed(description="Quel est l'id du vendeur'?", color=0xFFA500)

            await interactions.channel.send(embed=em1)

            try:
                channele = await self.bot.wait_for("message", timeout=60,
                                                   check=lambda
                                                       msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=1, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            digits = "0123456789"
            channele_id = ""

            for i in channele.content:
                if i in digits:
                    channele_id += i

            channele_id = int(channele_id)

            await interactions.channel.send(embed=em2)

            try:
                item = await self.bot.wait_for("message", timeout=60,
                                               check=lambda
                                                   msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=3, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3)

            try:
                prix = await self.bot.wait_for("message", timeout=60,
                                               check=lambda
                                                   msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=5, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4)

            try:
                duree = await self.bot.wait_for("message", timeout=60,
                                                check=lambda
                                                    msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=7, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5)

            try:
                pas = await self.bot.wait_for("message", timeout=60,
                                              check=lambda
                                                  msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=9, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em6)

            try:
                vendeurid = await self.bot.wait_for("message", timeout=60,
                                                    check=lambda
                                                        msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=11, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.purge(limit=12, check=lambda msg: not msg.pinned)

            time = convert(duree.content)
            fin = datetime.datetime.now() + datetime.timedelta(seconds=time)
            month = "Aucun"

            if fin.month == 1:
                month = "Janvier"
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

            echannel = self.bot.get_channel(channele_id)

            embed = discord.Embed(title="⚖️ ► Nouvelle enchère",
                                  description=f"**Enchère de :** \n <:fad:835500807210270770> <@{vendeurid.content}> \n \n **Enchère :** \n > 📦 *Item en vente:* ***{item.content}*** \n > 💰 *Prix de départ:* ***{prix.content}$*** \n > ⏱️ *Date de fin:* ***{fin.day} {month} {fin.year} à {fin.hour}h{minute}***",
                                  color=0xFFA500)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/758324312829591582.png?v=1")
            embed.set_footer(
                text=f"⇾ Veuillez enchérir de {pas.content}.000$ en {pas.content}.000$. \n ⇾ Il est interdit de discuter ici sous peine de sanction.")

            await echannel.send(embed=embed)
            await echannel.send("<@&714866835589431298>", delete_after=1)

            await asyncio.sleep(time)

            await echannel.send("***L'ENCHÈRE EST TERMINÉE !***")
            await echannel.send("<@&753490443819417741>", delete_after=1)


def setup(bot):
    bot.add_cog(Enchere(bot))
