import discord
from discord.ext import commands

re_list=[]

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
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

    @commands.Cog.listener()
    async def on_member_join(self,member):
        role = discord.utils.find(lambda r: r.name == 'Server member', member.guild.roles)
        #role = guild.get_role(738979069009461299)
        await member.add_roles(role)
    '''
    @commands.Cog.listener() 
    async def on_raw_reaction_add(self, re): 
    #変換
        re_emoji = re.emoji 
        channel = self.bot.get_channel(re.channel_id)
        guild = self.bot.get_guild(re.guild_id)  
        member = guild.get_member(re.user_id)  
    #設定
        ROLE_CHANNEL = 0
        re_list=[]
        ro_list=[] 
        if channel.id != ID_CHANNEL_README or re_emoji not in re_list:
            return  
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)
    '''

def setup(bot):
    bot.add_cog(Role(bot))