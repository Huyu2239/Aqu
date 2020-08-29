import discord
from discord.ext import commands
from datetime import datetime
import asyncio

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def about_pages(self, ctx, msg):
        langs_list=self.bot.get_cog('Contents').langs_list
        for lang in langs_list:
            await msg.add_reaction(lang)
        def check(reaction, user):
            if reaction.message.id != msg.id:
                return False
            elif ctx.author.bot or user != ctx.author:
                return False
            elif str(reaction.emoji) in langs_list:
                return reaction, user
            else:
                return False
        while not self.bot.is_closed():
            try:
                react, user= await self.bot.wait_for("reaction_add", check=check, timeout=300)
            except asyncio.TimeoutError:
                await ctx.message.clear_reactions()
                break
            emoji = str(react.emoji)
            await msg.remove_reaction(emoji, user)
            if emoji in langs_list:
                if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}":
                    lang = 0
                    lang_txt = 'English'
                if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}":
                    lang = 1
                    lang_txt = 'Japanese'
            else:
                return
            embed = self.bot.get_cog('Contents').about[lang]
            await msg.edit(content=lang_txt, embed=embed)
#about
    @commands.group()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def about(self, ctx):
        if ctx.invoked_subcommand is None:
            abouts=self.bot.get_cog('Contents').about[0]
            msg = await ctx.send('English', embed=abouts)
            await self.about_pages(ctx, msg)

    @about.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def en(self, ctx):
        en=self.bot.get_cog('Contents').about[0]
        msg = await ctx.send('English', embed=en)
        await self.about_pages(ctx, msg)

    @about.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def jp(self, ctx):
        jp=self.bot.get_cog('Contents').about[1]
        msg = await ctx.send('Japanese', embed=jp)
        await self.about_pages(ctx, msg)


def setup(bot):
    bot.add_cog(About(bot))