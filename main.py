import asyncio
import json
import os
import sys

import discord
from discord import app_commands
from discord.ext import commands

print('[INIT]: Successfully imported libraries.')

# Creates a configuration json file if it doesn't exist.
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "!", "Owner": ""}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)
    sys.exit(
        "[WARNING]: Seems like it's your first time running it. \n"
        "Set up your configurations in the json file before launching it again."
    )

try:
    token = configData["Token"]
    prefix = configData["Prefix"]
    owner = int(configData["Owner"])
except ValueError:
    sys.exit("[ERROR]: A configuration is not valid. Please check it again.")

print('[INIT]: Configurations are checked.')


class SetupBot(commands.Bot):
    def __init__(self):
        self.synced = False
        intents = discord.Intents.all()
        print('[INIT]: Intents have been declared.')
        
        activity = discord.Activity(type=discord.ActivityType.watching, name="obscure references")
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'), 
            owner_id=owner, 
            intents=intents,
            activity=activity, 
            status=discord.Status.online
        )
        print('[INIT]: Activity and status are up.')

    async def setup_hook(self) -> None:
        self.remove_command("help")
        for filename in os.listdir('./bot/cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'bot.cogs.{filename[:-3]}')

    async def on_ready(self) -> None:
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print(f'[EVENT]: {self.user.name} is ready to tell obscure references.\n------')


client = SetupBot()

async def main():
    async with client:
        @client.command()
        @commands.is_owner()
        async def sleep(ctx):
            if ctx.voice_client:
                await ctx.guild.voice_client.disconnect()
            await client.change_presence(status=discord.Status.offline)
            await client.close()
            print('[EVENT]: {self.user.name} successfully sealed herself away.')

        await client.start(token)

asyncio.run(main())
