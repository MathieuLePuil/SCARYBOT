import discord
from discord.ext import commands
from discord_components import *
from discord_slash import *
import json
import datetime


async def get_gift_data():
    with open("/home/mmi21b12/DISCORD/SCARYBOT/gift.json", "r") as f:
        giftinfo = json.load(f)

    return giftinfo


async def when_gift(message):
    giftinfo = await get_gift_data()

    if str(message.id) in giftinfo:
        return False
    else:
        giftinfo[str(message.id)] = {}
        giftinfo[str(message.id)]["Message ID"] = message.id
        giftinfo[str(message.id)]["Winner"] = "gagnant"
        giftinfo[str(message.id)]["Cadeau"] = "cadeau"
        giftinfo[str(message.id)]["Author ID"] = "id author"

    with open("/home/mmi21b12/DISCORD/SCARYBOT/gift.json", "w") as f:
        json.dump(giftinfo, f, indent=2)
    return True


class Gift(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def gift(self, ctx, *, gift):
        embed = discord.Embed(title=f"**{gift}**",
                              description=f"> *Host par:* {ctx.author.mention} \n \n Clique sur le bouton en premier pour remporter le lot !",
                              color=0xFFA500, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/857904665986596904.gif?size=96&quality=lossless")
        embed.set_footer(icon_url=ctx.guild.icon_url, text=f"{ctx.guild.name}")

        giftmsg = await ctx.send(embed=embed,
                                 components=[Button(style=ButtonStyle.green, label="🎁", custom_id="gift")])

        await when_gift(message=giftmsg)
        giftinfo = await get_gift_data()

        try:
            giftinfo[str(giftmsg.id)]["Cadeau"] = gift
            giftinfo[str(giftmsg.id)]["Message ID"] = giftmsg.id
            giftinfo[str(giftmsg.id)]["Author ID"] = ctx.author.id
        except KeyError:
            print(f"Il y a une erreur!")

        with open("/home/mmi21b12/DISCORD/SCARYBOT/gift.json", "w") as f:
            json.dump(giftinfo, f, indent=2)

        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interactions: Interaction):
        message = interactions.message
        channel = interactions.channel
        if interactions.custom_id == "gift":
            await interactions.respond(type=7)

            await when_gift(message=interactions.message)
            giftinfo = await get_gift_data()

            cadeau = giftinfo[str(message.id)]["Cadeau"]
            idmsg = giftinfo[str(message.id)]["Message ID"]
            authorid = giftinfo[str(message.id)]["Author ID"]

            embed = discord.Embed(title=f"**{cadeau}**",
                                  description=f"> *Host par:* <@{authorid}> \n \n Lot remporté par {interactions.user.mention}. GG !",
                                  color=0xFFA500, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/857904665986596904.gif?size=96&quality=lossless")
            embed.set_footer(icon_url=interactions.guild.icon_url, text=f"{interactions.guild.name}")

            msg = await channel.fetch_message(idmsg)
            await msg.edit(embed=embed, components=[
                Button(style=ButtonStyle.green, label="🎁", custom_id="gift", disabled=True)])

            await interactions.channel.send(
                f"🎉 GG {interactions.user.mention}, tu remportes **{cadeau}**! Je t'invite à te rendre dans le <#765633542658195456> pour récupérer ton lot. 🎉")

        else:
            return


def setup(bot):
    bot.add_cog(Gift(bot))
