from discord.ext import commands
from discord_components import *
from discord_slash.utils.manage_components import *


class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def interroles(self, ctx):

        em = discord.Embed(title="__**Cliquez sur le bouton puis cochez dans le menu les rôles que vous souhaitez:**__",
                           description=" > <a:Economie:808291607396089876> **Économie** <a:fl:802827880618000414> Ajout d'item, changement de prix... \n \n > 🎉 **Giveaway** <a:fl:802827880618000414> Soyez prévenu lorsque nous lançons un giveaway. \n \n > <a:Sondage:808290725816041472> **Sondages** <a:fl:802827880618000414> Donner votre avis dans nos nombreux sondages. \n \n > <a:LuckyBloc:808290712683675658> **Lucky Bloc** <a:fl:802827880618000414> Recevez une notification quand un vendeur met des Lucky Blocs en vente. \n \n > <a:VenteSpeciale:808290722692202496> **Vente Spéciale** <a:fl:802827880618000414> Un endroit où les prix sont cassés. \n \n > 📪 **Quête du jour** <a:fl:802827880618000414> Si un vendeur vend la quête du jour, vous serez notifié. \n \n > <a:Enchere:808290709404516402> **Enchère** <a:fl:802827880618000414> Des enchères sont souvent proposées. Profitez-en! \n \n > 📜 **Patch-Note** <a:fl:802827880618000414> Soyez informé lorsque des nouveautés arrivent sur le serveur. \n \n > 📻 **Publicité** <a:fl:802827880618000414> Soyez informé lorsque des publicités sont faites sur le serveur.",
                           color=0xFF7F00)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303774855168/roles.png")
        em.set_footer(text="ScaryBot - Rôles",
                      icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=em, components=[
            [Button(style=ButtonStyle.blue, label="Ajout de Rôle", custom_id="addroles"),
             Button(style=ButtonStyle.red, label="Retrait de Rôle", custom_id="removeroles")]])
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interactions: Interaction):
        guild = self.bot.get_guild(705089080693751850)
        rolebarre = guild.get_role(733678420764000266)
        sepa = guild.get_role(838448105308684368)
        if interactions.custom_id == "addroles":
            author = interactions.user

            await interactions.respond(
                content="<a:fl:802827880618000414> **Cliquez sur le/les rôle(s) que vous souhaitez obtenir!**",
                components=[Select(placeholder="Sélectionnez les rôles que vous souhaitez !",
                                   min_values=1,
                                   max_values=9,
                                   options=[
                                       SelectOption(
                                           label="Economie",
                                           value="economie",
                                           emoji="🪙"
                                       ),
                                       SelectOption(
                                           label="Giveaway",
                                           value="giveaway",
                                           emoji="🎉"
                                       ),
                                       SelectOption(
                                           label="Sondages",
                                           value="sondages",
                                           emoji="📊"
                                       ),
                                       SelectOption(
                                           label="Lucky Blocs",
                                           value="lucky",
                                           emoji="🍀"
                                       ),
                                       SelectOption(
                                           label="Vente Spéciale",
                                           value="ventespeciale",
                                           emoji="🏷"
                                       ),
                                       SelectOption(
                                           label="Quête du Jour",
                                           value="qdj",
                                           emoji="📪"
                                       ),
                                       SelectOption(
                                           label="Enchères",
                                           value="enchere",
                                           emoji="⚖️"
                                       ),
                                       SelectOption(
                                           label="Patch-Note",
                                           value="patchnote",
                                           emoji="📜"
                                       ),
                                       SelectOption(
                                           label="Publicité",
                                           value="pub",
                                           emoji="📻"
                                       ),
                                   ])]
            )

            while True:
                try:
                    event = await self.bot.wait_for("select_option", check=None)

                    for value in event.values:
                        await event.respond(type=6)
                        if value == "economie":
                            role = interactions.guild.get_role(705405332230504491)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Économie** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Économie** sur le ***ScaryShop*** !")

                        elif value == "giveaway":
                            role = interactions.guild.get_role(705408472711299113)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Giveaway** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Giveaway** sur le ***ScaryShop*** !")

                        elif value == "sondages":
                            role = interactions.guild.get_role(705410033562681466)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Sondages** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Sondages** sur le ***ScaryShop*** !")

                        elif value == "lucky":
                            role = interactions.guild.get_role(705411725599703133)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Lucky Bloc** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Lucky Bloc** sur le ***ScaryShop*** !")

                        elif value == "ventespeciale":
                            role = interactions.guild.get_role(705413291240980510)
                            if role in author.roles:
                                await author.send(
                                    "Vous possédez déjà le rôle **Vente Spéciale** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Vente Spéciale** sur le ***ScaryShop*** !")

                        elif value == "qdj":
                            role = interactions.guild.get_role(706473637372231742)
                            if role in author.roles:
                                await author.send(
                                    "Vous possédez déjà le rôle **Quête du Jour** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Quête du Jour** sur le ***ScaryShop*** !")

                        elif value == "enchere":
                            role = interactions.guild.get_role(714866835589431298)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Enchère** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Enchère** sur le ***ScaryShop*** !")

                        elif value == "patchnote":
                            role = interactions.guild.get_role(840149202998657044)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Patch-Note** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Patch-Note** sur le ***ScaryShop*** !")

                        elif value == "pub":
                            role = interactions.guild.get_role(868842519566376990)
                            if role in author.roles:
                                await author.send("Vous possédez déjà le rôle **Publicité** sur le ***ScaryShop*** !")
                            else:
                                await author.add_roles(role)
                                await author.send(
                                    "Vous possédez maintenant le rôle **Publicité** sur le ***ScaryShop*** !")

                    await author.add_roles(rolebarre)
                    await author.add_roles(sepa)
                    return

                except discord.NotFound:
                    print("error")
                    return

        if interactions.custom_id == "removeroles":
            author = interactions.user

            await interactions.respond(
                content="<a:fl:802827880618000414> **Cliquez sur le/les rôle(s) que vous souhaitez retirer !**",
                components=[Select(placeholder="Sélectionnez les rôles que vous souhaitez retirer !",
                                   min_values=1,
                                   max_values=9,
                                   options=[
                                       SelectOption(
                                           label="Economie",
                                           value="economier",
                                           emoji="🪙"
                                       ),
                                       SelectOption(
                                           label="Giveaway",
                                           value="giveawayr",
                                           emoji="🎉"
                                       ),
                                       SelectOption(
                                           label="Sondages",
                                           value="sondagesr",
                                           emoji="📊"
                                       ),
                                       SelectOption(
                                           label="Lucky Blocs",
                                           value="luckyr",
                                           emoji="🍀"
                                       ),
                                       SelectOption(
                                           label="Vente Spéciale",
                                           value="ventespecialer",
                                           emoji="🏷"
                                       ),
                                       SelectOption(
                                           label="Quête du Jour",
                                           value="qdjr",
                                           emoji="📪"
                                       ),
                                       SelectOption(
                                           label="Enchères",
                                           value="encherer",
                                           emoji="⚖️"
                                       ),
                                       SelectOption(
                                           label="Patch-Note",
                                           value="patchnoter",
                                           emoji="📜"
                                       ),
                                       SelectOption(
                                           label="Publicité",
                                           value="pubr",
                                           emoji="📻"
                                       ),
                                   ])]
            )

            while True:
                try:
                    event = await self.bot.wait_for("select_option", check=None)

                    for value in event.values:
                        await event.respond(type=6)
                        if value == "economier":
                            role = interactions.guild.get_role(705405332230504491)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send("Vous ne possédez plus le rôle **Économie** sur le ***ScaryShop*** !")
                            else:
                                await author.send("Vous ne possédez pas le rôle **Économie** sur le ***ScaryShop*** !")

                        elif value == "giveawayr":
                            role = interactions.guild.get_role(705408472711299113)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send("Vous ne possédez plus le rôle **Giveaway** sur le ***ScaryShop*** !")
                            else:
                                await author.send("Vous ne possédez pas le rôle **Giveaway** sur le ***ScaryShop*** !")

                        elif value == "sondagesr":
                            role = interactions.guild.get_role(705410033562681466)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send("Vous ne possédez plus le rôle **Sondage** sur le ***ScaryShop*** !")
                            else:
                                await author.send("Vous ne possédez pas le rôle **Sondage** sur le ***ScaryShop*** !")

                        elif value == "luckyr":
                            role = interactions.guild.get_role(705411725599703133)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send(
                                    "Vous ne possédez plus le rôle **Lucky Bloc** sur le ***ScaryShop*** !")
                            else:
                                await author.send(
                                    "Vous ne possédez pas le rôle **Lucky Bloc** sur le ***ScaryShop*** !")
                        elif value == "ventespecialer":
                            role = interactions.guild.get_role(705413291240980510)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send(
                                    "Vous ne possédez plus le rôle **Vente Spéciale** sur le ***ScaryShop*** !")
                            else:
                                await author.send(
                                    "Vous ne possédez pas le rôle **Vente Spéciale** sur le ***ScaryShop*** !")

                        elif value == "qdjr":
                            role = interactions.guild.get_role(706473637372231742)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send(
                                    "Vous ne possédez plus le rôle **Quête du Jour** sur le ***ScaryShop*** !")
                            else:
                                await author.send(
                                    "Vous ne possédez pas le rôle **Quête du Jour** sur le ***ScaryShop*** !")

                        elif value == "encherer":
                            role = interactions.guild.get_role(714866835589431298)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send("Vous ne possédez plus le rôle **Enchère** sur le ***ScaryShop*** !")
                            else:
                                await author.send("Vous ne possédez pas le rôle **Enchère** sur le ***ScaryShop*** !")

                        elif value == "patchnoter":
                            role = interactions.guild.get_role(840149202998657044)
                            if role in author.roles:
                                await author.remove_roles(role)
                                await author.send(
                                    "Vous ne possédez plus le rôle **Patch-Note** sur le ***ScaryShop*** !")
                            else:
                                await author.send(
                                    "Vous ne possédez pas le rôle **Patch-Note** sur le ***ScaryShop*** !")

                        elif value == "pubr":
                            pubrole = interactions.guild.get_role(868842519566376990)
                            if pubrole in author.roles:
                                await author.remove_roles(pubrole)
                                await author.send(
                                    "Vous ne possédez plus le rôle **Publicité** sur le ***ScaryShop*** !")
                            else:
                                await author.send("Vous ne possédez pas le rôle **Publicité** sur le ***ScaryShop*** !")

                        return

                except discord.NotFound:
                    print("error")
                    return


def setup(bot):
    bot.add_cog(Autorole(bot))
