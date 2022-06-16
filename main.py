from discord import *
from discord.ext import commands
from discord.utils import get
from config import TOKEN as token, dbl_token, dev_channel, prefix
import os
import topgg
import asyncio
import requests


client = commands.AutoShardedBot(command_prefix= f"{prefix}", intents = Intents.all())
client.topggpy = topgg.DBLClient(client, dbl_token, autopost=True)

client.remove_command("help")

async def status_task():
    while True:
        await client.change_presence(status=Status.online, activity= Activity(type=ActivityType.listening, name="J-pop"))
        await asyncio.sleep(10)
        await client.change_presence(status=Status.online, activity= Activity(type=ActivityType.watching, name=f"{len(client.guilds)} серверов"))
        await asyncio.sleep(10) 

@client.event
async def on_autopost_success():
    channel = client.get_channel(dev_channel)
    await channel.send(f"Количество серверов: {client.topggpy.guild_count}")
    

@client.event
async def on_ready():
    
    client.load_extension('jishaku')
    print('[COGS] jishaku')    
    for filename in os.listdir('./core'): 
            if filename.endswith('.py') and filename[:-3] != "yandex" and filename[:-3] != "nekro":
                client.load_extension(f"core.{filename[:-3]}")
                print(f'[COGS] {filename[:-3]}')
    client.loop.create_task(status_task())
    print("[Invite] https://discord.com/api/oauth2/authorize?client_id=882648343564652544&permissions=137475992896&scope=bot")



@client.command()
async def help(ctx, arg = ''):

    if arg == "join":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "join или join <голосовой канал>", value = f'Псевдонимы: `connect`, `j`\n')

    if arg == "leave":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "leave", value = f'Псевдонимы: `stop`, `dc`, `disconnect`, `bye`\n')
    
    if arg == "play":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name =  "play <название> или play <ссылка>", value = f'Псевдонимы: `sing`,`p`\n')
    
    if arg == "pause":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "pause", value = f'Псевдонимы: *Пусто*\n')
    
    if arg == "resume":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "resume", value = f'Псевдонимы: *Пусто*\n')
    
    if arg == "skip":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "skip", value = f'Псевдонимы: `s`\n')
    
    if arg == "remove":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "remove <позиция в очереди>", value = f'Псевдонимы: `rm`, `rem`\n') 
    
    if arg == "clear":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "clear", value = f'Псевдонимы: `clr`, `cl`, `cr`\n')

    if arg == "queue":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "queue", value = f'Псевдонимы: `q`, `playlist`, `que`, `list`, `l`\n')
    
    if arg == "currentsong":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "currentsong", value = f'Псевдонимы: `np`, `song`, `current`, `playing`')
    
    if arg == "ping":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "ping", value = f'Псевдонимы: `pg`')
    
    if arg == "all_commands":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "all_commands", value = f'Псевдонимы: `all`')


    if arg == "image":
        emb = Embed(title = f'Помощь по команде {arg.capitalize()}', colour = Colour.dark_purple(),  timestamp = ctx.message.created_at)
        emb.add_field(name = "image <название тега>", value = f'Псевдонимы: `i, img`\nТеги: `{imgs_help}`') 


    if arg == '':
        emb = Embed(title = 'Помощь по командам!', colour = Colour.dark_purple(), description = "Мой префикс: `yt`\nЕсли нужна справка по конкретной команде - yt help <команда>", timestamp = ctx.message.created_at)
        emb.add_field(name = "Разработчик", value = f'`ping`, `all_commands`', inline=False)
        emb.add_field(name = "Музыка", value = f'`join`, `leave`, `play`, `pause`, `resume`, `skip`, `remove`, `clear`, `queue`, `currentsong`', inline=False)
    emb.set_footer(text = f"Для {ctx.author}")
    await ctx.send(embed = emb)
client.run(token)
