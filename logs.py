import discord
from discord.ext import commands


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        channel = self.bot.get_channel(856896928267894804)

        if message.content == "**":
            return

        elif message.author.id == 851078177337245767:
            return

        else:

            em = discord.Embed(title="",
                               description=f"💾 **► Message supprimé** \n \n **Le message de {message.author} a été supprimé dans <#{message.channel.id}>!** \n \n *{message.content}*",
                               color=0xFFA500)

            await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        channel = self.bot.get_channel(857701139730137158)

        em = discord.Embed(title="",
                           description=f"💾 **► Message edité** \n \n **Le message de {before.author} a été édité dans <#{before.channel.id}>!** \n \n *{before.content}* \n <:fad:835500807210270770> *{after.content}*",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(857701370467057674)

        em = discord.Embed(title="",
                           description=f"💾 **► Nouvel arrivant** \n \n **{member.mention}** viens de rejoindre le serveur!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        channel = self.bot.get_channel(857701873355980810)

        em = discord.Embed(title="",
                           description=f"💾 **► Nouveau départ** \n \n **{member.mention}** viens malheureusement de quitter le serveur!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):

        channel = self.bot.get_channel(857704947679101018)

        em = discord.Embed(title="",
                           description=f"💾 **► Serveur edité** \n \n **{before}** devient maintenant **{after}**!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):

        channel = self.bot.get_channel(857704947679101018)

        em = discord.Embed(title="",
                           description=f"💾 **► Serveur modifié** \n \n **{before}** devient maintenant **{after}**!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):

        channel = self.bot.get_channel(857705968007381002)

        em = discord.Embed(title="", description=f"💾 **► Rôle créé** \n \n Le rôle **{role}** a été créé!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):

        channel = self.bot.get_channel(857705996524847164)

        em = discord.Embed(title="", description=f"💾 **► Rôle supprimé** \n \n Le rôle **{role}** a été supprimé!",
                           color=0xFFA500)

        await channel.send(embed=em)

    ####################################################################

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):

        channel = self.bot.get_channel(857706025070362624)

        em = discord.Embed(title="",
                           description=f"💾 **► Rôle modifié** \n \n **{before.name}** a été modifié en **{after.name}**!",
                           color=0xFFA500)

        await channel.send(embed=em)


####################################################################

def setup(bot):
    bot.add_cog(Logs(bot))
