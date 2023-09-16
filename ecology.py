import discord
from discord.ext import commands
import os
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} запущен')

@bot.command()
async def help(ctx):
    await ctx.send("/eco - факт об экологии\n/whatis [предмет] - что можно сделать из переработанного предмета")

@bot.command()
async def eco(ctx):
    fact = os.listdir('facts')
    with open(f'facts/{choice(fact)}', 'r') as f:
        text = discord.File(f)
    await ctx.send(text)

