import discord
from discord.ext import commands
from googletrans import Translator
    
class Translation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        channel = self.bot.get_channel(payload.channel_id)
        reacted_message = await channel.fetch_message(payload.message_id)
        if str(payload.emoji) == '\N{REGIONAL INDICATOR SYMBOL LETTER J}\N{REGIONAL INDICATOR SYMBOL LETTER P}':
            translator = Translator()
            trans_ja = translator.translate(reacted_message.content, dest='ja')
            await channel.send(trans_ja.text)
            return
        if str(payload.emoji) == '\N{REGIONAL INDICATOR SYMBOL LETTER U}\N{REGIONAL INDICATOR SYMBOL LETTER S}':
            translator = Translator()
            trans_en = translator.translate(reacted_message.content, dest='en')
            await channel.send(trans_en.text)
            return
        if str(payload.emoji) == '\N{REGIONAL INDICATOR SYMBOL LETTER D}\N{REGIONAL INDICATOR SYMBOL LETTER E}':
            translator = Translator()
            trans_de = translator.translate(reacted_message.content, dest='de')
            await channel.send(trans_de.text)
            return
def setup(bot):
    bot.add_cog(Translation(bot))