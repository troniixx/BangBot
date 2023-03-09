import asyncio
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get


intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

activity = discord.Game(name="with your nipples")
client = commands.Bot(command_prefix=";", intents=intents, help_command=None, activity = activity)

@client.command()
async def load(ctx, extension):
    
    await client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} loaded')
    print("--------------------------------------")


@client.command()
async def unload(ctx, extension):

    await client.unload_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} unloaded')
    print("--------------------------------------")


@client.command()
async def reload(ctx, extension):

    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')
    print("--------------------------------------")
    print(f'Cog {extension} reloaded')
    print("--------------------------------------")


async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


with open("TOKEN.txt") as f:
    token = f.read()


async def main():
    async with client:
        await load_extensions()
        await client.start(token)

asyncio.run(main())

