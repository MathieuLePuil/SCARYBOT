import discord
from discord.ext import commands
from discord_slash import *

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name = "help", description = "Affiche toutes les commandes du bot.")
    async def help(self, ctx, *, categorie = "aucune"):
        if categorie == "aucune":
            embed = discord.Embed(title = "Help ScaryBot", description = "Veuillez signalez la catégorie que vous souhaitez en utilisant `!help <catégorie>`.", color=0xFFA500)
            embed.add_field(name = "`Acheteur`", value = "<:fad:835500807210270770> Affiche les commandes disponibles pour les acheteurs.", inline = False)
            embed.add_field(name = "`Vendeur`", value = "<:fad:835500807210270770> Affiche les commandes disponibles pour les vendeurs.", inline = False)
            embed.add_field(name = "`Moderateur`", value = "<:fad:835500807210270770> Affiche les commandes disponibles pour les modérateurs.", inline = False)
            embed.add_field(name = "`Responsable`", value = "<:fad:835500807210270770> Affiche les commandes disponibles pour les responsables.", inline = False)
            embed.add_field(name = "`Admin`", value = "<:fad:835500807210270770> Affiche les commandes disponibles pour les administrateurs.", inline = False)
            embed.add_field(name = "`Bots`", value = "<:fad:835500807210270770> Affiche les commandes help et les prefix pour chaque Bots.", inline = False)
            embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            embed.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            embed.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = embed)

        if categorie == "acheteur":
            em1 = discord.Embed(title = "Help Acheteur", description = "Voici toutes les commandes disponibles pour la catégorie `Acheteur`.", color=0xFFA500)
            em1.add_field(name = "`/suggestion`", value = "<:fad:835500807210270770> Proposer des ajouts/changements au serveur.", inline = False)
            em1.add_field(name = "`/youtube`", value = "<:fad:835500807210270770> Affiche la chaîne Youtube du créateur.", inline = False)
            em1.add_field(name = "`/twitch`", value = "<:fad:835500807210270770> Affiche la chaîne Twitch du créateur.", inline = False)
            em1.add_field(name = "`/recompenses`", value = "<:fad:835500807210270770> Demande de récompense lors d'évènement d'invitation.", inline = False)
            em1.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em1.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em1.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em1)

        if categorie == "vendeur":
            em3 = discord.Embed(title = "Help Vendeur", description = "Voici toutes les commandes disponibles pour la catégorie `Vendeur`.", color=0xFFA500)
            em3.add_field(name = "`/qdj", value = "<:fad:835500807210270770> Propose de vendre la quête du jour.", inline = False)
            em3.add_field(name = "`/latence`", value = "<:fad:835500807210270770> Affiche la latence du Bot.", inline = False)
            em3.add_field(name = "`!pat_avis`", value = "<:fad:835500807210270770> Indique à l'acheteur de laisser un avis.", inline = False)
            em3.add_field(name = "`/close`", value = "<:fad:835500807210270770> Ferme un ticket de commande.", inline = False)
            em3.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em3.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em3.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em3)

        if categorie == "moderateur":
            em3 = discord.Embed(title = "Help Modérateur", description = "Voici toutes les commandes disponibles pour la catégorie `modérateur`.", color=0xFFA500)
            em3.add_field(name = "`/gblacklist`", value = "<:fad:835500807210270770> Permet de blacklister un utilisateur qui n'a pas respecté les giveaways.", inline = False)
            em3.add_field(name = "`/eblacklist`", value = "<:fad:835500807210270770> Permet de blacklister un utilisateur qui n'a pas respecté les enchères.", inline = False)
            em3.add_field(name = "`/cblacklist`", value = "<:fad:835500807210270770> Permet de blacklister un utilisateur qui n'a pas respecté les commandes.", inline = False)
            em3.add_field(name = "`/gunblacklist`", value = "<:fad:835500807210270770> Permet d'unblacklister un utilisateur qui n'a pas respecté les giveaways.", inline = False)
            em3.add_field(name = "`/eunblacklist`", value = "<:fad:835500807210270770> Permet d'unblacklister un utilisateur qui n'a pas respecté les enchères.", inline = False)
            em3.add_field(name = "`/cunblacklist`", value = "<:fad:835500807210270770> Permet d'unblacklister un utilisateur qui n'a pas respecté les commandes.", inline = False)
            em3.add_field(name = "`/tempgrade`", value = "<:fad:835500807210270770> Ajoute un grade payant temporairement à un utilisateur.", inline = False)
            em3.add_field(name = "`/cles`", value = "<:fad:835500807210270770> Donner l'accès de son bureau à un utilisateur.", inline = False)
            em3.add_field(name = "`/addrole`", value = "<:fad:835500807210270770> Ajouter un rôle à un utilisateur.", inline = False)
            em3.add_field(name = "`/rappel`", value = "<:fad:835500807210270770> Mettre un rappel dans un certain temps dans un channel spécifique.", inline = False)
            em3.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em3.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em3.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em3)

        if categorie == "responsable":
            em6 = discord.Embed(title = "Help Responsable", description = "Voici toutes les commandes disponibles pour la catégorie `Responsable`.", color=0xFFA500)
            em6.add_field(name = "`/resultats`", value = "<:fad:835500807210270770> Démarre une nouvelle enchère.", inline = False)
            em6.add_field(name = "`/chut`", value = "<:fad:835500807210270770> Rappel à l'ordre ceux qui discutent dans le channel enchère.", inline = False)
            em7.add_field(name = "`/tempgrade`", value = "<:fad:835500807210270770> Ajoute un rôle payant temporairement.", inline = False)           
            em7.add_field(name = "`/addrole`", value = "<:fad:835500807210270770> Ajoute un rôle à un utilisateur.", inline = False)
            em7.add_field(name = "`/effectif_vendeur`", value = "<:fad:835500807210270770> Affiche la liste des vendeurs du serveur.", inline = False)
            em6.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em6.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em6.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em6)

        if categorie == "admin":
            em7 = discord.Embed(title = "Help Administrateur", description = "Voici toutes les commandes disponibles pour la catégorie `Administrateur`.", color=0xFFA500)
            em7.add_field(name = "`!sorciere`", value = "<:fad:835500807210270770> Affiche les avantages du grade Amethyst.", inline = False)
            em7.add_field(name = "`!faucheuse`", value = "<:fad:835500807210270770> Affiche les avantages du grade Titane.", inline = False)
            em7.add_field(name = "`!fantome`", value = "<:fad:835500807210270770> Affiche les avantages du grade Paladium.", inline = False)
            em7.add_field(name = "`!assassin`", value = "<:fad:835500807210270770> Affiche les avantages du grade Endium.", inline = False)
            em7.add_field(name = "`/effectif_grade`", value = "<:fad:835500807210270770> Affiche la liste des gradés du serveur.", inline = False)
            em7.add_field(name = "`!msgsugg`", value = "<:fad:835500807210270770> Affiche le message pour proposer une suggestion.", inline = False)
            em7.add_field(name = "`/rupture`", value = "<:fad:835500807210270770> Ajout d'un item en rupture de stock.", inline = False)
            em7.add_field(name = "`!partenariat`", value = "<:fad:835500807210270770> Affiche l'interface des pubs pour le market.", inline = False)
            em7.add_field(name = "`!conditionspart`", value = "<:fad:835500807210270770> Affiche l'interface des conditions de partenariats.", inline = False)
            em7.add_field(name = "`!rcm`", value = "<:fad:835500807210270770> Affiche l'interface des recrutements Modérateurs.", inline = False)
            em7.add_field(name = "`!rcv`", value = "<:fad:835500807210270770> Affiche l'interface des recrutements Vendeurs.", inline = False)
            em7.add_field(name = "`!reseau`", value = "<:fad:835500807210270770> Affiche l'interface de pub des réseaux sociaux du ScaryShop.", inline = False)
            em7.add_field(name = "`!absence`", value = "<:fad:835500807210270770> Affiche l'interface des absences.", inline = False)
            em7.add_field(name = "`!interroles`", value = "<:fad:835500807210270770> Affiche l'interface des auto-rôles.", inline = False)
            em7.add_field(name = "`!ticket`", value = "<:fad:835500807210270770> Affiche l'interface des commandes.", inline = False)
            em7.add_field(name = "`!enchere`", value = "<:fad:835500807210270770> Affiche l'interface des enchères.", inline = False)
            em7.add_field(name = "`!giveaway`", value = "<:fad:835500807210270770> Affiche l'interface des giveaway.", inline = False)
            em7.add_field(name = "`!support`", value = "<:fad:835500807210270770> Affiche l'interface du support.", inline = False)
            em7.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em7.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em7.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em7)

        if categorie == "bots":
            em8 = discord.Embed(title = "Help Bots", description = "Voici toutes les commandes disponibles pour la catégorie `Bots`.", color=0xFFA500)
            em8.add_field(name = "`p!help`", value = "<:fad:835500807210270770> Affiche l'aide du Paladium'Bot.", inline = False)
            em8.add_field(name = "`g!help`", value = "<:fad:835500807210270770> Affiche l'aide du GiveawayBot.", inline = False)
            em8.add_field(name = "`.help`", value = "<:fad:835500807210270770> Affiche l'aide d'InviteLogger Classic.", inline = False)
            em8.add_field(name = "`#help`", value = "<:fad:835500807210270770> Affiche l'aide de YAGPDB.", inline = False)
            em8.add_field(name = "`/help`", value = "<:fad:835500807210270770> Affiche l'aide de Rythm.", inline = False)
            em8.add_field(name = "`a!help`", value = "<:fad:835500807210270770> Affiche l'aide de Atlas.", inline = False)
            em8.add_field(name = "`:help`", value = "<:fad:835500807210270770> Affiche l'aide de Dyno.", inline = False)
            em8.add_field(name = "`?help`", value = "<:fad:835500807210270770> Affiche l'aide de Voltage.", inline = False)
            em8.set_thumbnail(url = "https://cdn.discordapp.com/emojis/762020637283713055.png?v=1")
            em8.set_image(url = "https://cdn.discordapp.com/emojis/813748552915222529.png?v=1")
            em8.set_footer(text = "ScaryBot - Help",
                     icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            await ctx.send(embed = em8)

def setup(bot):
    bot.add_cog(Help(bot))