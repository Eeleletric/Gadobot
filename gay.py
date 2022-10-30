from discord.ext import commands
import random
class gay_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="gay", aliases=["chibira"],help="Vê se ta na hora de sair do armário ou não!!")
    async def gay(self, ctx):
        name = ctx.author.name
        if name=="matheus662":
                F = str(100)
                await ctx.send("Homofóbico: -"+F+"%")
                return
        else:
            G=random.randrange(1,101)
            F=str(G)
            if G==100:
                await ctx.send("Você é a pessoa que fala pros amigos que brotheram não quer dizer ser gay: "+F+"%")
            else:
                if G>=75:
                    await ctx.send("By the way You are Gay: "+F+"%")
                elif  G>=50 and G<75:
                    await ctx.send("Vem pro painho venha: "+F+"%")
                elif  G>= 25 and G<50:
                    await ctx.send("Eu diria que por baixo desse rostinho, você quer um cuzinho: "+F+"%")
                else:
                    await ctx.send(f"Tu é "+F+"% hetero amigo!!")