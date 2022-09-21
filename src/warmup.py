import random
from discord.ext import commands


class Warmup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  # now you'll use self.bot instead of just bot when referring to the bot in the code

    # this is how you register events, instead of using @bot.event
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "Salut tout le monde":
            await message.channel.send("Salut tout seul")

    @commands.command()
    async def name(self, message):
        await message.channel.send(message.author.name)

    @commands.command()
    async def d6(self, message):
        await message.channel.send(random.randint(1, 6))


# this setup function needs to be in every cog in order for the bot to be able to load it
def setup(bot):
    bot.add_cog(Warmup(bot))
