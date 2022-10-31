
from discord_components import ComponentsBot
from decouple import config
from help_cog import help_cog
from music import music_cog
from help_cog import help_cog
from gado import Gado
from gay import gay_cog
from mentioned import Mentioned
from salve import Salve
from moeda import moeda_cog
from merchan import merchan


bot = ComponentsBot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Bora Pivete!!!DJ {bot.user} na aréa!!")
    bot.remove_command('help')
    bot.add_cog(help_cog(bot))
    bot.add_cog(music_cog(bot))
    bot.add_cog(Mentioned(bot)) 
    bot.add_cog(Salve(bot))
    bot.add_cog(Gado(bot)) 
    bot.add_cog(gay_cog(bot))
    bot.add_cog(moeda_cog(bot))
    bot.add_cog(merchan(bot))
key = config("TOKEN")
bot.run(key)
