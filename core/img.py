import asyncio
from discord import *
from discord.ext import commands
from discord.utils import get
import requests
from requests.utils import requote_uri
from core.nekro import nekro_random
class Image(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(aliases=["i", "img"])
    @commands.guild_only()
    async def image(self, ctx, *, args):
        if not ctx.channel.is_nsfw():
            await ctx.send("Этот канал не имеет пометку `nsfw`!")
            return
        if args.lower() == "nekro":
            img = nekro_random()
        else:
            resp  = requests.get(f'http://discord-holo-api.ml/api/{args.lower()}')

            if resp.status_code == 200:


                img = resp.json()

                img = img["url"]
                img = requote_uri(img)

        emb = Embed(title = f'{args.capitalize()}', colour = Colour.dark_purple())
        emb.set_image(url = img)
        emb.set_footer(text = f"For  {ctx.author}")
        await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Image(bot))
