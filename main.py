import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='!' , intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'run!                                                                                          制作者Dorihu116by {bot.user}')

bot .run('TOKEN')
