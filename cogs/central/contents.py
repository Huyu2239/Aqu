import discord
from discord.ext import commands
from datetime import datetime
class Contents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #abouts
        timestamp = datetime.utcfromtimestamp(20200810)
        about = [
            (discord.Embed(title="ABOUT THIS BOT:", description=f">>> ```This is an Management BOT\nmade for this server```", timestamp=timestamp,color=discord.Color.blue())),
            (discord.Embed(title="このBOTの概要:", description=f">>> ```このサーバー専用の運営BOTです```", timestamp=timestamp, color=discord.Color.blue()))
        ]
        #en
        about[0].set_thumbnail(url=self.bot.user.avatar_url)
        about[0].add_field(name="all_members", value=f"`{len(set(self.get_all_members()))}`")
        about[0].add_field(name="dev_lang", value="`discord.py`")
        about[0].add_field(name="Base machine", value="`TeraServer`")
        about[0].set_footer(text="This bot made on")

        #jp
        about[1].set_thumbnail(url=self.bot.user.avatar_url)
        about[1].add_field(name="総ユーザー数", value=f"`{len(set(self.get_all_members()))}`")
        about[1].add_field(name="開発言語", value="`discord.py`")
        about[1].add_field(name="動作環境", value="`TeraServer`")
        about[1].set_footer(text="このBOTの作成日")
def setup(bot):
    bot.add_cog(Contents(bot))