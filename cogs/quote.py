import discord
from discord.ext import commands
import random

class Quote(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx):
        responses = open('quotes.txt').read().splitlines()
        random.seed(a=None)
        response = random.choice(responses)
        await ctx.send(response)


async def setup(client):
    await client.add_cog(Quote(client))