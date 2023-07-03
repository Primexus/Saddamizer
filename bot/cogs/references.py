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
        if 'sleep' in message.content.lower():
            await ctx.reply(random.choice(sleep))

        # Quoi Reference
        if self.is_last_word(message, 'quoi'):
            await ctx.reply(random.choice(quoi))

        if len(message.content.split()) == 2 and self.filter_message(message) == "im":
            await ctx.reply(f"Hi {message.content.split()[1]}, I'm Saddamizer!")

        

async def setup(client):
    await client.add_cog(References(client))