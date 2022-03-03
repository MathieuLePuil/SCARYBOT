from discord.ext import commands
from discord_slash.utils.manage_components import *
from discord_components import *


class Reseau(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reseau(self, ctx):
        embed = discord.Embed(
            description="📱 **► Réseaux Sociaux du ScaryShop** \n \n __Lien de nos réseaux:__ \n \n > <:instagram:835499519248171068> <a:fl:802827880618000414> https://bit.ly/3tY8gUd \n > <:twitter:835499512863653900> <a:fl:802827880618000414> https://bit.ly/3dIywMo \n > <:youtube:835499535500967996> <a:fl:802827880618000414> https://bit.ly/3aAeqSG \n \n __Nous contacter:__ \n \n > 📧 <a:fl:802827880618000414> scaryshopv3@gmail.com",
            color=0xFFA500)
        embed.set_image(url="https://cdn.discordapp.com/attachments/701111672844320868/913437551967211610/1.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/834364622555054080.png?v=1")
        await ctx.send(embed=embed, components=[
            [Button(style=ButtonStyle.URL, label="Instragam", url="https://bit.ly/3tY8gUd", custom_id="insta"),
             Button(style=ButtonStyle.URL, label="Twitter", url="https://bit.ly/3dIywMo", custom_id="twitter"),
             Button(style=ButtonStyle.URL, label="Youtube", url="https://bit.ly/3aAeqSG", custom_id="twitter")]])
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Reseau(bot))
