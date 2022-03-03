from discord.ext import commands
from discord_components import *
from discord_slash.utils.manage_components import *

class Absence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def absence(self, ctx):
        embed = discord.Embed(title="**Signaler une absence**",
                              description="Pour signaler une absence, veuillez cliquer sur le bouton sous ce message.",
                              color=0xFFA500)
        embed.set_thumbnail(
            url="https://discord.com/assets/8becd37ab9d13cdfe37c08c496a9def3.svg")
        embed.set_footer(text="ScaryBot",
                         icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

        await ctx.send(embed=embed,
                       components=[Button(style=ButtonStyle.green, label="❌ Absence", custom_id="absence")])
        await ctx.message.delete()

    @commands.Cog.listener()
    async def on_button_click(self, interaction: Interaction):
        channel = interaction.channel
        if interaction.custom_id == "absence":
            await interaction.respond(type=7)
            absenceChannel = self.bot.get_channel(866409747828441088)
            author = interaction.user

            em1 = discord.Embed(description="À partir de quand serez-vous absent?", color=0xFFA500)
            em2 = discord.Embed(description="Jusqu'à quand serez-vous absent?", color=0xFFA500)
            em3 = discord.Embed(description="Combien de temps serez-vous connecté à Discord par jour?", color=0xFFA500)
            em4 = discord.Embed(
                description="Quelle est la raison de votre absence? (si personnelle, veuillez le préciser)",
                color=0xFFA500)

            await interaction.channel.send(embed=em1)

            try:
                debut = await self.bot.wait_for("message", timeout=60,
                                                check=lambda
                                                    msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=1, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            message = await interaction.channel.send(embed=em2)

            try:
                fin = await self.bot.wait_for("message", timeout=60,
                                              check=lambda
                                                  msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=3, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            message = await interaction.channel.send(embed=em3)

            try:
                connection = await self.bot.wait_for("message", timeout=60,
                                                     check=lambda
                                                         msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=5, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            message = await interaction.channel.send(embed=em4)

            try:
                raison = await self.bot.wait_for("message", timeout=60,
                                                 check=lambda
                                                     msg: interaction.author == msg.author and channel == msg.channel)
            except:
                await interaction.channel.purge(limit=7, check=lambda msg: not msg.pinned)
                await interaction.channel.send("Vous avez été trop long, veuillez recommencer.", delete_after=10)
                return

            await interaction.channel.purge(limit=8, check=lambda msg: not msg.pinned)

            em = discord.Embed(
                description=f"**❌ ABSENCE de {author} ❌** \n \n > *Date de début* <a:fl:802827880618000414> **`{debut.content}`** \n > *Date de fin* <a:fl:802827880618000414> **`{fin.content}`** \n > *Temps de connexion (par jour)* <a:fl:802827880618000414> **`{connection.content}`** \n > *Raison* <a:fl:802827880618000414> **`{raison.content}`**",
                color=0xFFA500)
            em.set_footer(text="ScaryBot - Absence",
                          icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")
            em2 = discord.Embed(
                description=f"**❌ Votre absence a bien été signalée ❌** \n \n > *Date de début* <a:fl:802827880618000414> **`{debut.content}`** \n > *Date de fin* <a:fl:802827880618000414> **`{fin.content}`** \n > *Temps de connexion (par jour)* <a:fl:802827880618000414> **`{connection.content}`** \n > *Raison* <a:fl:802827880618000414> **`{raison.content}`**",
                color=0xFFA500)
            em2.set_footer(text="ScaryBot - Absence",
                           icon_url="https://cdn.discordapp.com/emojis/834364622555054080.png?size=128")

            await interaction.author.send(embed=em2)
            await absenceChannel.send(embed=em)


def setup(bot):
    bot.add_cog(Absence(bot))
