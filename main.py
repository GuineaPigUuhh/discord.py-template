
import discord
import token
from discord.ext import commands

client = commands.Bot(command_prefix = "youprefix", case_insensitive = True)

#event start

@client.event
async def on_ready():
  print('Hello World!')

@client.command()
async def template(ctx):
  await ctx.send(f'start template')  

#event end  

client.run(token.token)
