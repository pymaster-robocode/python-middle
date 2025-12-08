import os

import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user.name} готовий до роботи!')
    await bot.change_presence(activity=discord.Game(name='!допомога для команд'))

@bot.command(name='hello')
async def hello(ctx):
    await ctx.reply(f'👋 Привіт, {ctx.author.name}!')

@bot.command(name='gpt')
async def hello(ctx, *, content):
    response = requests.post("http://ai_service:8001/ask", json={"prompt": content})
    result = response.json()
    await ctx.reply(f'🤖: {result['response']}!')

def main():
    if TOKEN is None:
        raise TypeError("Please set DISCORD_TOKEN environment variable")
    bot.run(TOKEN)

if __name__ == '__main__':
    main()


