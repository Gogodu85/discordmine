import discord
import os
import startserver

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!start'):
        startserver()
        await message.channel.send('Démarrage en cours...')

try:
    client.run("MTEyMTkxMzI4NDI1NDI0MDg2OQ.Gu6ZQo.GNc2UyyUi6ftkVXH38jxWh2mUnGoZXqUysC0-4")
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e