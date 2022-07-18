import discord
from discord.ext import commands
import json


class On_member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("/home/mmi21b12/DISCORD/SCARYBOT/membre-serveur.json", 'r') as f:
            data = json.load(f)

        member_number = int(data["member-counter"])
        member_number += 1

        thewelChann = member.guild.get_channel(705101200990928967)
        maintwelChann = member.guild.get_channel(833077370151501864)
        stats = member.guild.get_channel(733783525395791892)
        roleChannel = member.guild.get_channel(705126357797044297)
        em = discord.Embed(title="𝑵𝒐𝒖𝒗𝒆𝒂𝒖 𝒎𝒆𝒎𝒃𝒓𝒆",
                           description=f"> **Bienvenue à toi** {member.mention} sur le **𝓢𝓬𝓪𝓻𝔂𝓼𝓱𝓸𝓹**. Tu es le **{member.guild.member_count} ème**. Je t'invite à lire le <#705101956418633848> pour ne pas te faire punir. Pour commander, rend-toi dans <#705135137830207568> et suis les instructions. \n \n *Bon jeu à toi sur le serveur !*",
                           color=0xFFA500)
        em.set_thumbnail(url=member.avatar_url)
        await stats.edit(name=f"⭐ ▬  Membres: {member.guild.member_count}")
        await thewelChann.send(embed=em)
        await maintwelChann.send(embed=em)
        msg = await roleChannel.send(f"{member.mention}")
        await msg.delete()

        data["member-counter"] = int(member_number)

        with open("/home/mmi21b12/DISCORD/SCARYBOT/membre-serveur.json", 'w') as f:
            json.dump(data, f)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("/home/mmi21b12/DISCORD/SCARYBOT/membre-serveur.json", 'r') as f:
            data = json.load(f)

        member_number = int(data["member-counter"])
        member_number -= 1
        stats = self.bot.get_channel(733783525395791892)
        await stats.edit(name=f"⭐ ▬  Membres: {member.guild.member_count}")

        data["member-counter"] = int(member_number)

        with open("/home/mmi21b12/DISCORD/SCARYBOT/membre-serveur.json", 'w') as f:
            json.dump(data, f)


def setup(bot):
    bot.add_cog(On_member_join(bot))
