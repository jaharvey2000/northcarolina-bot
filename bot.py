import discord
from dotenv import load_dotenv
import os
import random
import logging
import re

# Load environment variables
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
IMAGE_URL = os.getenv('IMAGE_URL')

# Configure bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    replyEmbed = discord.Embed(
        title='North Carolina Mentioned',
        color=random.randint(0, 0xFFFFFF)
    )
    replyEmbed.set_image(url=IMAGE_URL)

    if re.search(r'north carolina', message.content, re.IGNORECASE):
        await message.reply(embed=replyEmbed, mention_author=False)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
client.run(DISCORD_TOKEN, log_handler=handler)
