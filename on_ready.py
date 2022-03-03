from discord.ext import commands
from discord_slash.utils.manage_components import *
from discord_components import *


class On_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(828549652621164574)

        await self.bot.change_presence(status=discord.Status.online,
                                       activity=discord.Activity(type=discord.ActivityType.playing,
                                                                 name="Comment ça marche? | !help"))
        print("Scarybot est PRET!")
        await channel.send("**`Scarybot`** vient de redémarrer!")
        # msg = await channel.send("<@337971595928666113>")
        # await msg.delete()
        DiscordComponents(self.bot)


def setup(bot):
    bot.add_cog(On_ready(bot))
