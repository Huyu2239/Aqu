import discord
from discord.ext import commands
from datetime import datetime
import asyncio
self_id=742371009352433714
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#言語ページめくり関数
    async def commands_pages(self, ctx, msg, com):
        langs_list = self.bot.get_cog('Contents').langs_list
        for lang in langs_list:
            await msg.add_reaction(lang)
        def check(reaction, user):
            if reaction.message.id != msg.id or ctx.author.bot or user != ctx.author:
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
            embed = self.bot.get_cog('Contents').help[com][lang]
            await msg.edit(content=lang_txt,embed=embed)
#helpコマンド
    @commands.group(invoke_without_command=True)
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def help(self, ctx, langs = None):
        msg = await ctx.send('Now loading...')
        if ctx.invoked_subcommand is None:
            try:
                langs = ctx.message.content.split()[1]
            except IndexError:
                langs = None
    #/helpの時は言語確認してページ
        if langs == None:
            embed = self.bot.get_cog('Contents').lang   
            await msg.edit(content='',embed=embed)
            langs_list = self.bot.get_cog('Contents').langs_list
            for LANG in langs_list:
                await msg.add_reaction(LANG)
            def check1(reaction, user):
                if reaction.message.id != msg.id or ctx.author.bot or user != ctx.author:
                    return False
                elif str(reaction.emoji) in langs_list:
                    return reaction, user
                else:
                    return False
            try:
                react, user = await self.bot.wait_for("reaction_add", check=check1, timeout=300)
            except asyncio.TimeoutError:
                await ctx.message.clear_reactions()
            emoji = str(react.emoji)
            await msg.remove_reaction(emoji, user)
            lang = 0
            lang_txt = ''
            if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}":
                lang = 0
                lang_txt = 'English'
            if emoji == "\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}":
                lang = 1
                lang_txt = 'Japanese'
            embed = self.bot.get_cog('Contents').help[0][lang][0]
            await msg.edit(content='[' + lang_txt + '　' +str(1) + '/4]',embed=embed)
            user = await self.bot.fetch_user(self_id)
            for emoji in langs_list:
                await msg.remove_reaction(emoji, user)
    #/help langs　の時はその言語のページ
        else:
            lang = 0
            lang_txt = ''
            if langs == 'en':
                lang = 0
                lang_txt = 'English'
            if langs =='jp':
                lang = 1
                lang_txt = 'Japanese'
            else:
                pass
            embed = self.bot.get_cog('Contents').help[0][lang][0]
            await msg.edit(content='[' + lang_txt + '　' +str(1) + '/4]',embed=embed)
            user = await self.bot.fetch_user(self_id)
    #ページめくり
        page = 0
        react_list = self.bot.get_cog('Contents').react_list
        for react in react_list:
            await msg.add_reaction(react)
        def check2(reaction, user):
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
                react, user= await self.bot.wait_for("reaction_add", check=check2, timeout=300)
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
            await msg.edit(content='[' + lang_txt + '　' +str(page+1) + '/4]',embed=embed)
#その他
    @help.command()
    @commands.bot_has_permissions(add_reactions=True, manage_messages=True)
    async def about(self, ctx, langs=None):
        #/help commands の時は言語選べるページ
        if langs == None:
            abouts = self.bot.get_cog('Contents').help[1][0]
            msg = await ctx.send(embed=abouts)
            await self.commands_pages(ctx, msg, 1)
        #/help commands langsの時はその言語のembed
        else:
            if langs == 'en':
                abouts = self.bot.get_cog('Contents').help[1][0]
                await ctx.send(embed=abouts)
            if langs == 'jp':
                abouts = self.bot.get_cog('Contents').help[1][1]
                await ctx.send(embed=abouts)

def setup(bot):
    bot.add_cog(Help(bot))