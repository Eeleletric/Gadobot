import discord
from discord.ext import commands

class Salve(commands.Cog):
    def _init_(self, bot):
        self.bot = bot
    @commands.command(name="salve", aliases=["oi","hi"], help= "Manda Salve")
    async def salve(self,ctx):
        name = ctx.author.name
        if name== "Heitor, O Gadorcista":
            await ctx.send("É um Prazer conhecer um Gadorcista igual a você, "+name+" =3")
        elif name == "matheus662":
            await ctx.send("""SAI DAQUI CORNO, NÃO COLOQUE I WANNA STAY AT YOUR HOUSE NÃO!! E JÁ FEZ TCC? CANALHA!!
:angry: """)
        elif name == "Samwise":
            await ctx.send("VAI ESTUDAR SAFADO!!")
        elif name == "Prometheus V":
            await ctx.send("Salve Promethinha, quer um pagodizin pivete? Bota ai po!!")
        else:
            await ctx.send("Salve Corno " + name +"!! Quer uma músiquinha é? SÓ NÃO VAI COLOCAR I WANNA STAY AT YOUR HOUSE OU MÚSICA DE ANIME PIVETE!!! :angry:")
    