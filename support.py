from discord.ext import commands
from discord_components import *
from discord_slash.utils.manage_components import *


class Support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def support(self, ctx):

        embed = discord.Embed(title="**Contacter le support __𝗦𝗰𝗮𝗿𝘆𝗦𝗵𝗼𝗽__**",
                              description="> Pour contacter le support, cliquez sur le bouton ci-dessous. Vous pourrez ensuite sélectionné votre demande dans le menu ouvert. \n \n __*Voici la liste des demandes:*__ \n \n > ⬜ Demande de Partenariat \n > 🟦 Achat de Grade <#768491281982292020> \n > 🟥 Récupération des récompenses \n > 🟩 Report un joueur \n > ⬛ Demande d'enchère \n > 🟧 Questions \n > 🟨 Autres \n \n Patientez ensuite qu'un membre du support s'occupe de vous. Merci!",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/705448891570716752/913711303078576188/support.png")
        embed.set_footer(text="ScaryBot - Support",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.blue, label="☎️ Support", custom_id="support")])
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interaction: Interaction):
        guild = self.bot.get_guild(705089080693751850)
        catego = self.bot.get_channel(765634020976885822)
        role = guild.get_role(770373622928900166)
        modo1 = guild.get_role(832699561255501834)
        respench = guild.get_role(753490443819417741)
        if interaction.custom_id == "support":
            author = interaction.user

            await interaction.respond(
                content="<a:fl:802827880618000414> **Cliquez sur la catégorie que vous souhaitez ouvrir !**",
                components=
                [Select(placeholder="Quel est l'objet de votre demande ?",
                        options=[
                            SelectOption(
                                label="Demande de Partenariat",
                                description="Proposer un partenariat avec votre serveur !",
                                value="partenariat",
                                emoji="⬜"
                            ),
                            SelectOption(
                                label="Achat de Grade",
                                description="Procéder à l'achat d'un grade.",
                                value="achat",
                                emoji="🟦"
                            ),
                            SelectOption(
                                label="Récupération des récompenses",
                                value="recompenses",
                                description="Récupérer vos récompenses de Giveaway ou d'event !",
                                emoji="🟥"
                            ),
                            SelectOption(
                                label="Signaler un joueur",
                                value="report",
                                description="Report le mauvais comportement d'un utilisateur !",
                                emoji="🟩"
                            ),
                            SelectOption(
                                label="Demande d'enchère",
                                value="enchere",
                                description="Faire une proposition d'enchère.",
                                emoji="⬛"
                            ),
                            SelectOption(
                                label="Question",
                                value="question",
                                description="Poser une question au staff du ScaryShop.",
                                emoji="🟧"
                            ),
                            SelectOption(
                                label="Autres",
                                value="autres",
                                description="Pour toutes autres demandes non présentes ci-dessus.",
                                emoji="🟨"
                            ),
                        ])]
                )

            while True:
                try:
                    event = await self.bot.wait_for("select_option", check=None)

                    for value in event.values:

                        if value == "partenariat":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("⬜〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)
                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)
                            await ticket_channel.set_permissions(respench, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Avant de faire une demande de partenariat, merci de vous référer aux conditions (<#797397350095912981>). Une fois ceci fait, envoyez le lien de votre serveur Discord.",
                                color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "achat":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("🟦〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Pour acheter un grade ou une mention, je vous laisse procéder au payement au compte `ScaryShop` au montant du grade/mention. Le screen doit contenir: \n > • Pseudo en haut à gauche \n > • Date et heure en bas à droite \n > • Paiement dans le chat \n *(Si le screen ne comprend pas une de ces informations, il sera refusé. Pour éviter ceci, un exemple est présent ci-dessous)* \n \n Merci de préciser ensuite ce que vous souhaitez. \n \n __Rappel des prix:__ \n \n > Grade Sorcière -> **5.000$ / mois** \n > Grade Faucheuse -> **10.000$ / mois (27.000$/3 mois)** \n > Grade Fantôme -> **15.000$ / mois (40.000$/3 mois)** \n > Grade Assassin -> **30.000$ / mois (82.000$/3 mois)** \n \n > Mention @here -> **Indisponible** \n > Mention @everyone -> **Indisponible**",
                                color=0x00a8ff)
                            em.set_image(
                                url="https://cdn.discordapp.com/attachments/362608930469314560/888805081884012554/unknown.png")

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "recompenses":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("🟥〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Pour récuperer vos récompenses, merci de nous dire ce que vous devez avoir. Pour les évents invites, veuillez faire la commande `/recompenses` et suivez les indications.",
                                color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "report":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("🟩〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Vous souhaitez report un joueur qui a un comportement inadéquat, merci de nous donner toutes les preuves ci-dessous avec le pseudo et tag du joueur et également son ID.",
                                color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "enchere":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("⬛〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(respench, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Pour faire une demande d'enchère, merci de nous donner les informations suivantes: \n \n > *Item à vendre:* \n > *Prix de départ:* \n > *Durée:* (3 jours maximum) \n > *Screen de preuve:* \n > *Pas de l'enchère (ex: 1.000$ en  1.000$):* \n \n Nous nous réservons le droit de lancer l'enchère quand nous le souhaitons.",
                                color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "question":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("🟧〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Merci de poser votre question ci-dessous, nous tâcherons d'y répondre le plus rapidement possible.",
                                color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return
                        if value == "autres":
                            await event.respond(type=7)
                            ticket_channel = await guild.create_text_channel("🟨〡{}".format(author.name),
                                                                             category=catego)
                            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False,
                                                                 read_messages=False)

                            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(modo1, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True,
                                                                 add_reactions=True, embed_links=True,
                                                                 attach_files=True, read_message_history=True,
                                                                 external_emojis=True)

                            em = discord.Embed(
                                title="Demande de support de {}#{}".format(author.name, author.discriminator),
                                description="Merci de faire votre demande ci-dessous.", color=0x00a8ff)

                            await ticket_channel.send(
                                f"Bienvenue {author.mention}. Un <@&770373622928900166> va s'occuper de vous.")
                            await ticket_channel.send(embed=em)
                            return

                except discord.NotFound:
                    print("error")
                    return


def setup(bot):
    bot.add_cog(Support(bot))
