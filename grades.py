import discord
from discord.ext import commands


class Grades(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # <a:scarycheck:835499517977690122>
    # <a:scarywrong:835499521341128746>

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sorciere(self, ctx):
        em = discord.Embed(title="Grade Sorcière | ScaryShop V4",
                           description="__**Avantages du grades:**__ \n \n <a:scarycheck:835499517977690122> -3% sur tout le catalogue \n \n <a:scarycheck:835499517977690122> Possibilité de faire 2 commandes en même temps \n \n <a:scarycheck:835499517977690122> Commandes prioritaires\n \n <a:scarycheck:835499517977690122> Salons textuels et vocaux privés \n \n <a:scarycheck:835499517977690122> Rabais de 5% sur le prix des partenariats \n \n <a:scarywrong:835499521341128746> Accès aux Giveaways V.I.P  \n \n <a:scarywrong:835499521341128746> Accès au channel <#705389537127432203> \n \n <a:scarywrong:835499521341128746> Accès au channel <#705389017943769158> \n \n <a:scarywrong:835499521341128746> Accès au channel <#705122397300195484> \n \n <a:scarywrong:835499521341128746> Couleur de grade personnalisé \n \n <a:scarywrong:835499521341128746> Grade personnalisé \n \n <a:scarywrong:835499521341128746> Proposer des sondages \n \n <a:scarywrong:835499521341128746> Apprendre les mises à jour en avance \n \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `1 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `5.000$`",
                           color=0x8b13db)
        em.set_image(url="https://cdn.discordapp.com/attachments/705448891570716752/913880857629061150/PROJET.png")
        em.set_footer(text="⇾ Pour commander un grade, rendez-vous dans le support.")
        await ctx.send(embed=em)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def faucheuse(self, ctx):
        em = discord.Embed(title="Grade Faucheuse | ScaryShop V4",
                           description="__**Avantages du grades:**__ \n \n <a:scarycheck:835499517977690122> -7% sur tout le catalogue \n \n <a:scarycheck:835499517977690122> Possibilité de faire 3 commandes en même temps \n \n <a:scarycheck:835499517977690122> Commandes prioritaires \n \n <a:scarycheck:835499517977690122> Salons textuels et vocaux privés \n \n <a:scarycheck:835499517977690122> Rabais de 10% sur le prix des partenariats \n \n <a:scarycheck:835499517977690122> Accès aux Giveaways V.I.P \n \n <a:scarycheck:835499517977690122> Accès au channel <#705389537127432203> \n \n <a:scarywrong:835499521341128746> Accès au channel <#705389017943769158> \n \n <a:scarywrong:835499521341128746> Accès au channel <#705122397300195484> \n \n <a:scarywrong:835499521341128746> Couleur de grade personnalisé \n \n <a:scarywrong:835499521341128746> Grade personnalisé \n \n <a:scarywrong:835499521341128746> Proposer des sondages \n \n <a:scarywrong:835499521341128746> Apprendre les mises à jour en avance \n \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `1 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `10.000$` \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `3 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `27.000$`",
                           color=0x5c5c5c)
        em.set_image(url="https://cdn.discordapp.com/attachments/705448891570716752/913880857968783390/PROJET.png")
        em.set_footer(text="⇾ Pour commander un grade, rendez-vous dans le support.")
        await ctx.send(embed=em)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def fantome(self, ctx):
        em = discord.Embed(title="Grade Fantôme | ScaryShop V4",
                           description="__**Avantages du grades:**__ \n \n <a:scarycheck:835499517977690122> -10% sur tout le catalogue \n \n <a:scarycheck:835499517977690122> Commandes illimitées \n \n <a:scarycheck:835499517977690122> Commandes prioritaires \n \n <a:scarycheck:835499517977690122> Salons textuels et vocaux privés \n \n <a:scarycheck:835499517977690122> Rabais de 15% sur le prix des partenariats \n \n <a:scarycheck:835499517977690122> Accès aux Giveaways V.I.P \n \n <a:scarycheck:835499517977690122> Accès au channel <#705389537127432203> \n \n <a:scarycheck:835499517977690122> Accès au channel <#705389017943769158> \n \n <a:scarycheck:835499517977690122> Accès au channel <#705122397300195484> \n \n <a:scarycheck:835499517977690122> Couleur de grade personnalisé \n \n <a:scarywrong:835499521341128746> Grade personnalisé \n \n <a:scarywrong:835499521341128746> Proposer des sondages \n \n <a:scarywrong:835499521341128746> Apprendre les mises à jour en avance \n \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `1 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `15.000$` \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `3 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `40.000$`",
                           color=0xff9b65)
        em.set_image(url="https://cdn.discordapp.com/attachments/705448891570716752/913880858241417256/PROJET.png")
        em.set_footer(text="⇾ Pour commander un grade, rendez-vous dans le support.")
        await ctx.send(embed=em)
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def assassin(self, ctx):
        em = discord.Embed(title="Grade Assassin | ScaryShop V4",
                           description="__**Avantages du grades:**__ \n \n <a:scarycheck:835499517977690122> -15% sur tout le catalogue \n \n <a:scarycheck:835499517977690122> Commandes illimitées \n \n <a:scarycheck:835499517977690122> Commandes prioritaires \n \n <a:scarycheck:835499517977690122> Salons textuels et vocaux privés \n \n <a:scarycheck:835499517977690122> Rabais de 20% sur le prix des partenariats \n \n <a:scarycheck:835499517977690122> Accès aux Giveaways V.I.P \n \n <a:scarycheck:835499517977690122> Accès au channel <#705389537127432203> \n \n <a:scarycheck:835499517977690122> Accès au channel <#705389017943769158> \n \n <a:scarycheck:835499517977690122> Accès au channel <#705122397300195484> avec mention <@&868842519566376990> \n \n <a:scarycheck:835499517977690122> Couleur de grade personnalisé \n \n <a:scarycheck:835499517977690122> Grade personnalisé \n \n <a:scarycheck:835499517977690122> Proposer des sondages \n \n <a:scarycheck:835499517977690122> Apprendre les mises à jour en avance \n \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `1 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `30.000$` \n \n > <a:TIME:869502326031913011> Durée du grade <a:fl:802827880618000414> `3 mois` \n > 💸 Prix du grade <a:fl:802827880618000414> `82.000$`",
                           color=0x373f6f)
        em.set_image(url="https://cdn.discordapp.com/attachments/705448891570716752/913880858535006258/PROJET.png")
        em.set_footer(text="⇾ Pour commander un grade, rendez-vous dans le support.")
        await ctx.send(embed=em)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Grades(bot))
