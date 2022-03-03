import discord
from discord.ext import commands


class Conditionspart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def conditionspart(self, ctx, membres_sans_mention, membres_here, membres_everone):
        em = discord.Embed(title="🎲 ► Conditions Partenariats",
                           description=f"Pour établir un partenariat avec le ScaryShop, voici les mentions que vous pouvez espérer avoir selon vos membres: \n \n > **•** __**Entre {membres_sans_mention} et {membres_here} Membres:**__ \n ScaryShop V3 <a:fl:802827880618000414> Aucune Mention \n Votre serveur <a:fl:802827880618000414> @everyone \n \n > **•** __**Entre {membres_here} et {membres_everone} Membres:**__ \n ScaryShop V3 <a:fl:802827880618000414> @here \n Votre serveur <a:fl:802827880618000414> @everyone \n \n > **•** __**Plus de {membres_everone} Membres:**__ \n ScaryShop V3 <a:fl:802827880618000414> @everyone \n Votre serveur <a:fl:802827880618000414> @everyone",
                           color=0xFFA500)
        em.set_footer(text="⇾ Merci de passer par le support pour faire votre demande.")
        em.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/705448891570716752/913711303305076756/partenariat.png")
        await ctx.send(embed=em)
        await ctx.message.delete()


###!conditionspart 300 600 900

def setup(bot):
    bot.add_cog(Conditionspart(bot))
