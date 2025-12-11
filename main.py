import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from econendpoints import *

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

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    resp = message_sent(ctx.author)
    if resp['nl']:
        await ctx.reply(f'🤖: Вітаю з новим рівнем!')
    await bot.process_commands(ctx)

@bot.command(name='hello')
async def hello(ctx):
    await ctx.reply(f'👋 Привіт, {ctx.author.name}!')

@bot.command(name='gpt')
async def hello(ctx, *, content):
    response = requests.post("http://ai_service:8001/ask", json={"prompt": content})
    result = response.json()
    await ctx.reply(f'🤖: {result['response']}!')

@bot.command(name="me")
async def me(ctx):
    resp = get_user(ctx.author)
    embed = discord.Embed(
        title=f'👤 Статистика {ctx.author.name}',
        color=discord.Color.orange()
    )
    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.add_field(name="Рівень", value=resp['lvl'], inline=True)
    embed.add_field(name="Досвід", value=resp['xp'], inline=False)
    await ctx.reply(embed=embed)

@bot.command(name="leaderboard")
async def leaderboard(ctx):
    resp = get_leaderboard()
    embed = discord.Embed(
        title='Топ лідерів'
    )
    for i, x in enumerate(resp):
        embed.add_field(name=str(i+1), value=f"{x['id']}: {x['xp']}xp", inline=False)

    await ctx.reply(embed=embed)

def main():
    if TOKEN is None:
        raise TypeError("Please set DISCORD_TOKEN environment variable")
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
