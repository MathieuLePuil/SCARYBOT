import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
from discord_slash import SlashCommand, ButtonStyle
import datetime
import json
import random
from discord import Permissions
from colorama import Fore, Style
from discord_slash.utils.manage_components import *
from discord_components import *

class Commande(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(self, interaction: Interaction):
        guild = self.bot.get_guild(705089080693751850)
        catego = self.bot.get_channel(733746634172923904)
        role = guild.get_role(705093311248990312)
        modo = guild.get_role(832699561255501834)
        resprole = guild.get_role(849934378175823874)
        log_channel = self.bot.get_channel(935648359027466380)
        channel = interaction.channel
        if interaction.custom_id == "commande":
            await interaction.respond(type=7)

            with open("nbrcommande.json", 'r') as f:
                data = json.load(f)

            ticket_number = int(data["ticket-counter"])
            ticket_number += 1

            author = interaction.user

            ticket_channel = await guild.create_text_channel(f"🔴〡{author.name}-{ticket_number}", category=catego)
            channelid = ticket_channel.id
            await self.when_commande(ticket_channel)
            channel = ticket_channel
            commandeinfo = await self.get_commande_data()
            await ticket_channel.set_permissions(guild.get_role(guild.id), send_messages=False, read_messages=False)

            await ticket_channel.set_permissions(role, send_messages=False, read_messages=False, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=False,
                                                 external_emojis=True)
            await ticket_channel.set_permissions(resprole, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True, send_tts_messages=True, manage_channels=True, manage_permissions=True)

            await ticket_channel.set_permissions(author, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)

            em = discord.Embed(title="Commande de {}#{}".format(author.name, author.discriminator),
                               description="Veuillez cliquer sur le bouton ci-dessous pour lancer la procédure de commande. Vous pourrez annuler celle-ci du moment qu'elle n'est pas prise.",
                               color=0xFFA500)

            await ticket_channel.send(
                f"Bienvenue {author.mention} sur l'espace de commande. L'<@&705093311248990312> va s'occuper de vous.")
            await ticket_channel.send(embed=em,
                                      components=[Button(style=ButtonStyle.green, label="Lancer la procédure de commande",
                                                         custom_id="procedure")])

            try:
                commandeinfo[str(ticket_channel.id)]["Numero"] = ticket_number
            except KeyError:
                print(f"Il y a une erreur!")

            with open("commande.json", "w") as f:
                commandeinfo = json.dump(commandeinfo, f, indent=2)

            data["ticket-counter"] = int(ticket_number)

            with open("nbrcommande.json", 'w') as f:
                json.dump(data, f)

        elif interaction.custom_id == "procedure":
            await interaction.respond(type=7)
            author = interaction.user

            await self.when_commande(interaction.channel)
            commandeinfo = await self.get_commande_data()

            reduction = "Aucune"

            troispc = interaction.guild.get_role(836949397089812511)
            septpc = interaction.guild.get_role(833274658467348480)
            dixpc = interaction.guild.get_role(833788987516256298)
            quinzepc = interaction.guild.get_role(871680557602439189)
            if troispc in author.roles:
                reduction = "- 3%"
            if septpc in author.roles:
                reduction = "- 7%"
            if dixpc in author.roles:
                reduction = "- 10%"
            if quinzepc in author.roles:
                reduction = "- 15%"

            em1 = discord.Embed(description="Quel item souhaitez-vous commander? (Même nom que dans le catalogue)",
                                color=0xFFA500)
            em2 = discord.Embed(description="En quelle quantité souhaitez-vous cet item?", color=0xFFA500)
            em3 = discord.Embed(description="Quel est le prix de votre commande? (sans le $ ni la réduction)",
                                color=0xFFA500)
            em4 = discord.Embed(description="Quel est votre pseudo IG?", color=0xFFA500)

            await interaction.channel.send(embed=em1)

            try:
                item = await self.bot.wait_for("message", timeout=60,
                                          check=lambda msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=1, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Veuillez réiterer votre commande.", delete_after = 10)
                return

            message = await interaction.channel.send(embed=em2)

            try:
                quantite = await self.bot.wait_for("message", timeout=60,
                                              check=lambda msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=3, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Veuillez réiterer votre commande.", delete_after = 10)
                return

            message = await interaction.channel.send(embed=em3)

            try:
                prix = await self.bot.wait_for("message", timeout=60,
                                          check=lambda msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=5, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Veuillez réiterer votre commande.", delete_after = 10)
                return

            message = await interaction.channel.send(embed=em4)

            try:
                pseudo = await self.bot.wait_for("message", timeout=60,
                                            check=lambda msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=7, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Veuillez réiterer votre commande.", delete_after = 10)
                return

            await interaction.channel.purge(limit=None, check=lambda msg: not msg.pinned)

            ticket_number = commandeinfo[str(channel.id)]["Numero"]

            embed = discord.Embed(
                description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item.content}** \n > *`Quantité souhaité:`* **{quantite.content}** \n > *`Prix total:`* **{prix.content}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudo.content}** \n > *`Pseudo Discord:`* **{author.mention}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n Commande n°**{ticket_number}**",
                color=0xFFA500, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="⇾ Vous serez notifié lorsqu'un vendeur aura pris votre commande.")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

            emb = discord.Embed(title=f"Commande n°{ticket_number}", description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item.content}** \n > *`Quantité souhaité:`* **{quantite.content}** \n > *`Prix total:`* **{prix.content}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudo.content}** \n > *`Pseudo Discord:`* **{author.mention}**  \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n 💠 __**Statut:**__ \n \n > 🔔 **Non prise**", color=0xFFA500, timestamp=datetime.datetime.utcnow())
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

            emp = discord.Embed(title="**Suivi du votre commande**",
                                description=f"<a:fleche_new:915897203392917514> Votre commande à été signalé aux vendeurs. \n \n > *`Item commandé:`* **{item.content}** \n > *`Quantité souhaité:`* **{quantite.content}** \n > *`Prix total:`* **{prix.content}**$ \n \n \n 🛒 __**Vos informations:**__ \n \n > *`Pseudo Discord:`* **{interaction.user.mention}** \n > *`Pseudo IG:`* **{pseudo.content}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n Commande n°**{ticket_number}**",
                                color=0xFFA500, timestamp=datetime.datetime.utcnow())
            emp.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")
            emp.set_footer(
                text="⇾ Vous serez notifié sur le serveur lorsqu'un vendeur aura pris votre commande. Sinon, elle sera close au bout de 2 jours.")

            if reduction == "Aucune":
                message1 = await interaction.channel.send(embed=embed,
                                                          components=[[
                                                              Button(style=ButtonStyle.blue, label="Prendre la commande",
                                                                     id="takecommande"),
                                                              Button(style=ButtonStyle.red, label="Annuler la commande",
                                                                     id="delcommande")]])
            else:
                message1 = await interaction.channel.send(embed=embed,
                                                          components=[[
                                                              Button(style=ButtonStyle.blue, label="Prendre la commande",
                                                                     id="takecommande"),
                                                              Button(style=ButtonStyle.red, label="Annuler la commande",
                                                                     id="delcommande"),
                                                              Button(style=ButtonStyle.green, label="Définir nouveau prix",
                                                                     id="newprix")]])

            await message1.pin()
            message2 = await log_channel.send(embed=emb)
            message3 = await interaction.author.send(embed=emp)
            messages = await interaction.channel.history(limit=1).flatten()
            for message in messages:
                await message.delete()

            try:
                commandeinfo[str(channel.id)]["Acheteur (name)"] = author.name
                commandeinfo[str(channel.id)]["Acheteur (discriminator)"] = author.discriminator
                commandeinfo[str(channel.id)]["Acheteur (ID)"] = author.id
                commandeinfo[str(channel.id)]["Item"] = item.content
                commandeinfo[str(channel.id)]["Quantite"] = quantite.content
                commandeinfo[str(channel.id)]["Prix"] = prix.content
                commandeinfo[str(channel.id)]["Pseudo IG"] = pseudo.content
                commandeinfo[str(channel.id)]["Reduction"] = reduction
                commandeinfo[str(channel.id)]["Message1"] = message1.id
                commandeinfo[str(channel.id)]["Logs"] = message2.id
            except KeyError:
                print(f"Il y a une erreur!")

            with open("commande.json", "w") as f:
                commandeinfo = json.dump(commandeinfo, f, indent=2)

            await interaction.channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)
            await interaction.channel.set_permissions(modo, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)
            await interaction.channel.send("<@&705093311248990312>", delete_after = 1)



        elif interaction.custom_id == "newprix":
            await interaction.respond(type=7)
            author = interaction.user

            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()

            vendeur = interaction.guild.get_role(705093311248990312)

            if vendeur in author.roles:
                em = discord.Embed(description = "Quel est le nouveau prix de la commande? (sans le $)", color = 0xFFA500)

                message = await interaction.channel.send(embed=em)

                try:
                    newprix = await self.bot.wait_for("message", timeout=60,
                                                check=lambda msg: interaction.author == msg.author and channel == msg.channel)
                except:
                    await interaction.channel.send("Veuillez recommencer le changement de prix.")
                    return

                try:
                    commandeinfo[str(channel.id)]["Prix"] = newprix.content
                except KeyError:
                    print(f"Il y a une erreur!")

                with open("commande.json", "w") as f:
                    commandeinfo = json.dump(commandeinfo, f, indent=2)

                await interaction.channel.purge(limit=2, check=lambda msg: not msg.pinned)

                message_newprix = await interaction.channel.send(f"Le *nouveau prix* est **{newprix.content}$**.", delete_after = 5)



        elif interaction.custom_id == "takecommande":
            await interaction.respond(type=7)
            author = interaction.user

            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()

            acheteurname = commandeinfo[str(channel.id)]["Acheteur (name)"]
            acheteurid = commandeinfo[str(channel.id)]["Acheteur (ID)"]
            item = commandeinfo[str(channel.id)]["Item"]
            quantite = commandeinfo[str(channel.id)]["Quantite"]
            prix = commandeinfo[str(channel.id)]["Prix"]
            pseudoig = commandeinfo[str(channel.id)]["Pseudo IG"]
            reduction = commandeinfo[str(channel.id)]["Reduction"]
            message1 = commandeinfo[str(channel.id)]["Message1"]
            ticket_number = commandeinfo[str(channel.id)]["Numero"]
            logsmessage = commandeinfo[str(channel.id)]["Logs"]

            vendeur = interaction.guild.get_role(705093311248990312)

            if vendeur in author.roles:

                await interaction.channel.set_permissions(role, send_messages=False, read_messages=False, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=False,
                                                 external_emojis=True)
                await interaction.channel.set_permissions(author, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)
                await interaction.channel.set_permissions(modo, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)

                await interaction.channel.edit(name = f"🟢〡{acheteurname}-{ticket_number}")
                embed = discord.Embed(title = "<a:load:899616055213817886> Commande en cours de préparation...",
                description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`Pseudo Discord:`* **<@{acheteurid}>** \n > *`ID:`* **{acheteurid}** \n > *`Réduction:`* **{reduction}** \n \n \n 💼 __**Informations du vendeur:**__ \n \n > *`Pseudo vendeur:`* **{author.mention}** \n > *`ID vendeur:`* **{author.id}** \n \n Commande n°**{ticket_number}**",
                color=0xFFA500, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text="⇾ Vous serez notifié lorsque votre commande sera prête.")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")
                message2 = await interaction.channel.send(embed = embed,
                                                components=[[
                                                  Button(style=ButtonStyle.blue, label="Livrer la commande",
                                                         id="endcommande"),
                                                  Button(style=ButtonStyle.green, label="Whitelist",
                                                         id="whitelist")]])
                await interaction.channel.send(f"<@{acheteurid}>", delete_after = 1)
                await message2.pin()
                messages = await interaction.channel.history(limit=1).flatten()
                for message in messages:
                    await message.delete()
            else:
                await interaction.channel.send(
                    "Vous **n'êtes pas Vendeur**. Vous n'avez donc ***pas la permission de prendre des commandes***.", delete_after = 5)
                return

            msg = await channel.fetch_message(message1)
            logsmsg = await log_channel.fetch_message(logsmessage)
            await msg.delete()

            emb = discord.Embed(title=f"Commande n°{ticket_number}", description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n 💠 __**Statut:**__ \n \n > 🔔 **En cours de préparation** \n > *`Vendeur:`* {interaction.user.mention}", color=0xFFA500, timestamp=datetime.datetime.utcnow())
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

            await logsmsg.edit(embed = emb)

            try:
                commandeinfo[str(channel.id)]["Message2"] = message2.id
            except KeyError:
                print(f"Il y a une erreur!")

            with open("commande.json", "w") as f:
                commandeinfo = json.dump(commandeinfo, f, indent=2)



        elif interaction.custom_id == "delcommande":
            author = interaction.user
            await interaction.respond(type=7)

            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()
            acheteurname = commandeinfo[str(channel.id)]["Acheteur (name)"]
            acheteurid = commandeinfo[str(channel.id)]["Acheteur (ID)"]
            item = commandeinfo[str(channel.id)]["Item"]
            quantite = commandeinfo[str(channel.id)]["Quantite"]
            prix = commandeinfo[str(channel.id)]["Prix"]
            pseudoig = commandeinfo[str(channel.id)]["Pseudo IG"]
            reduction = commandeinfo[str(channel.id)]["Reduction"]
            message1 = commandeinfo[str(channel.id)]["Message1"]
            ticket_number = commandeinfo[str(channel.id)]["Numero"]
            logsmessage = commandeinfo[str(channel.id)]["Logs"]

            if interaction.user.id == acheteurid:
                await interaction.channel.delete()
                logsmsg = await log_channel.fetch_message(logsmessage)

                emb = discord.Embed(title=f"Commande n°{ticket_number}", description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n 💠 __**Statut:**__ \n \n > 🔔 **Annuler par l'acheteur**", color=0xFFA500, timestamp=datetime.datetime.utcnow())
                emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

                await logsmsg.edit(embed = emb)
            else:
                await interaction.channel.send(
                    "Vous **n'êtes pas acheteur**. Vous n'avez donc ***pas la permission d'annuler la commande***.", delete_after = 5)
                return



        elif interaction.custom_id == "endcommande":
            await interaction.respond(type=7)
            author = interaction.user


            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()


            acheteurname = commandeinfo[str(channel.id)]["Acheteur (name)"]
            acheteurid = commandeinfo[str(channel.id)]["Acheteur (ID)"]
            item = commandeinfo[str(channel.id)]["Item"]
            quantite = commandeinfo[str(channel.id)]["Quantite"]
            prix = commandeinfo[str(channel.id)]["Prix"]
            pseudoig = commandeinfo[str(channel.id)]["Pseudo IG"]
            reduction = commandeinfo[str(channel.id)]["Reduction"]
            message2 = commandeinfo[str(channel.id)]["Message2"]
            ticket_number = commandeinfo[str(channel.id)]["Numero"]
            logsmessage = commandeinfo[str(channel.id)]["Logs"]

            vendeur = interaction.guild.get_role(705093311248990312)

            if vendeur in author.roles:

                await interaction.channel.edit(name = f"🔵〡{acheteurname}-{ticket_number}")

                embed = discord.Embed(title = "💸 Commande prête",
                description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`Pseudo Discord:`* **<@{acheteurid}>** \n > *`ID:`* **{acheteurid}** \n > *`Réduction:`* **{reduction}** \n \n \n 💼 __**Informations du vendeur:**__ \n \n > *`Pseudo vendeur:`* **{author.mention}** \n > *`ID vendeur:`* **{author.id}** \n \n Commande n°**{ticket_number}**",
                color=0xFFA500, timestamp=datetime.datetime.utcnow())
                embed.set_footer(text="⇾ Merci de trouver un accord avec le vendeur.")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")
                message3 = await interaction.channel.send(embed = embed,
                                                components=[[
                                                  Button(style=ButtonStyle.red, label="Fermer le channel",
                                                         id="close")]])
                await interaction.channel.send(f"<@{acheteurid}>", delete_after = 1)
                await message3.pin()
                messages = await interaction.channel.history(limit=1).flatten()
                for message in messages:
                    await message.delete()
            else:
                await interaction.channel.send(
                    "Vous **n'êtes pas Vendeur**. Vous n'avez donc ***pas la permission de faire des commandes***.", delete_after = 5)
                return

            msg = await channel.fetch_message(message2)
            await msg.delete()

            logsmsg = await log_channel.fetch_message(logsmessage)

            emb = discord.Embed(title=f"Commande n°{ticket_number}", description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n 💠 __**Statut:**__ \n \n > 🔔 **En cours de livraison** \n > *`Vendeur:`* {interaction.user.mention}", color=0xFFA500, timestamp=datetime.datetime.utcnow())
            emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

            await logsmsg.edit(embed = emb)


        elif interaction.custom_id == "whitelist":
            await interaction.respond(type=7)
            author = interaction.user

            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()

            vendeur = interaction.guild.get_role(705093311248990312)

            if vendeur in author.roles:
                em = discord.Embed(description = "Quel est l'ID du vendeur que vous souhaitez Whitelist?", color = 0xFFA500)

                message = await interaction.channel.send(embed=em)

                try:
                    whitelist_user = await self.bot.wait_for("message", timeout=60,
                                                check=lambda msg: interaction.author == msg.author and channel == msg.channel)
                except:
                    await interaction.channel.send("Veuillez recommencer la procédure de whitelist.")
                    return

                guild = self.bot.get_guild(705089080693751850)
                user_whitelist = self.bot.get_user(int(whitelist_user.content))

                await interaction.channel.set_permissions(user_whitelist, send_messages=True, read_messages=True, add_reactions=True,
                                                     embed_links=True, attach_files=True, read_message_history=True,
                                                     external_emojis=True)

                await interaction.channel.purge(limit=2, check=lambda msg: not msg.pinned)

                await interaction.channel.send(f"<@{whitelist_user.content}> a bien été **Whitelist**.", delete_after = 5)

            else:
                await interaction.channel.send(
                    "Vous **n'êtes pas Vendeur**. Vous n'avez donc ***pas la permission de whitelist des vendeurs***.", delete_after = 5)

        elif interaction.custom_id == "close":
            await interaction.respond(type=7)
            author = interaction.user

            await self.when_commande(channel = interaction.channel)
            commandeinfo = await self.get_commande_data()

            acheteurname = commandeinfo[str(channel.id)]["Acheteur (name)"]
            acheteurid = commandeinfo[str(channel.id)]["Acheteur (ID)"]
            item = commandeinfo[str(channel.id)]["Item"]
            quantite = commandeinfo[str(channel.id)]["Quantite"]
            prix = commandeinfo[str(channel.id)]["Prix"]
            pseudoig = commandeinfo[str(channel.id)]["Pseudo IG"]
            reduction = commandeinfo[str(channel.id)]["Reduction"]
            ticket_number = commandeinfo[str(channel.id)]["Numero"]
            logsmessage = commandeinfo[str(channel.id)]["Logs"]

            vendeur = interaction.guild.get_role(705093311248990312)
            acheteur = guild.get_member(acheteurid)

            if vendeur in author.roles:
                try:

                    em = discord.Embed(title="Fermeture du Ticket", description="Pour valider la fermeture, entrez `close` dans le chat. Si vous souhaitez annulé, faites `cancel`", color=0x00a8ff)
                    em1 = discord.Embed(title="Fermeture du Ticket", description="Vous avez annulé la fermeture du channel !", color=0x00a8ff)
                    emclose = discord.Embed(title = "Fermeture de votre commande", description = f"> Votre commande n°**{ticket_number}** a été fermée! Vous pouvez laisser un avis sur {author.mention} dans <#705434824323760209>. Vous pouvez également laisser un avis sur les prix dans <#706532743705788558>. \n \n **À bientôt sur le ScaryShop !**", timestamp=datetime.datetime.utcnow(), color = 0xFFA500)
                    emclose.set_footer(text="ScaryBot",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

                    await interaction.channel.send(embed=em)
                    msg = await self.bot.wait_for('message', check=lambda msg: interaction.author == msg.author and channel == msg.channel, timeout=60)

                    if msg.content == "close":
                        await interaction.channel.delete()
                        await acheteur.send(embed = emclose)
                    elif msg.content == "Close":
                        await interaction.channel.delete()
                        await acheteur.send(embed = emclose)
                    else:
                        await interaction.channel.send(embed = em1)
                        return

                    logsmsg = await log_channel.fetch_message(logsmessage)

                    emb = discord.Embed(title=f"Commande n°{ticket_number}", description=f"💳 __**Informations de la commande:**__ \n \n > *`Item commandé:`* **{item}** \n > *`Quantité souhaité:`* **{quantite}** \n > *`Prix total:`* **{prix}**$ \n \n \n 🛒 __**Informations de l'acheteur:**__ \n \n > *`Pseudo IG:`* **{pseudoig}** \n > *`ID:`* **{author.id}** \n > *`Réduction:`* **{reduction}** \n \n 💠 __**Statut:**__ \n \n > 🔔 **Terminé** \n > *`Vendeur:`* {interaction.user.mention}", color=0xFFA500, timestamp=datetime.datetime.utcnow())
                    emb.set_thumbnail(url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")

                    await logsmsg.edit(embed = emb)

                except asyncio.TimeoutError:
                    em = discord.Embed(title="Fermeture", description="Vous avez mis trop de temps à répondre, veuillez refaire !close.", color=0x00a8ff)
                    await interaction.channel.send(embed=em)
                
            else:
                await interaction.channel.send(
                    "Vous **n'êtes pas Vendeur**. Vous n'avez donc ***pas la permission d'unclaim des commandes***.", delete_after = 5)
                return



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def ticket(self, ctx):
        embed = discord.Embed(title="**Passer une commande**",
                              description="Pour passer une commande, veuillez cliquer sur le bouton sous ce message. \n \n Le ticket peut parfois être long à s'ouvrir. Patientez avant de cliquer de nouveau.",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/705448891570716752/913711303980363816/buy.png")
        embed.set_footer(text="ScaryBot - Commande",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.green, label="🛒 Commander", custom_id="commande")])
        await ctx.message.delete()


    async def when_commande(self, channel):
        commandeinfo = await self.get_commande_data()

        if str(channel.id) in commandeinfo:
            return False
        else:

            commandeinfo[str(channel.id)] = {}
            commandeinfo[str(channel.id)]["channel_id"] = channel.id
            commandeinfo[str(channel.id)]["Acheteur (name)"] = "Acheteur (name)"
            commandeinfo[str(channel.id)]["Acheteur (discriminator)"] = "Acheteur (discriminator)"
            commandeinfo[str(channel.id)]["Acheteur (ID)"] = "Acheteur (ID)"
            commandeinfo[str(channel.id)]["Item"] = "Item"
            commandeinfo[str(channel.id)]["Quantite"] = "Quantite"
            commandeinfo[str(channel.id)]["Prix"] = "Prix"
            commandeinfo[str(channel.id)]["Pseudo IG"] = "Pseudo IG"
            commandeinfo[str(channel.id)]["Reduction"] = "Reduction"
            commandeinfo[str(channel.id)]["Message1"] = "Message 1"
            commandeinfo[str(channel.id)]["Message2"] = "Message 2"
            commandeinfo[str(channel.id)]["Numero"] = "Numero"
            commandeinfo[str(channel.id)]["Logs"] = "Logs"

        with open("commande.json", "w") as f:
            commandeinfo = json.dump(commandeinfo, f, indent=2)
        return True


    async def get_commande_data(self):
        with open("commande.json", "r") as f:
            commandeinfo = json.load(f)

        return commandeinfo


def setup(bot):
    bot.add_cog(Commande(bot))