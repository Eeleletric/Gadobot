import discord
from discord.ext import commands


class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embedOrange = 0xeab148

    @commands.Cog.listener()
    async def on_ready(self):
        sendToChannels = []
        for guild in self.bot.guilds:
            channel = guild.text_channels[0]
            sendToChannels.append(channel)
        helloEmbed = discord.Embed(
            title="Bom Dia, Boa Tarde, Boa Noite!",
            description="""
            BORA PIVETE!! DJ Gadobot na aréa, se quiser qualquer coisa manda o comando com prefixo "!", exemplo !help""",
            colour=self.embedOrange)
        for channel in sendToChannels:
            await channel.send(embed=helloEmbed)

    @commands.command(
        name="help",
        aliases=["h","ajuda"],
        help="Mostra todos os comandos"
    )
    async def help(self, ctx):
        helpCog = self.bot.get_cog('help_cog')
        musicCog = self.bot.get_cog('music_cog')
        gadoCog= self.bot.get_cog('Gado')
        salveCog= self.bot.get_cog('Salve')
        gayCog = self.bot.get_cog('gay_cog')
        moedaCog = self.bot.get_cog('moeda_cog') 
        merchanCog=self.bot.get_cog('merchan')     
        commands = helpCog.get_commands() + musicCog.get_commands() + gadoCog.get_commands() + salveCog.get_commands() + gayCog.get_commands() + moedaCog.get_commands() + merchanCog.get_commands()
        commandDescription = ""

        for c in commands:
            commandDescription += f"**`!{c.name}`** {c.help}\n"
        commandsEmbed = discord.Embed(
            title="Lista de Comands",
            description=commandDescription,
            colour=self.embedOrange
        )

        await ctx.send(embed=commandsEmbed)