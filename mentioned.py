import discord
from discord.ext import commands
import random

class Mentioned(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
                    return
        R = random.randrange(1,3)
        mention= message.mentions[0].name
        print(R)
        gay=[]
        gay.append(mention)
        if R==1:
            if "Samwise" in gay:
            #Samuca
                await message.channel.send(":rainbow_flag: ?")
            if "Hiromyn" in gay:
                #Hiromyn
                await message.channel.send("https://tenor.com/view/meek-horn-corno-manso-chifrudo-horned-touro-gif-25135020")
            if "Savin Noel" in gay:
                #Savin
                await message.channel.send("https://tenor.com/view/aesthetic-coffee-gif-25334064")
        elif R==2:
            if "matheus662" in gay:
                    #Chibira
                await message.channel.send(":rainbow_flag: ?")
            if "Prometheus V" in gay:
                    #Prometheus
                await message.channel.send("https://tenor.com/view/capybara-capivara-piuvas-cute-adorable-gif-25811257")
            if "MadT" in gay:
                    #MadT
                await message.channel.send("https://tenor.com/view/aatrox-league-of-legends-croc-town-gif-24412455")
            if "Imaturo" in gay:
                    #Felipão
                await message.channel.send("https://tenor.com/view/anime-funny-weeb-waifu-anime-roast-your-waifu-isnt-real-gif-15764528")
            if "Heitor, O Gadorcista" in gay:
                    #Eu
                print(message.mentions[0].name)
                await message.channel.send("https://tenor.com/view/chad-monke-gif-20835999")
        else:
            return
        await self.bot.process_commands(message)
  