import asyncio
from  discord import *
from discord.ext import commands
from discord.utils import get
from config import admin
import os


class Dev(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases=["pg"]) 
    async def ping(self, ctx):
        
        if ctx.author.id in admin:
            emb = Embed(title = f'Ping', colour = Colour.dark_purple(), description = f"<a:ping:883346584539107338> {int(float(self.client.latency)*1000)} ms")
            await ctx.send(embed = emb)
        else:
            await ctx.send(f"У тебя нет прав!") 
    @commands.command(aliases=["all"])
    async def all_commands(self, ctx):
        if ctx.author.id in admin:
            com = ""
            count = 0
            for command in self.client.commands:
                count += 1
                com += "****" + str(count) + ")****  **"+ str(command) + "**\n"
            emb = Embed(title = f'Все команды', colour = Colour.dark_purple(), description = f"{com}")
            await ctx.send(embed=emb)
        else:
            await ctx.send(f"Разве ты мой разработчик?!") 


def setup(client):
    client.add_cog(Dev(client))