import discord
from discord.ext import commands
from datetime import datetime
import libneko

def default_buttons():
    from libneko.pag.reactionbuttons import (
        first_page,
        back_10_pages,
        previous_page,
        next_page,
        forward_10_pages,
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
#help
#help lang    
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please wait...')
            return
    @help.command()
    async def about(self, ctx, lang=None):
        if lang==None:
            await ctx.send('aq?about')

    @help.command()
    async def en(self, ctx):
        await ctx.send('Please wait...')
        return
    @help.command()
    async def jp(self, ctx):
        jp = [(discord.Embed(title="基本機能",color=discord.Color.blue())),
                (discord.Embed(title="スレッド機能",color=discord.Color.blue())),
                (discord.Embed(title="レベル機能",color=discord.Color.blue())),
                (discord.Embed(title="その他機能",color=discord.Color.blue()))
        ]
        #central
        jp[0].add_field(name="aq?help", value="コマンド一覧表示", inline=False)
        jp[0].add_field(name="aq?about", value="このBOTの概要を表示します。。", inline=False)
        jp[0].add_field(name="~~aq?help `<コマンド>`~~", value="~~`<コマンド>`で指定したコマンドの詳細を表示します。~~\ncoming soon", inline=False)

        #main
        jp[1].add_field(name="スレッド作成", value="<#742244652115034203>に質問したいことを書き込むと、自由に聞けるスレッドが作成されます。",inline=False)
        jp[1].add_field(name="スレッド閉鎖",value="自分が作成したスレッドで`close`と発言すると、スレッドを閉鎖できます", inline=False)
        jp[1].add_field(name="スレッド検索",value="aq?search `検索ワード`　のように入力すると、一致するスレッド一覧を返信します。" ,inline=False)

        #main-level
        jp[2].add_field(name="概要", value="サーバー内で発言すると経験値が溜まり、レベルが上がります。",inline=False)
        jp[2].add_field(name="特典", value="レベルに基づいて、様々な特典（ロールや権限など）があります。",inline=False)

        #common
        jp[3].add_field(name="aq?ping", value="pong値を返信します。(あくまでBotのpongなので正直あてになりません)", inline=False)
        jp[3].add_field(name="翻訳機能", value="翻訳したいメッセージに国旗のリアクションを付けると、その国の言語に翻訳した文章を返信します", inline=False)
        jp[3].add_field(name="ロールパネル", value="自分でロールを取得できます。\n詳しくは<#>まで", inline=False)

        nav = libneko.pag.navigator.EmbedNavigator(ctx, jp, buttons=default_buttons(), timeout=60)
        nav.start()
        await ctx.send(nav)

#about       
    @commands.group()
    async def about(self, ctx):
        if ctx.invoked_subcommand is None:
            abouts=en=self.bot.get_cog('Contents').about
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
    bot.add_cog(Help(bot))