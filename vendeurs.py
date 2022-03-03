from discord.ext import commands
from discord_components import *
from discord_slash.utils.manage_components import *


class Vendeurs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rcv(self, ctx, status):
        embedo = discord.Embed(
            description="👨🏼‍💼 **► Recrutement Vendeurs ScaryShop** \n \n __Conditions à respecter:__ \n \n > • Avoir minimum **13** ans \n > • Avoir un orthographe **correct** \n > • Pouvoir répondre à **toute commande** \n > • Avoir un **minimum de stuff** et être **avancé** dans **les métiers** \n \n Si vous respectez ces conditions, je vous invite à cliquer sur le bouton ci-dessous pour accéder au formulaire. \n \n Bonne chance à vous!",
            color=0x00FFFF)
        embedo.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/705448891570716752/913711303493840916/recrutement.png")
        embedo.set_footer(text="ScaryShop V4 | Recrutements",
                          icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        embedc = discord.Embed(
            description="👨🏼‍💼 **► Recrutement Vendeurs ScaryShop** \n \n __Conditions à respecter:__ \n \n > • Avoir minimum **13** ans \n > • Avoir un orthographe **correct** \n > • Pouvoir répondre à **toute commande** \n > • Avoir un **minimum de stuff** et être **avancé** dans **les métiers** \n \n Les recrutements sont clos pour le moment. Vous serez informé quand ils seront de nouveau ouvert. \n \n Bonne chance à vous!",
            color=0x00FFFF)
        embedc.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/705448891570716752/913711303493840916/recrutement.png")
        embedc.set_footer(text="ScaryShop V4 | Recrutements",
                          icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        if status == "open":
            await ctx.send(embed=embedo, components=[
                Button(style=ButtonStyle.URL, label="Formulaire Vendeur", url="https://bit.ly/3gGqw0a",
                       custom_id="vendeur")])
            await ctx.message.delete()
        if status == "close":
            await ctx.send(embed=embedc)
            await ctx.message.delete()
        else:
            return


# https://bit.ly/3gGqw0a

def setup(bot):
    bot.add_cog(Vendeurs(bot))
