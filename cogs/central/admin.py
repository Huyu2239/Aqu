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
file_name = [
    'central',
    'main',
    'common',
    'dev'
]

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def reload(self, ctx):
        if not ctx.author.id in admin_list:
            return await ctx.send('Admin専用コマンドです')
        await ctx.send("更新中")
        for fold_name in file_name:
            if fold_name == 'dev':
                continue
            for cog in os.listdir(path + '/' + fold_name):
                if cog.endswith(".py"):
                    if cog == "admin.py":
                        continue
                    try:
                        self.bot.reload_extension(f"cogs.{fold_name}.{cog[:-3]}")
                    except commands.ExtensionNotLoaded:
                        self.bot.load_extension(f"cogs.{fold_name}.{cog[:-3]}")
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
        for fold_name in file_name:
            await ctx.send(fold_name)
            for cog in os.listdir(path + fold_name):
                if cog.endswith(".py"):
                    await ctx.send(cog)
        await ctx.send('end')
def setup(bot):
    bot.add_cog(Admin(bot))