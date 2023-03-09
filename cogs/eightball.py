import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

class eightBall(commands.Cog):

    intents = discord.Intents.all()
    intents.members = True
    intents.typing = True
    intents.presences = True

    def __init__(self, client):
        self.client = client

    client = discord.Client(intents=intents)

    @commands.command(aliases =['8ball', 'questions'])
    async def EigtBall(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'{random.choice(responses)}')

async def setup(client):
    await client.add_cog(eightBall(client))