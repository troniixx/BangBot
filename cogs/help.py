import discord
from discord.ext import commands

class Help(commands.Cog):

    intents = discord.Intents.all()
    intents.members = True
    intents.typing = True
    intents.presences = True

    def __init__(self, client):
        self.client = client

    client = discord.Client(intents=intents)

    #client.remove_command("help")

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(
            color = discord.Color.green())
        
        embed.set_author(name='Help : list of commands available.')
        embed.add_field(name=';ping', value='Returns bot respond time in milliseconds', inline=False)
        embed.add_field(name=';8ball', value='Ask the magic 8ball a question', inline=False)
        embed.add_field(name=';quote', value='Get inspired by a powerful quote', inline=False)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Help(client))