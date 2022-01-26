import dotenv
import nextcord
import os
import random
from nextcord.ext import commands

myIntents = nextcord.Intents.default()
myIntents.members = True

bot = commands.Bot(command_prefix="$ ", intents=myIntents, description="Test Bot!")

dotenv.load_dotenv()
myToken = os.getenv("token")
bot.run(myToken)

@bot.command()
async def ping(ctx):
    """ Will respond with the message 'pong' """
    await ctx.send("pong")

@bot.command()
async def repeat(ctx, num: int, *, msg):
    """repeat a message num times"""
    if num < 1:
        num = 1
    for i in range(num):
        await ctx.send(msg)





