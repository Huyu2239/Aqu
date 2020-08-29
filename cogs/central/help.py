import discord
from discord.ext import commands
from datetime import datetime
import asyncio
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def help_pages(self, ctx, msg, lang):
        page = 0
        if lang == 0:
            lang_txt='English'
        if lang == 1:
            lang_txt = 'Japanese'
        react_list = self.bot.get_cog('Contents').react_list
        for react in react_list:
            await msg.add_reaction(react)
        def check(reaction, user):
            if reaction.message.id != msg.id:
                return False
            elif ctx.author.bot or user != ctx.author:
                return False
            elif str(reaction.emoji) in react_list:
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

            if emoji == "\U000025c0":
                if page == 0:
                    pass
                else:
                    page -= 1
            if emoji == "\U000025b6":
                if page == 3:
                    pass
                else:
                    page += 1
            if emoji == "\U000023f9":
                await msg.delete()
                break
            embed = self.bot.get_cog('Contents').help[0][lang][page]
            await msg.edit(content='[' + lang_txt + '　' +str(page+1) + '/10]',embed=embed)


    @commands.group()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = self.bot.get_cog('Contents').lang
            msg = await ctx.send(embed=embed)

            langs_list = self.bot.get_cog('Contents').langs_list
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
            try:
                react = await self.bot.wait_for("reaction_add", check=check, timeout=300)
            except asyncio.TimeoutError:
                await ctx.message.clear_reactions()
            if str(react.emoji) == "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}":
                lang = 0
                lang_txt = 'English'
            if str(react.emoji) == "\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}":
                lang = 1
                lang_txt = 'Japanese'
            embed = self.bot.get_cog('Contents').help[0][lang][0]
            await msg.edit(content='[' + lang_txt + '　' +str(0) + '/10]',embed=embed)
            await self.help_pages(ctx, msg, lang)

    @help.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def en(self, ctx):
        en = self.bot.get_cog('Contents').help[0][0][0]
        msg = await ctx.send('English', embed=en)
        await self.help_pages(ctx, msg, 0)

    @help.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def jp(self, ctx):
        jp = self.bot.get_cog('Contents').help[0][1][0]
        msg = await ctx.send('Japanese', embed=jp)
        await self.help_pages(ctx, msg, 1)

    async def commands_help_pages(self, ctx, msg):
        langs_list = self.bot.get_cog('Contents').langs_list
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
            lang = 0
            lang_txt = 'English'
            if emoji in langs_list:
                if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}":
                    lang = 0
                    lang_txt = 'English'
                if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}":
                    lang = 1
                    lang_txt = 'Japanese'
            embed = self.bot.get_cog('Contents').help[0][lang]
            await msg.edit(content=lang_txt,embed=embed)

    @help.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def about(self, ctx, lang=None):
        if lang == (None or 'en'):
            abouts = self.bot.get_cog('Contents').help[1][0]
            msg = await ctx.send(embed=abouts)
            await self.commands_help_pages(ctx, msg)
        if lang == 'jp':
            abouts = self.bot.get_cog('Contents').help[1][1]
            msg = await ctx.send(embed=abouts)
            await self.commands_help_pages(ctx, msg)

def setup(bot):
    bot.add_cog(Help(bot))