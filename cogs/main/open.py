import discord
from discord.ext import commands

en_channel=742244607298895942
jp_channel=742244652115034203
ot_channel=742244760462295051

#スレッド作成関数
async def maker(self, message, category_id):
    try:
        category = message.guild.get_channel(category_id)
    except AttributeError:
        return
    nch=await category.create_text_channel(name=message.content) 
    embed = discord.Embed(description=message.author.mention+"created "+nch.mention,color=0x009193)
    await message.channel.send(embed=embed)

class Open(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id==en_channel:
            await maker(self, message,738994847624593488)
            return
        if message.channel.id==jp_channel:
            await maker(self, message,738994847624593488)
            return
        if message.channel.id==ot_channel:
            await message.channel.send('送信しました')
            return
        if message.channel.category.id==738994847624593488:
            await message.channel.edit(pisition=22)
def setup(bot):
    bot.add_cog(Open(bot))