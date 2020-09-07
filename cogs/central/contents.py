import discord
from discord.ext import commands
from datetime import datetime
import numpy as np
import asyncio
class Contents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#about
        timestamp = datetime.utcfromtimestamp(int(self.bot.user.created_at.timestamp()))
        self.about = [
            (discord.Embed(title="ABOUT THIS BOT:", description=f">>> ```This is an Management BOT\nmade for this server```", timestamp=timestamp,color=discord.Color.blue())),
            (discord.Embed(title="このBOTの概要:", description=f">>> ```このサーバー専用の運営BOTです```", timestamp=timestamp, color=discord.Color.blue()))
        ]
    #en
        self.about[0].set_thumbnail(url=self.bot.user.avatar_url)
        self.about[0].add_field(name="all_members", value=f"`{len(set(self.bot.get_all_members()))}`")
        self.about[0].add_field(name="dev_lang", value="`discord.py`")
        self.about[0].add_field(name="Base machine", value="`TeraServer`")
        self.about[0].set_footer(text="This bot made on")

    #jp
        self.about[1].set_thumbnail(url=self.bot.user.avatar_url)
        self.about[1].add_field(name="総ユーザー数", value=f"`{len(set(self.bot.get_all_members()))}`")
        self.about[1].add_field(name="開発言語", value="`discord.py`")
        self.about[1].add_field(name="動作環境", value="`TeraServer`")
        self.about[1].set_footer(text="このBOTの作成日")

#help
        self.help = [#help all
            [#help
                [#help en
                    (discord.Embed(title="main",color=discord.Color.blue())),
                    (discord.Embed(title="スレッド機能",color=discord.Color.blue())),
                    (discord.Embed(title="レベル機能",color=discord.Color.blue())),
                    (discord.Embed(title="etc",color=discord.Color.blue()))
                ],
                [#help jp
                    (discord.Embed(title="基本機能",color=discord.Color.blue())),
                    (discord.Embed(title="スレッド機能",color=discord.Color.blue())),
                    (discord.Embed(title="レベル機能",color=discord.Color.blue())),
                    (discord.Embed(title="その他機能",color=discord.Color.blue()))
                ]
            ],

            [#help about
                (discord.Embed(title="English",dcolor=discord.Color.blue())),
                (discord.Embed(title="日本語",color=discord.Color.blue()))
            ]
        ]
    #help en
        en = self.help[0][0]
        en[0].add_field(name="aq?help", value="コマンド一覧表示", inline=False)
    #help jp
        jp = self.help[0][1]
        #central
        jp[0].add_field(name="aq?help", value="コマンド一覧表示", inline=False)
        jp[0].add_field(name="aq?about", value="このBOTの概要を表示します。。", inline=False)
        jp[0].add_field(name="aq?help `<コマンド>`", value="`<コマンド>`で指定したコマンドの詳細を表示します。", inline=False)

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

    #about
        self.help[1][0].add_field(name="about", value="show infomation of this bot")
        self.help[1][1].add_field(name="about", value="ボットの情報を表示します")

        self.lang = discord.Embed(title="languages",color=discord.Color.blue())

#reactions
        self.langs_list = [
            "\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}",#英語
            "\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}"#日本語
        ]
        
        self.react_list = [
            "\N{BLACK LEFT-POINTING TRIANGLE}",  # 戻る
            "\N{BLACK RIGHT-POINTING TRIANGLE}",  # 進む
            "\N{BLACK SQUARE FOR STOP}\N{VARIATION SELECTOR-16}"#終了
        ]

#panels
        self.role_panels = [
            (discord.Embed(title="role panel", description="",color=discord.Color.blue())),
            (discord.Embed(title="ロールパネル", description="当てはまるものにリアクションを付けてください。\nロールを付与します。\nリアクションを外すとロールも外れます。",color=discord.Color.blue()))
        ]

        self.role_panels[0].add_field(name="all_members", value=f"`{len(set(self.bot.get_all_members()))}`")
        self.role_panels[0].add_field(name="dev_lang", value="`discord.py`")
        self.role_panels[0].add_field(name="Base machine", value="`TeraServer`")

def setup(bot):
    bot.add_cog(Contents(bot))