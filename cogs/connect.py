import discord
from discord.ext import commands

class Connect(commands.Cog):

    intents = discord.Intents.all()
    intents.members = True
    intents.typing = True
    intents.presences = True

    def __init__(self, client):
        self.client = client

    client = discord.Client(intents=intents)

    @commands.Cog.listener()
    async def on_ready(self):
        print("--------------------------------------")
        print('BangBot is currently running')
        print("--------------------------------------")



# adds class to cogs
async def setup(client):
    await client.add_cog(Connect(client))