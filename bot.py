import discord
from decouple import config
from discord.ext import commands
from music import music_cog
from help import help_cog
from gado import Gado
from mentioned import Mentioned
from salve import Salve
import os

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
@bot.event
async def on_ready():
    bot.remove_command('help')
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(Mentioned(bot)) 
    await bot.add_cog(Salve(bot))
    await bot.add_cog(Gado(bot)) 

bot.run(os.enviro['TOKEN'])