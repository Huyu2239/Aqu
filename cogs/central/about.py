import discord
from discord.ext import commands
from datetime import datetime
import libneko

def default_buttons():
    from libneko.pag.reactionbuttons import (
        first_page,
        previous_page,
        next_page,
        last_page
    )
    return (
        first_page(),
        previous_page(),
        next_page(),
        last_page()
    )
buttons = default_buttons()

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #about
    @commands.group()
    async def about(self, ctx):
        if ctx.invoked_subcommand is None:
            abouts=self.bot.get_cog('Contents').about
            nav = libneko.pag.navigator.EmbedNavigator(ctx, abouts, buttons=default_buttons(), timeout=60)
            nav.start()
            await ctx.send(nav)


    @about.command()
    async def en(self, ctx):
        en=self.bot.get_cog('Contents').about[0]
        await ctx.send(embed=en)

    @about.command()
    async def jp(self, ctx):
        jp=self.bot.get_cog('Contents').about[1]
        await ctx.send(embed=jp)


def setup(bot):
    bot.add_cog(About(bot))