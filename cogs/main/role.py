import discord
from discord.ext import commands

ROLE_MSGID = 752401701562089532
LANG_MSGID = 752401585761550563
ro_list = {

}

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
#認証
    @commands.Cog.listener()
    async def on_member_join(self,member):
        role = discord.utils.find(lambda r: r.name == 'Server member', member.guild.roles)
        #role = guild.get_role(738979069009461299)
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id!=738994215362625536:
            return
        if "I already understand the server conventions and adhere to them." in message.content:
            await message.add_reaction('\U00002b55')
            role = discord.utils.find(lambda r: r.name == 'verified', message.guild.roles)
            await message.author.add_roles(role)
            roled = discord.utils.find(lambda r: r.name == 'Server member', message.guild.roles)
            await message.author.remove_roles(roled)
            return
        else:
            await message.add_reaction('\U0000274c')
            return
#リアクションロール
    @commands.Cog.listener() 
    async def on_raw_reaction_add(self, re): 
    #変換
        #channel = self.bot.get_channel(re.channel_id)
        #guild = self.bot.get_guild(re.guild_id)  
        #member = guild.get_member(re.user_id)  
        langs_list=self.bot.get_cog('Contents').langs_list
        number_list = self.bot.get_cog('Contents').number_list
    #設定
        if re.message_id == ROLE_MSGID:# and re.emoji not in number_list:
            if str(re.emoji) == '\U000020e3':
                for reac in number_list:
                    await re.message.add_reaction(reac)
            #role = guild.get_role(ro_list[re.emoji])  
            #await member.add_roles(role)

        if re.message_id == LANG_MSGID and re.emoji not in langs_list:  
            if re.emoji == '\U00000031':
                for reac in number_list:
                    await re.message.add_reaction(reac)
            


def setup(bot):
    bot.add_cog(Role(bot))