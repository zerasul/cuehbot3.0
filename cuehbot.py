import discord
from discord.ext import commands
from ducksapi import DucksApi
from elliapi import ElliApi
from os import environ

intents = discord.Intents.default()

intents.message_content=True
bot = commands.Bot(command_prefix='cueh!', description="CUEH-bOT 3.0", intents=intents)
ducks = DucksApi()
ellis= ElliApi()

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.command()
async def duck(ctx):
    random_duck=ducks.get_random_duck()
    await ctx.send(f'Cueh\n{random_duck}')

@bot.command()
async def elli(ctx):
    random_elli=ellis.get_random_elli()
    await ctx.send(f'cuehpompo\n{random_elli}')


bot.run(environ["DISCORD_TOKEN"])