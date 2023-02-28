import discord
from discord.ext import commands
from ducksapi import DucksApi
from os import environ

intents = discord.Intents.default()

intents.message_content=True
bot = commands.Bot(command_prefix='cueh!', description="CUEH-bOT 3.0", intents=intents)
ducks = DucksApi()
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.command()
async def duck(ctx):
    random_duck=ducks.get_random_duck()
    await ctx.send(f'Cueh\n{random_duck}')


bot.run(environ["DISCORD_TOKEN"])