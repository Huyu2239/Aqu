import discord
from discord.ext import commands
import json
import re
import os

with open('setting.json', mode='r', encoding='utf-8') as sett:
    set_json = sett.read()

    staff = json.loads(set_json)['staff']
    owner = staff['owner']
    admin_list = staff['admin']

path="./cogs"

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="reload")
    async def _reload(self, ctx, cog_name):
        if not ctx.author.id in admin_list:
            return await ctx.send('Admin専用コマンドです')
        await ctx.send("更新中")
        if cog_name == "all":
            for cog in os.listdir(path+"/main"):
                if cog.endswith(".py"):
                    try:
                        self.bot.reload_extension(f"cogs.common.{cog[:-3]}")
                    except commands.ExtensionNotLoaded:
                        self.bot.load_extension(f"cogs.common.{cog[:-3]}")
            for cog in os.listdir(path+"/common"):
                if cog.endswith(".py"):
                    try:
                        self.bot.reload_extension(f"cogs.common.{cog[:-3]}")
                    except commands.ExtensionNotLoaded:
                        continue
            await ctx.send("更新しました")
            return
        try:
            self.bot.reload_extension(f'cogs.common.{cog_name}')
        except commands.ExtensionNotFound:
            await ctx.send('指定されたcogが見つかりませんでした')
            return
        except commands.ExtensionNotLoaded:
            self.bot.load_extension(f'cogs.common.{cog_name}')
        else:
            await ctx.message.add_reaction('\U00002705')
        await ctx.send("更新しました")

    @commands.command()
    async def dreload(self, ctx):
        if not ctx.author.id in admin_list:
            return await ctx.send('Admin専用コマンドです')
        await ctx.send("更新中")
        for cog in os.listdir(path+"/dev"):
            if cog.endswith(".py"):
                try:
                    self.bot.reload_extension(f"cogs.dev.{cog[:-3]}")
                except commands.ExtensionNotLoaded:
                    self.bot.load_extension(f"cogs.dev.{cog[:-3]}")
        await ctx.send("更新しました")
        return

    @commands.command()
    async def coglist(self, ctx):
        if not ctx.author.id in admin_list:
            return await ctx.send('Admin専用コマンドです')
        await ctx.send('/centaral')
        for cog in os.listdir(path+"/central"):
            if cog.endswith(".py"):
                await ctx.send(cog)
        await ctx.send('/dev')
        for cog in os.listdir(path+"/dev"):
            if cog.endswith(".py"):
                await ctx.send(cog)
        '''
        await ctx.send('/main')
        for cog in os.listdir(path+"/main"):
            if cog.endswith(".py"):
                await ctx.send(cog)
        await ctx.send('/common')
        for cog in os.listdir(path+"/common"):
            if cog.endswith(".py"):
                await ctx.send(cog)
        '''
        await ctx.send('end')
def setup(bot):
    bot.add_cog(Admin(bot))