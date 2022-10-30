from discord.ext import commands
import random

class Gado(commands.Cog):
        def _init_(self, bot):
                self.bot = bot
        @commands.command(name="gado",aliases=["hiromyn","samuca"], help="Vê o quão gado você é")
        async def gado(self,ctx):
                name = ctx.author.name
                if name== "Heitor, O Gadorcista":
                        F = str(0)
                        await ctx.send("Bem Vindo Gadorcista, é uma honra receber você novamente: "+F+"%")
                        return
                if name=="Samwise":
                        F = str(8000)
                        await ctx.send("MEU DEUS SUA GADISSE É MAIS DE "+F+"%")
                        return
                elif name=="matheus662":
                        F = str(60)
                        await ctx.send("Algo me diz que você é apreciador de waifus: "+F+"%")
                        return
                elif name=="Hiromyn":
                        F = str(7999)
                        await ctx.send("Um Oponente digno para Samuca!! "+F+"%")
                        return
                else:
                        G=random.randrange(1,101)
                        F=str(G)
                        if G==100:
                                await ctx.send("Você não tem solução VERME, SAIA DAQUI: "+F+"%")
                        else:
                                if G>=75:
                                        await ctx.send("Sua Gadisse já ocupou 3/4 da sua mente, vai procurar um Gadorcista verme: "+F+"%")
                                elif  G>=50 and G<75:
                                        await ctx.send("Foque em você meu amigo, ainda tem chance de se salvar: "+F+"%")
                                elif  G>= 25 and G<50:
                                        await ctx.send("Você está no caminho certo amigo, continue no seu grindset: "+F+"%")
                                else:
                                        await ctx.send("SIGMA que se fala né? "+F+"%")
               
