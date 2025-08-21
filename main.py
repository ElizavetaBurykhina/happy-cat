import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client(intents=discord.Intents(messages=True, message_content=True))


@bot.event
async def on_message(message):
    message_content = str(message.content).lower()
    if 'happy' in message_content or 'congratulations' in message_content:
        with open('./cat.gif', 'rb') as img:
            await message.channel.send(file=discord.File(img), reference=message, mention_author=False)


bot.run(DISCORD_TOKEN)
