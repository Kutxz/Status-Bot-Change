import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print(bot.user.name)
  while True:
    await bot.change_presence(activity=discord.Activity(name="Epicgames", type=1))
    await asyncio.sleep(5)
    
    await bot.change_presence(activity=discord.Activity(name="*", type=2))
    await asyncio.sleep(5)
    
    await bot.change_presence(activity=discord.Activity(name="", type=3))
    await asyncio.sleep(5)
    
bot.run("Your Token")
