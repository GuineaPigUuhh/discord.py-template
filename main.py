import discord

# Settings
from src.settings import *
from src.private_settings import *

from discord.ext import commands

client = commands.Bot(
                      command_prefix=PREFIX,
                      case_insensitive=INSENSITIVE,
                      intents=INTENTS
                    )

@client.event
async def on_ready():
  print(f'Bot Name: {client.user.name}')
  print(f'Bot Ping: {client.latency}')

@client.command()
async def template(ctx):
  await ctx.send(f'start template')  

client.run(TOKEN)
