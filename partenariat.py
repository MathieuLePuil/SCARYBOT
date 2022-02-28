import discord
from discord.ext import commands

class Partenariat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def partenariat(self, ctx): 
        embed = discord.Embed(title = "📮 ► Promotion du ScaryShop", description = " __**PARTENARIATS :**__ \n ```════════════════════╣ __***ScaryShop V4***__ ╠════════════════════ \n \n  Vous êtes à la recherche du market **le plus innovant**, nous l'avons trouvé pour vous : le **ScaryShop**. \n \n  __Les avantages du *𝗦𝗰𝗮𝗿𝘆𝗦𝗵𝗼𝗽:*__ \n \n > :book: • Un **catalogue** avec **BEAUCOUP** de choix \n > \n > :money_with_wings: • Un des Market les **moins chers** de  tout Paladium \n > \n > :trophy: • Des vendeurs **très rapides** \n > \n > :medal: • Un staff **réactif** permettant de répondre aux demandes de chacun \n > \n > :shopping_cart: • Un bot **unique** et **intuitif** vous permettant une meilleure expérience \n > \n > :gem:  • Des **Grades Payants** qui vous donne des avantages \n > \n > :tada: • D'énormes **Giveaways** tout au long de la Saison \n > \n > :shopping_bags: • **Et encore beaucoup d'autres choses** \n \n **Votre ticket pour le ScaryShop :** https://discord.gg/4S2uamx  \n \n *Bon jeu à vous cher joueurs/euses de Paladium.* \n \n ***Mention:*** \n ***Bannière:*** https://cdn.discordapp.com/attachments/701111672844320868/913437551967211610/1.gif``` \n \n __**PUB EN JEU :**__ \n \n > - <a:check:835499517977690122> ***Non-Gradés*** \n \n • `ScaryShop | Prix Bas | Nombreux Giveaways | Animations | Bot Unique | Add <Pseudo Discord + #>` \n \n • `ScaryShop | Prix Bas | Nombreux Giveaways | Recrutements Vendeurs OPEN | Add <Pseudo Discord + #>` \n \n \n > - <a:wrong:835499521341128746> ***Gradés*** \n \n • `&aScaryShop &f| &bPrix Bas &f| &9Nombreux Giveaways &f| &7Bot Unique &f| &dAdd <Pseudo Discord + #>` \n \n • `&aScaryShop &f| &9Nombreux Giveaways &f| &bRecrutements Vendeurs OPEN &f| &dAdd <Pseudo Discord + #>`", color = 0xFFA500)
        embed.set_image(url = "https://cdn.discordapp.com/attachments/701111672844320868/913437551967211610/1.gif")
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/705448891570716752/913711303305076756/partenariat.png")
        await ctx.send(embed = embed)
        await ctx.message.delete()

###!partenariat

def setup(bot):
    bot.add_cog(Partenariat(bot))