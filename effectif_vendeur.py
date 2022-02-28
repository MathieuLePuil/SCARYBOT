import discord
from discord.ext import commands
from discord_slash import *
import datetime

class EffeVendeur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "effectif_vendeur", description = "Affiche la liste des vendeurs du serveur.")
    @commands.has_permissions(manage_roles = True)
    async def effectif_vendeur(self, ctx):
        guild = ctx.guild

        total_effectif = 0
        blacklist_users = []
        data_roles = [
            {"name": "Vendeur# Expérimenté#+", "id": 830762213219762216, "count": 0, "list_users": []},
            {"name": "Vendeur# Confirmé#+", "id": 797183065272483842, "count": 0, "list_users": []},
            {"name": "Vendeur", "id": 797898409318416385, "count": 0, "list_users": []},
            {"name": "Vendeur# Test+", "id": 797183068125134868, "count": 0, "list_users": []}
        ]

        for member in guild.members:
            m_roles_id = [r.id for r in member.roles]
            for role in data_roles:
                if role['id'] in m_roles_id and member.id not in blacklist_users:
                    total_effectif += 1
                    role['count'] += 1
                    role['list_users'].append(member)
                    blacklist_users.append(member.id)

        embed = discord.Embed(description=f"Voici l'effectif des vendeurs du ScaryShop ({total_effectif}) :",
                              timestamp=datetime.datetime.utcnow(),
                              color=0xFFA500)

        for role in reversed(data_roles):
            list_users = []
            for user in role['list_users']:
                list_users.append(f"• {user.mention}")
            if list_users == []: list_users = ["Aucun"]
            if role['count'] > 1 or role['count'] == 0: prefix, suffix = "Nos", "s"
            else: prefix, suffix = "Notre", ""
            if "+" not in role['name']: role['name'] = f"{prefix} {role['name']}{suffix}"
            else: role['name'] = f"{prefix} {role['name'].replace('#', suffix).replace('+', '')}"
            embed.add_field(name=f"{role['name']} ({role['count']})",
                            value="\n".join(list_users),
                            inline=False)

        embed.set_thumbnail(url="https://c.tenor.com/VI9RkEoTzLQAAAAi/busts-in-silhouette-people.gif")
        embed.set_author(name=f"ScaryShop V4", icon_url=guild.icon_url)
        embed.set_footer(icon_url=guild.icon_url, text=f"{guild.name}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EffeVendeur(bot))