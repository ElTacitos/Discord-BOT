import json
from discord.ext import commands
import requests


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def xkcd(self, message):
        request = requests.get("https://random-xkcd-img.herokuapp.com/").text
        body = json.loads(request)
        await message.channel.send(body["url"])

    @commands.command()
    async def poll(self, ctx, question: str):
        message = await ctx.send(f'@here {question}')
        await message.add_reaction('👍')
        await message.add_reaction('👎')


def setup(bot):
    bot.add_cog(Fun(bot))
