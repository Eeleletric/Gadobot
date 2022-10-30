from discord.ext import commands
import random

class moeda_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="moeda", aliases=["MadT"],help="Vê se tem sorte na moeda!!")
    async def moeda(self, ctx):
        M = random.randrange(1,3)
        if ctx.author.name=="MadT":
            await ctx.send("AAAAAEEEEEEEEUUUUUUUGGGGGGGHHHHHH")
        else:   
            if M == 1:
                await ctx.send("Caiu Coroa!!!")
            if M == 2:
                await ctx.send("Caiu Cara!!!")
        
