import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix='.')

@bot.command()
async def serverinfo(ctx):
    await ctx.reply('This is a minecraft server and the owner is NightTerror5293#8508 and he developed me and my work is to guide new members of the server. Pls got to #rules📜📜to read the rules of the server.For more info Dm him.Thank you!! am glad to help you.')
  

bot.run(getenv('TOKEN'))