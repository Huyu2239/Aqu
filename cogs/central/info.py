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
        back_10_pages(),
        previous_page(),
        next_page(),
        forward_10_pages(),
        last_page()
    )
buttons = default_buttons()

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#help
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Please wait...')
            return
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
        timestamp = datetime.utcfromtimestamp(int(self.bot.user.created_at.timestamp()))
        if ctx.invoked_subcommand is None:
            abouts = [
                (discord.Embed(title="ABOUT THIS BOT:", description=f">>> ```This is an Management BOT\nmade for this server```", timestamp=timestamp,color=discord.Color.blue())),
                (discord.Embed(title="このBOTの概要:", description=f">>> ```このサーバー専用の運営BOTです```", timestamp=timestamp, color=discord.Color.blue()))
                    ]
            #en
            abouts[0].set_thumbnail(url=self.bot.user.avatar_url)
            abouts[0].add_field(name="all_members", value=f"`{len(set(self.bot.get_all_members()))}`")
            abouts[0].add_field(name="dev_lang", value="`discord.py`")
            abouts[0].add_field(name="Base machine", value="`TeraServer`")
            abouts[0].set_footer(text="This bot made on")

            #jp
            abouts[1].set_thumbnail(url=self.bot.user.avatar_url)
            abouts[1].add_field(name="総ユーザー数", value=f"`{len(set(self.bot.get_all_members()))}`")
            abouts[1].add_field(name="開発言語", value="`discord.py`")
            abouts[1].add_field(name="動作環境", value="`TeraServer`")
            abouts[1].set_footer(text="このBOTの作成日")

            nav = libneko.pag.navigator.EmbedNavigator(ctx, abouts, buttons=default_buttons(), timeout=60)
            nav.start()
            await ctx.send(nav)


    @about.command()
    async def en(self, ctx):
        en = discord.Embed(title="ABOUT THIS BOT:", description=f">>> ```This is an Management BOT\nmade for this server```", timestamp=timestamp, color=0x009193)
        en.set_thumbnail(url=self.bot.user.avatar_url)
        en.add_field(name="all_members", value=f"`{len(set(self.bot.get_all_members()))}`")
        en.add_field(name="dev_lang", value="`discord.py`")
        en.add_field(name="Base machine", value="`TeraServer`")
        en.set_footer(text="This bot made on")
        await ctx.send(embed=en)

    @about.command()
    async def jp(self, ctx):
        jp = discord.Embed(title="このBOTの概要:", description=f">>> ```このサーバー専用の運営BOTです```", timestamp=timestamp, color=0x009193)
        jp.set_thumbnail(url=self.bot.user.avatar_url)
        jp.add_field(name="総ユーザー数", value=f"`{len(set(self.bot.get_all_members()))}`")
        jp.add_field(name="開発言語", value="`discord.py`")
        jp.add_field(name="動作環境", value="`TeraServer`")
        jp.set_footer(text="このBOTの作成日")
        await ctx.send(embed=jp)


def setup(bot):
    bot.add_cog(Help(bot))