
import discord

from config import token,prefix,insensitive
from discord.ext import commands

client = commands.Bot(command_prefix = prefix, case_insensitive = insensitive)

#event start

@client.event
async def on_ready():
  print('Hello World!')

@client.command()
async def template(ctx):
  await ctx.send(f'start template')  

#event end  

client.run(token)
