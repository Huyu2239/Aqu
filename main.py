import discord
from discord.ext import commands
import json
import asyncio 
import traceback 
import os  

with open('setting.json', mode='r', encoding='utf-8') as sett:
    set_json = sett.read()

    status = json.loads(set_json)['bot_status']
    token = status['token']
    prefix = status['prefix']
    logch_id = status['log_ch_id']

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        path="./cogs"
        for cog in os.listdir(path+"/central"):
            if cog.endswith(".py"):
                try:
                    self.load_extension(f"cogs.central.{cog[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    self.load_extension(f"cogs.central.{cog[:-3]}")
        for cog in os.listdir(path+"/main"):
            if cog.endswith(".py"):
                try:
                    self.load_extension(f"cogs.main.{cog[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    self.load_extension(f"cogs.main.{cog[:-3]}")
        for cog in os.listdir(path+"/common"):
            if cog.endswith(".py"):
                try:
                    self.load_extension(f"cogs.common.{cog[:-3]}")
                except commands.ExtensionAlreadyLoaded:
                    self.load_extension(f"cogs.common.{cog[:-3]}")
        await self.change_presence(activity=discord.Game(name=f"{prefix}about"))

    async def on_ready(self):
        print('-----')
        print('起動')
        print('-----')

    async def on_command_error(self, ctx, error1):
        orig_error = getattr(error1, "original", error1)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        error_msg = "```py\n" + error_msg + "\n```"
        await self.get_channel(logch_id).send(error_msg)

if __name__ == '__main__':
    bot = MyBot(command_prefix=prefix) 
    bot.run(token) 
