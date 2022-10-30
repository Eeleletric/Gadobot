import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
Bora Pivete!! DJ {bot.user} na aréa!! :sunglasses:
Comandos de Música:
!p <keywords> - Toca a música do youtube encontrada.
!q - Mostra a queue, se não sabe o que é queue, FODA-SE!!.
!skip - Pula a música atual.
!clear - Para a música e limpa a queue, se não sabe o que é queue coloca !q.
!leave - Me Expulsa do canal de voz.
!pause - Pausa a música atual.
!resume - Resume a música pausada.

Comandos de Interação:
!salve
!gado
!gay
!moeda
!sorteio
!twitch
!youtube
"""     
    @commands.command(name="help", help="Mostra todos os comandos disponíveis!!")
    async def help(self, ctx):
        await ctx.send(self.help_message)


    

