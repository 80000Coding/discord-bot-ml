import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAIN_CHANNEL_ID = int(os.getenv("MAIN_CHANNEL_ID"))
OUTPUT_CHANNEL_ID = int(os.getenv("OUTPUT_CHANNEL_ID"))

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_channel(MAIN_CHANNEL_ID)
    await channel.send("Hello! Gonkapo is here!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    msg_to_send = f"Result: {result}"
    await ctx.send(msg_to_send)
    another_channel  = bot.get_channel(OUTPUT_CHANNEL_ID)
    await another_channel.send(msg_to_send)

bot.run(BOT_TOKEN)
