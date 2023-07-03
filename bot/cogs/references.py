import random
import discord
from discord.ext import commands

from bot.data.replies import *

class References(commands.Cog, name="References"):
    def __init__(self, bot):
        self.bot = bot

    def is_last_word(self, message, word):
        return message.content.lower().split()[-1].rstrip('?!.,;:').strip() == word

    def filter_message(self, message):
        return message.content.lower().split()[-1].rstrip('?!.,;:')

    @commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.bot.get_context(message)
        if message.author == self.bot.user:
            return

        # Saddam Hussein Reference
        if sleep_regex.search(message.content):
            await ctx.reply(random.choice(sleep))
            return

        # Quoi Reference
        if quoi_regex.search(message.content):
            await ctx.reply(random.choice(quoi))
            return
        
        # HEE HEE HEE HAW Reference
        if heeheeheehaw_regex.search(message.content):
            await ctx.reply(random.choice(heeheeheehaw))
            return
        
        # Forbidden Leo Reference
        if leo_regex.search(message.content):
            await message.delete()

        # I'm Reference
        if im_regex.search(message.content):
            await ctx.reply(f"Hi {message.content.split()[-1]}, I'm Saddamizer!")
            return
        
async def setup(client):
    await client.add_cog(References(client))