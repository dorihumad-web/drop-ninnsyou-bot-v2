import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='!' , intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'起動したyoooo                                                                                          制作者Dorihu116by {bot.user}')

bot .run('MTQ1NDQ0NDA2MDI4MTQwNTQ1Mw.Gm4XMB.qryPw_WSWpXdwdLOa8PkSbtD_OzG4yIQ0KBMdU')
