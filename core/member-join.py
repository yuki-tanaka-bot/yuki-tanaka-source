from discord import *
from discord.ext import commands
from discord.utils import get
from config import admin, dev_guild, user_role, hi_channel

class Member_join(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id != dev_guild:
            return
        r = member.guild.get_role(user_role)
        await member.add_roles(r)
        c = member.guild.get_channel(hi_channel)
        await c.send(f"Приветик, {member.mention}!")
        return


def setup(client):
    client.add_cog(Member_join(client))