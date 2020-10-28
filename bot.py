import json
import discord
from speech.speech import speech_out_msg

with open('config.json') as f:
    data = json.load(f)
    TOKEN = data["token"]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    speech_message = f'{message.author.name} said {message.content}'
    print(speech_message)
    speech_out_msg(speech_message)

client.run(TOKEN)
