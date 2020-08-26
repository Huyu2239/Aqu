import discord
from discord.ext import commands

class Close(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content=="close":
            await message.channel.send("This channel was closed by "+ message.author.name)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction):
        if reaction.emoji == '':
            pass
def setup(bot):
    bot.add_cog(Close(bot))