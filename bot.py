# bot.py
import os

import discord
from dotenv import load_dotenv
#from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#bot = commands.Bot(command_prefix='m!')

# below: manual input of token/guild vals
#TOKEN = input('Please enter the token: ')
#GUILD = input('Please enter the guild: ')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
)

"""
@bot.command(name='hi')
async def hello(ctx):
    response = 'Hi, ' + message.author.name + '!'
    await ctx.send(response)
"""

def eval(s,op):
    lst = []
    for i in s:
        if i.isnumeric():
            lst.append(int(i))
    if op == 'add':
        return sum(lst)
    elif op == 'mult':
        result = 1
        for i in lst:
            result *= i
        return result

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    cmddict = {'greet':'Hi, ' + message.author.name + '!',
               'gay':'no u',
               'm!':'haha yes very funny',
               'fuck':'wow haha i am dying of laughter',
               'daily':'wrong prefix idiot. not tatsumaki smdh',
               '':"that's not a command dumbass, that's the absence of a command. smdh",
               'help':'Commands:\n\t1. greet (prints a greeting)\n\t2. gay (no u)\n\t3. add (adds ints in input)\n\t4. mult (multiplies ints in input)'}
    prefix = 'm!'
    if message.content[:len(prefix)] == prefix:
        body = message.content[len(prefix):]
        if body[:3] == 'add':
            response = eval(message.content, 'add')
        elif body[:4] == 'mult':
            response = eval(message.content, 'mult')
        elif body not in cmddict:
            response = 'enter a valid command dumbass'
        else:
            response = cmddict[body]
        await message.channel.send(response)

client.run(TOKEN)
#bot.run(TOKEN)
