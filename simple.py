from discord.ext import commands
from discord_slash import cog_ext


class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="youtube", description="Affiche la chaîne Youtube du créateur et du ScaryShop.")
    async def youtube(self, ctx):
        await ctx.send(
            "__**Voici la chaîne Youtube de la Faction:**__ https://www.youtube.com/channel/UCAeJH7t9jJBL8aRuWVtcDMA\n__**Voici la chaîne Youtube du créateur:**__ https://youtube.com/c/Dr3Xt3r \n N'hésite pas à aller t'abonner aux deux chaînes :smile:")

    @cog_ext.cog_slash(name="twitch", description="Affiche la chaîne Twitch du créateur.")
    async def twitch(self, ctx):
        await ctx.send("__**Voici la chaîne Twitch de mon créateur:**__ https://www.twitch.tv/Dr3Xt3rTV")

    @cog_ext.cog_slash(name="natonat", description="Vasy fais la commande tu vas rire.")
    async def natonat(self, ctx):
        await ctx.send("Je vous présente le gros con de service!")

    @cog_ext.cog_slash(name="chut",
                       description="Permet de rappeller aux utilisateurs de ne pas discuter dans les salons d'enchères.")
    @commands.has_permissions(ban_members=True)
    async def chut(self, ctx):
        await ctx.send(f"Les salons enchères ne sont pas fait pour discuter!")


def setup(bot):
    bot.add_cog(Simple(bot))
