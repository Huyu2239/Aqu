import discord
from discord.ext import commands  
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def neko(self, ctx):
        if ctx.author.bot:
            return
        await ctx.send('にゃーん')

    @commands.command()
    async def ping(self, ctx):
        if ctx.author.bot:
            return
        await ctx.send('pong!')
        await ctx.send(f"`{self.bot.ws.latency * 1000:.0f}ms`")

def setup(bot):
    bot.add_cog(Ping(bot))