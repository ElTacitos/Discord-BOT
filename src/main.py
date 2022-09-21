import asyncio

from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

from src.admin import Admin
from src.warmup import Warmup

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,  # Commands aren't case-sensitive
    intents=intents  # Set up basic permissions
)
client = discord.Client(intents=intents)

bot.author_id = 315509578924032010  # Change to your discord id


@bot.event
async def on_ready():  # When the bot is ready
    await bot.add_cog(Warmup(bot))
    await bot.add_cog(Admin(bot))
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command()
async def pong(ctx):
    await ctx.send('pong')


bot.run(os.getenv("TOKEN"))
