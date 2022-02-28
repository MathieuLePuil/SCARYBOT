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
import requests

token = "TOKEN"
API_ENDPOINT = "https://discord.com/api/v9"
header = {
    "Authorization": f"Bot NzM1Nzg0MDEzOTM1MDE4MDU0.XxlSQw.utyzXyI-rD14yZyPMxy8Janni1g",
    "User-Agent": "Bot"
}


class Resend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def resend_message(self, ctx, message: discord.Message):
        print("1")
        r = requests.get(f"{API_ENDPOINT}/channels/{ctx.channel.id}/messages/{message.id}", headers=header)
        print(r.text)
        requests.post(f"{API_ENDPOINT}/channels/{ctx.channel.id}/messages", json=r.json(), headers=header)

def setup(bot):
    bot.add_cog(Resend(bot))