from discord.ext import commands

class merchan(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.command(name="youtube", aliases=["Yout", "yt"], help ="Manda o canal de alguém hehehe")
    async def youtube(self, ctx):
        await ctx.send("https://www.youtube.com/channel/UC3XfGX2Sxkf7y4UAHqflcoQ")
    @commands.command(name="twitch", aliases=["Twitch","tw"], help ="Manda a twitch de alguém hehehe")
    async def twitch(self, ctx):
        await ctx.send("https://www.twitch.tv/gadocista")
