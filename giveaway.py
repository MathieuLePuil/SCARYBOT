import discord
from discord.ext import commands
import asyncio
import datetime
import json
import random
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


# noinspection PyGlobalUndefined
class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def giveaway(self, ctx):
        embed = discord.Embed(title="**Lancer un Giveaway**",
                              description="Pour lancer un giveaway, veuillez cliquer sur le bouton sous ce message.",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://discord.com/assets/b052a4bef57c1aa73cd7cff5bc4fb61d.svg")
        embed.set_footer(text="ScaryBot - Giveaway",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.green, label="🎉 Giveaway", custom_id="giveaway")])

        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interactions: Interaction):
        guild = self.bot.get_guild(705089080693751850)
        channel = interactions.channel
        if interactions.custom_id == "giveaway":
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

            await interactions.channel.purge(limit=10, check=lambda msg: not msg.pinned)

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

            gchannel = self.bot.get_channel(channelg_id)
            guild.get_role(rolecond_id)

            embed = discord.Embed(title=f"**{lot.content}**",
                                  description=f"> *Host par:* **{interactions.user.mention}** \n > *Condition:* {conditions} \n \n Coche la réaction 🎉 pour participer !",
                                  color=0xFD3F92)
            embed.set_footer(text=f"Fin le: {fin.day} {month} {fin.year} à {fin.hour}h{minute}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/843936828016689152.png?v=1")

            message = await gchannel.send("🎉 **GIVEAWAY** 🎉", embed=embed, )
            await message.add_reaction("🎉")

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

            new_msgs = await gchannel.fetch_message(message.id)

            users = await new_msgs.reactions[0].users().flatten()
            users.pop(users.index(self.bot.user))

            winner = random.choice(users)

            emfin = discord.Embed(title=f"**{lot.content}**",
                                  description=f"> *Host par:* **{interactions.user.mention}** \n > *Condition:* {conditions} \n \n Le gagnant est {winner.mention} !",
                                  color=0xFD3F92)
            emfin.set_footer(text=f"🎉 Giveaway terminé")
            emfin.set_thumbnail(url="https://cdn.discordapp.com/emojis/843936828016689152.png?v=1")

            await message.edit(embed=emfin)

            await gchannel.send(
                f"🎉 **Bien joué** à toi {winner.mention}, tu remportes **{lot.content}**! Je t'invite à te rendre dans le <#765633542658195456> pour récuperer ton lot. 🎉")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        author = guild.get_member(payload.user_id)
        message = self.bot.get_channel(payload.channel_id).get_partial_message(payload.message_id)
        await when_giveaway(message)
        giveawayinfo = await get_giveaway_data()

        messageid = giveawayinfo[str(message.id)]["message_id"]
        channelid = giveawayinfo[str(message.id)]["channel_id"]
        rolecond = giveawayinfo[str(message.id)]["Role"]
        botrole = guild.get_role(705124069997281421)

        if payload.channel_id == channelid and payload.message_id == messageid:

            if rolecond == "Aucune":
                return
            else:
                if str(payload.emoji) == "🎉":
                    rolecondi = guild.get_role(rolecond)

                    if rolecondi in author.roles:
                        return
                    if botrole in author.roles:
                        return
                    else:
                        await message.remove_reaction("🎉", author)
                        em = discord.Embed(title="Entrée refusée",
                                           description="Vous n'avez pas respecté les conditions du Giveaway. Votre entrée à donc été refusée. Vous pouvez de nouveau participer une fois que celle-ci sera remplie.",
                                           color=0xFFA500)
                        em.set_footer(text="ScaryBot - Giveaway",
                                      icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
                        await author.send(embed=em)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        global new_msg
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("L'ID est incorrect.")

        print(locals())

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        print(winner)

        await channel.send(
            f"🎉 **Bien joué** à notre nouveau gagnant {winner.mention}! Je t'invite à te rendre dans le <#765633542658195456> pour récuperer ton lot. 🎉")


def setup(bot):
    bot.add_cog(Giveaway(bot))
