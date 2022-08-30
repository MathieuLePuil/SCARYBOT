from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *
from discord_components import *

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

# py Desktop\BOT_FINAL\main.py

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")
slash = SlashCommand(bot, sync_commands=True)

extensions = ['on_command_error', 'on_member_join', 'latence', 'cblacklist', 'eblacklist', 'gblacklist', 'pat_avis',
              'rupture', 'resultats', 'recompenses', 'conditionspart', 'grades', 'moderateurs', 'msgsugg',
              'partenariat', 'qdj', 'vendeurs', 'logs', 'absence', 'close', 'help', 'simple', 'suggestion', 'autorole',
              'commande', 'enchere', 'giveaway', 'support', 'role', 'reseau', 'effectif_vendeur', 'effectif_grades',
              'giveaway_prog', 'rappel', 'resend_message', 'gift', 'loterie', 'profil_update', 'profil_info']


@bot.event
async def on_ready():
    channel = bot.get_channel(828549652621164574)

    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing,
                                                                                      name="Comment ça marche? | !help"))
    print("Scarybot est PRET!")
    await channel.send("**`Scarybot`** vient de redémarrer!")
    # msg = await channel.send("<@337971595928666113>")
    # await msg.delete()
    DiscordComponents(bot)


@bot.command()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        await ctx.send('Loaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be loaded. [{}]'.format(extension, error))


@bot.command()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        await ctx.send('Unloaded **{}**'.format(extension))
    except Exception as error:
        await ctx.send('**{}** cannot be unloaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('**{}** cannot be loaded. [{}]'.format(extension, error))


@bot.command()
async def reload(ctx, extension):
    if extension:
        try:
            bot.reload_extension(extension)
            await ctx.send('Reloaded **{}**'.format(extension))
        except:
            bot.load_extension(extension)
            await ctx.send('Loaded **{}**'.format(extension))


bot.run("NzM1Nzg0MDEzOTM1MDE4MDU0.XxlSQw.utyzXyI-rD14yZyPMxy8Janni1g")
