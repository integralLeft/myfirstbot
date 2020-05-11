# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    cmddict = {'greet':'Hi, ' + message.author + '!', 'gay':'no u'}
    prefix = 'm!'
    if message.content[:len(prefix)] == prefix:
        body = message.content[len(prefix)]
        if body not in cmddict:
            response = 'enter a valid command dumbass'
        else:
            response = cmddict[body]
        await message.channel.send(response)

client.run(TOKEN)
