import discord
from discord.ext import commands
from discord_slash import SlashCommand, ButtonStyle
from discord_slash.utils.manage_components import *
from discord_components import *

class Moderateurs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def rcm(self, ctx, status):
        embedo = discord.Embed(description = "👨🏼‍💼 **► Recrutement Modérateurs ScaryShop** \n \n __Conditions à respecter:__ \n \n > • Avoir minimum **16** ans \n > • Être **souvent disponible** *ET* sur **PC** \n > • Avoir un microphone **correct** \n > • **Connaître** un minimum le **fonctionnement du Shop** \n > • Savoir juger avec des **sanctions adéquates** \n > • Ne **pas avoir** eu de **sanctions** sur le shop \n \n Si vous respectez ces conditions, je vous invite à cliquer sur le bouton ci-dessous pour accéder au formulaire. \n \n Bonne chance à vous!", color = 0x9A06AC)
        embedo.set_thumbnail(url = "https://cdn.discordapp.com/attachments/705448891570716752/913711303493840916/recrutement.png")
        embedo.set_footer(text = "ScaryShop V4 | Recrutements")

        embedc = discord.Embed(description = "👨🏼‍💼 **► Recrutement Modérateurs ScaryShop** \n \n __Conditions à respecter:__ \n \n > • Avoir minimum **16** ans \n > • Être **souvent disponible** *ET* sur **PC** \n > • Avoir un microphone **correct** \n > • **Connaître** un minimum le **fonctionnement du Shop** \n > • Savoir juger avec des **sanctions adéquates** \n > • Ne **pas avoir** eu de **sanctions** sur le shop \n \n Les recrutements sont clos pour le moment. Vous serez informé quand ils seront de nouveau ouvert. \n \n Bonne chance à vous!", color = 0x9A06AC)
        embedc.set_thumbnail(url = "https://cdn.discordapp.com/attachments/705448891570716752/913711303493840916/recrutement.png")
        embedc.set_footer(text = "ScaryShop V4 | Recrutements")

        if status == "open":
            await ctx.send(embed = embedo, components=[Button(style=ButtonStyle.URL, label = "Formulaire Modérateur", url = "https://bit.ly/2S2yV49", custom_id = "modo")])
            await ctx.message.delete()
        if status == "close":
            await ctx.send(embedc)
            await ctx.message.delete()
        else:
            return

def setup(bot):
    bot.add_cog(Moderateurs(bot))