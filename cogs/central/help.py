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

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please wait...')
    @help.command()
    async def about(self, ctx, lang=None):
        if lang == None:
            abouts = self.bot.get_cog('Contents').help[1]
            nav = libneko.pag.navigator.EmbedNavigator(ctx, abouts, buttons=default_buttons(), timeout=60)
            nav.start()
            await ctx.send(nav)
        if lang == 'en':
            abouts = self.bot.get_cog('Contents').help[1][0]
            await ctx.send(embed=abouts)
        if lang == 'jp':
            abouts = self.bot.get_cog('Contents').help[1][1]
            await ctx.send(embed=abouts)

    @help.command()
    async def en(self, ctx):
        en=self.bot.get_cog('Contents').help[0][0]
        nav = libneko.pag.navigator.EmbedNavigator(ctx, en, buttons=default_buttons(), timeout=60)
        nav.start()
        await ctx.send(nav)
    @help.command()
    async def jp(self, ctx):
        jp=self.bot.get_cog('Contents').help[0][1]
        nav = libneko.pag.navigator.EmbedNavigator(ctx, jp, buttons=default_buttons(), timeout=60)
        nav.start()
        await ctx.send(nav)
        await ctx.send('f')

def setup(bot):
    bot.add_cog(Help(bot))