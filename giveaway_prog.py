from discord.ext import commands
import asyncio
import datetime
import json
import random
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


async def get_giveaway_data():
    with open("/home/mmi21b12/DISCORD/SCARYBOT/giveaway.json", "r") as f:
        giveawayinfo = json.load(f)

    return giveawayinfo


async def when_giveaway(message):
    giveawayinfo = await get_giveaway_data()

    if str(message.id) in giveawayinfo:
        return False
    else:

        giveawayinfo[str(message.id)] = {}
        giveawayinfo[str(message.id)]["message_id"] = message.id
        giveawayinfo[str(message.id)]["channel_id"] = "Channel"
        giveawayinfo[str(message.id)]["Lot"] = "Lot"
        giveawayinfo[str(message.id)]["Fin"] = "Fin"
        giveawayinfo[str(message.id)]["Condition"] = "Condition"
        giveawayinfo[str(message.id)]["Role"] = "Role"
    with open("/home/mmi21b12/DISCORD/SCARYBOT/giveaway.json", "w") as f:
        json.dump(giveawayinfo, f, indent=2)
    return True


class Giveaway_prog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def proggiveaway(self, ctx):
        embed = discord.Embed(title="**Lancer un Giveaway programmé**",
                              description="Pour lancer un giveaway programmé, veuillez cliquer sur le bouton sous ce message.",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://discord.com/assets/b052a4bef57c1aa73cd7cff5bc4fb61d.svg")
        embed.set_footer(text="ScaryBot - Giveaway",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.green, label="🎉 Giveaway", custom_id="giveaway_prog")])

        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interactions: Interaction):
        guild = self.bot.get_guild(705089080693751850)
        channel = interactions.channel
        if interactions.custom_id == "giveaway_prog":
            await interactions.respond(type=7)

            em1 = discord.Embed(description="Dans quel channel souhaitez-vous lancer le giveaway?",
                                color=0xFFA500)
            em2 = discord.Embed(description="Quelle est la durée du Giveaway? (s | m | d | h)", color=0xFFA500)
            em3 = discord.Embed(description="Quel est le lot du Giveaway?",
                                color=0xFFA500)
            em4 = discord.Embed(description="Quelles sont les conditions du Giveaway?", color=0xFFA500)
            em5 = discord.Embed(
                description="Un rôle est-il nécessaire pour participer au Giveaway? `(Si oui, mentionnez, sinon, écrivez \"non\")`",
                color=0xFFA500)
            em6 = discord.Embed(description="Dans combien de temps souhaitez-vous lancer le giveaway ? (s | m | d | h)",
                                color=0xFFA500)
            em7 = discord.Embed(description="Quel est le message de pub ? (si aucun, écrire `non`)", color=0xFFA500)
            em8 = discord.Embed(description="Quel est le message de mention ? (si aucun, écrire `non`)", color=0xFFA500)
            await interactions.channel.send(embed=em1)

            try:
                channelg = await self.bot.wait_for("message", timeout=60,
                                                   check=lambda
                                                       msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=1, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            digits = "0123456789"
            channelg_id = ""

            for i in channelg.content:
                if i in digits:
                    channelg_id += i

            channelg_id = int(channelg_id)

            await interactions.channel.send(embed=em2)

            try:
                duree = await self.bot.wait_for("message", timeout=60,
                                                check=lambda
                                                    msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=3, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em3)

            try:
                lot = await self.bot.wait_for("message", timeout=60,
                                              check=lambda
                                                  msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=5, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em4)

            try:
                condition = await self.bot.wait_for("message", timeout=60,
                                                    check=lambda
                                                        msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=7, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em5)

            try:
                role = await self.bot.wait_for("message", timeout=60,
                                               check=lambda
                                                   msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=9, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em6)

            try:
                start = await self.bot.wait_for("message", timeout=60,
                                                check=lambda
                                                    msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=11, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em7)

            try:
                pub = await self.bot.wait_for("message", timeout=60,
                                              check=lambda
                                                  msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=13, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interactions.channel.send(embed=em8)

            try:
                mention = await self.bot.wait_for("message", timeout=60,
                                                  check=lambda
                                                      msg: interactions.author == msg.author and channel == msg.channel)
            except:
                await interactions.channel.purge(limit=15, check=lambda msg: not msg.pinned)
                await interactions.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            if role.content != "non":
                digits = "0123456789"
                rolecond_id = ""
                for i in role.content:
                    if i in digits:
                        rolecond_id += i

                rolecond_id = int(rolecond_id)
                conditions = f"**{condition.content}** (<@&{rolecond_id}>)"
            else:
                conditions = f"**{condition.content}**"
                rolecond_id = "Aucune"

            await interactions.channel.purge(limit=16, check=lambda msg: not msg.pinned)

            time = convert(duree.content)
            start_time = convert(start.content)
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

            gchannel = self.bot.get_channel(channelg_id)
            guild.get_role(rolecond_id)

            embed = discord.Embed(title=f"**{lot.content}**",
                                  description=f"> *Host par:* **{interactions.user.mention}** \n > *Condition:* {conditions} \n \n Coche la réaction 🎉 pour participer!",
                                  color=0xFD3F92)
            embed.set_footer(text=f"Fin le: {fin.day} {month} {fin.year} à {fin.hour}h{minute}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/843936828016689152.png?v=1")

            await interactions.channel.send(f"Le giveaway de {lot.content} sera lancé dans {start.content} !")

            await asyncio.sleep(start_time)

            if pub.content != "non":
                await gchannel.send(pub.content)
            else:
                pass
            message = await gchannel.send("🎉 **GIVEAWAY** 🎉", embed=embed)
            await message.add_reaction("🎉")

            if mention.content != "non":
                await gchannel.send(mention.content)
            else:
                pass

            await when_giveaway(message)
            giveawayinfo = await get_giveaway_data()

            try:
                giveawayinfo[str(message.id)]["channel_id"] = channelg_id
                giveawayinfo[str(message.id)]["Lot"] = lot.content
                giveawayinfo[str(message.id)]["Fin"] = f"{fin.day} {month} {fin.year} a {fin.hour}h{minute}"
                giveawayinfo[str(message.id)]["Condition"] = condition.content
                giveawayinfo[str(message.id)]["Role"] = rolecond_id
            except KeyError:
                print(f"Il y a une erreur!")

            with open("/home/mmi21b12/DISCORD/SCARYBOT/giveaway.json", "w") as f:
                json.dump(giveawayinfo, f, indent=2)

            await asyncio.sleep(time)

            new_msg = await gchannel.fetch_message(message.id)

            users = await new_msg.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))

            winner = random.choice(users)

            await gchannel.send(
                f"🎉 **Bien joué** à toi {winner.mention}, tu remportes **{lot.content}**! Je t'invite à te rendre dans le <#765633542658195456> pour récuperer ton lot. 🎉")


def setup(bot):
    bot.add_cog(Giveaway_prog(bot))
